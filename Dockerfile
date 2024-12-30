# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r app/requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]

ENV PYTHONPATH=/app