# AWS Cloud Practitioner Essentials - Complementar

Este projeto é uma aplicação Flask com integração AWS e PostgreSQL, desenvolvida como material complementar para o curso AWS Cloud Practitioner Essentials.

## Repositório

O código-fonte está disponível em: [https://github.com/luisrigo2005/aws_cloud](https://github.com/luisrigo2005/aws_cloud)

## Funcionalidades
- Upload e download de arquivos no S3
- Integração com banco de dados PostgreSQL
- Teste de estresse de memória com monitoramento em tempo real
- Interface web simples para interação

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/luisrigo2005/aws_cloud.git
   cd aws_cloud
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=SEU_SECRET_KEY
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET=nome-do-bucket
DATABASE_URL=postgresql://usuario:senha@host:porta/banco
```

## Uso

1. Inicie o servidor Flask:
   ```bash
   flask run
   ```
2. Acesse `http://localhost:5000` no navegador.

## Teste de Estresse de Memória
- Acesse a rota `/memory-stress` para iniciar o teste de estresse de memória e visualizar o monitoramento em tempo real.

## Licença

Este projeto é livre para uso educacional.

## Contato

Para suporte ou dúvidas, abra uma issue no repositório. 