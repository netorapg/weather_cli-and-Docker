# Usar uma imagem base menor para otimização de tamanho
FROM python:3.9-slim AS builder

# Variável de ambiente para a chave da API
ENV WEATHER_API_KEY="365e6b989657cb638c02c6b2f528557b"

# Diretório de trabalho
WORKDIR /app

# Copiar apenas requirements.txt para cache de camadas
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY src/ src/

# Expor variável de entrada do usuário
ENTRYPOINT ["python", "/app/src/weather_cli.py"]
