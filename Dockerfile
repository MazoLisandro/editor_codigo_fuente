# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el código fuente y el archivo INI al contenedor
COPY editor_codigo.py /app/
COPY config.ini /app/

# Instala Tkinter (necesario para GUI en Docker)
RUN apt-get update && apt-get install -y python3-tk

# Ejecuta la aplicación
CMD ["python", "editor_codigo.py"]
