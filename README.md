# Tercer Pre entrega

## 1 - Crear entorno virtual

py -m venv .\venv

## 2 - Dar permisos

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

## 3 - Activar entorno virtual

venv\Scripts\activate

## 4 - Instalar dependencias

pip install -r requirements.txt

## 5 - Levantar el servidor

python manage.py runserver

## Rutas disponibles

- / - Index
- /cars  - Añadir auto
- /customer - Añadir cliente
- /garage - Añadir Sucursal
- /seach - Buscar autos por marca