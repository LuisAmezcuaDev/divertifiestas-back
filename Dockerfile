FROM python:3.11-slim-buster

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Crear y activar el entorno virtual
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copiar el código y los archivos de requisitos
COPY . /app
WORKDIR /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
