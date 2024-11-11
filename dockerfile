# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación dentro del contenedor
COPY . .

# Expone el puerto 5000 para que Flask pueda aceptar conexiones
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
