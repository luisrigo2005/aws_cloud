from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
import boto3
import os
from dotenv import load_dotenv
import psycopg2
import platform
import psutil
import threading
import time

print("Iniciando aplicação...")

# Carrega variáveis de ambiente
load_dotenv()
print("Variáveis de ambiente carregadas")

app = Flask(__name__)
app.secret_key = os.urandom(24)
bootstrap = Bootstrap(app)
print("Flask e Bootstrap inicializados")

# Variáveis globais para controle dos testes de estresse
memory_stress_active = False
memory_stress_data = []

# Configuração AWS
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")
print(f"AWS Region: {AWS_REGION}")
print(f"S3 Bucket: {S3_BUCKET}")

# Configuração RDS
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
print(f"DB Host: {DB_HOST}")
print(f"DB Name: {DB_NAME}")

# Inicializa clientes AWS
try:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    print("Cliente S3 inicializado com sucesso")
except Exception as e:
    print(f"Erro ao inicializar cliente S3: {str(e)}")

@app.route("/")
def index():
    # Obtém informações do sistema
    system_info = {
        "platform": platform.platform(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
    return render_template("index.html", system_info=system_info)

@app.route("/s3")
def s3():
    try:
        # Lista objetos no bucket S3
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        objects = response.get("Contents", [])
        return render_template("s3.html", objects=objects)
    except Exception as e:
        flash(f"Erro ao acessar S3: {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("Nenhum arquivo selecionado", "error")
        return redirect(url_for("s3"))
    
    file = request.files["file"]
    if file.filename == "":
        flash("Nenhum arquivo selecionado", "error")
        return redirect(url_for("s3"))

    try:
        s3_client.upload_fileobj(
            file,
            S3_BUCKET,
            file.filename,
            ExtraArgs={"ACL": "public-read"}
        )
        flash("Arquivo enviado com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao enviar arquivo: {str(e)}", "error")
    
    return redirect(url_for("s3"))

@app.route("/rds")
def rds():
    try:
        # Conecta ao banco de dados
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM exemplo LIMIT 10")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return render_template("rds.html", data=data)
    except Exception as e:
        flash(f"Erro ao conectar ao banco de dados: {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/stress-test")
def stress_test():
    return render_template("stress_test.html")

def memory_stress_test():
    global memory_stress_active, memory_stress_data
    while memory_stress_active:
        try:
            # Aloca memória em blocos de 100MB
            for _ in range(5):  # Tenta alocar 500MB de uma vez
                memory_stress_data.append(' ' * (100 * 1024 * 1024))  # 100MB
            time.sleep(0.1)
        except MemoryError:
            memory_stress_active = False
            break

@app.route("/start-memory-stress", methods=["POST"])
def start_memory_stress():
    global memory_stress_active
    if not memory_stress_active:
        memory_stress_active = True
        thread = threading.Thread(target=memory_stress_test)
        thread.daemon = True
        thread.start()
        return jsonify({"status": "success", "message": "Teste de memória iniciado"})
    return jsonify({"status": "error", "message": "Teste de memória já está em execução"})

@app.route("/stop-memory-stress", methods=["POST"])
def stop_memory_stress():
    global memory_stress_active, memory_stress_data
    memory_stress_active = False
    memory_stress_data.clear()
    return jsonify({"status": "success", "message": "Teste de memória finalizado"})

@app.route("/get-system-metrics")
def get_system_metrics():
    return jsonify({
        "memory_percent": psutil.virtual_memory().percent,
        "memory_used": psutil.virtual_memory().used / (1024 * 1024 * 1024),  # GB
        "memory_total": psutil.virtual_memory().total / (1024 * 1024 * 1024)  # GB
    })

if __name__ == "__main__":
    print("Iniciando servidor Flask...")
    app.run(debug=True)
