FROM python:3.10.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copia todos los archivos de tu ruta local al directorio de trabajo en el contenedor
COPY . /usr/src/app

# Instala los paquetes definidos en requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto en el que Django se ejecutará
EXPOSE 8000

# Comando para ejecutar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
