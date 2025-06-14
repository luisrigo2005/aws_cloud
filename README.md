# AWS Cloud Practitioner Essentials - Aplicação de Demonstração

Esta aplicação é uma demonstração prática dos conceitos do AWS Cloud Practitioner Essentials, incluindo integração com serviços AWS (S3 e RDS) e ferramentas de monitoramento de sistema.

## Funcionalidades

- Integração com AWS S3 para gerenciamento de arquivos
- Conexão com banco de dados PostgreSQL (RDS)
- Monitoramento de recursos do sistema
- Teste de estresse de memória
- Interface web responsiva com Bootstrap

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta AWS com acesso aos serviços S3 e RDS
- Banco de dados PostgreSQL (pode ser local ou RDS)

## Instalação

1. **Clone ou extraia o projeto**
   ```bash
   # Se estiver usando git
   git clone [URL_DO_REPOSITÓRIO]
   
   # Se estiver usando o arquivo .zip
   # Extraia o conteúdo do arquivo .zip para uma pasta
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   # AWS Credentials
   AWS_ACCESS_KEY=sua_access_key
   AWS_SECRET_KEY=sua_secret_key
   AWS_REGION=sua_regiao
   S3_BUCKET=nome_do_seu_bucket

   # Database Configuration
   DB_HOST=seu_host
   DB_NAME=nome_do_banco
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   ```

## Estrutura do Projeto

```
.
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências do projeto
├── .env               # Configurações (não versionado)
├── static/            # Arquivos estáticos
│   ├── css/          # Estilos CSS
│   ├── js/           # Scripts JavaScript
│   └── img/          # Imagens
└── templates/         # Templates HTML
    ├── base.html     # Template base
    ├── index.html    # Página inicial
    ├── s3.html       # Página do S3
    ├── rds.html      # Página do banco de dados
    └── stress_test.html # Página de teste de estresse
```

## Configuração do Banco de Dados

1. **Crie o banco de dados PostgreSQL**
   ```sql
   CREATE DATABASE nome_do_banco;
   ```

2. **Crie a tabela de exemplo**
   ```sql
   CREATE TABLE exemplo (
       id SERIAL PRIMARY KEY,
       nome VARCHAR(100),
       data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

## Configuração do AWS S3

1. **Crie um bucket S3**
   - Acesse o console AWS
   - Vá para o serviço S3
   - Crie um novo bucket
   - Configure as permissões necessárias

2. **Configure as credenciais AWS**
   - Crie um usuário IAM com acesso ao S3
   - Gere as credenciais de acesso
   - Adicione as credenciais ao arquivo `.env`

## Executando a Aplicação

1. **Ative o ambiente virtual** (se ainda não estiver ativo)
   ```bash
   # Windows
   .\venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

2. **Inicie a aplicação**
   ```bash
   python app.py
   ```

3. **Acesse a aplicação**
   - Abra seu navegador
   - Acesse `http://localhost:5000`

## Uso

1. **Página Inicial**
   - Mostra informações do sistema
   - Links para outras funcionalidades

2. **S3**
   - Lista arquivos no bucket
   - Permite upload de arquivos
   - Visualiza arquivos existentes

3. **Banco de Dados**
   - Visualiza dados da tabela exemplo
   - Mostra os últimos 10 registros

4. **Teste de Estresse**
   - Monitora uso de memória
   - Permite realizar teste de estresse
   - Mostra gráficos em tempo real

## Solução de Problemas

1. **Erro de conexão com AWS**
   - Verifique as credenciais no arquivo `.env`
   - Confirme se as permissões do usuário IAM estão corretas
   - Verifique se a região está correta

2. **Erro de conexão com banco de dados**
   - Verifique as credenciais no arquivo `.env`
   - Confirme se o banco de dados está acessível
   - Verifique se a tabela existe

3. **Erro ao iniciar a aplicação**
   - Confirme se todas as dependências estão instaladas
   - Verifique se o ambiente virtual está ativo
   - Confirme se a porta 5000 está disponível

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para suporte ou dúvidas, abra uma issue no repositório. 