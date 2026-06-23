# The Reading Cauldron - Backend

Backend de **The Reading Cauldron**, una aplicación full stack de biblioteca personal.

Este backend estará desarrollado con **Python Flask** y se encargará de gestionar la API, la conexión con la base de datos MySQL, la autenticación de usuarios y las operaciones CRUD para los libros.

## Descripción del proyecto

The Reading Cauldron es una aplicación web donde cada usuario puede crear y gestionar su propia biblioteca personal.

El usuario podrá añadir libros, editarlos, eliminarlos, marcar su estado de lectura y guardar notas personales.

## Tecnologías utilizadas

* Python
* Flask
* MySQL
* REST API
* Git
* GitHub

## Funcionalidades principales del backend

* Registro de usuarios
* Inicio de sesión
* Gestión de libros
* Crear libros
* Ver libros
* Editar libros
* Eliminar libros
* Conexión con base de datos MySQL

## Estructura inicial del proyecto

```txt
the-reading-cauldron-backend/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── routes/
│   └── books_routes.py
│
├── database/
│   └── connection.py
│
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/emontalban/the-reading-cauldron-back
```

Entrar en la carpeta del proyecto:

```bash
cd the-reading-cauldron-backend
```

Crear el entorno virtual:

```bash
py -m venv venv
```

Activar el entorno virtual en Windows:

```bash
.\venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar el servidor

```bash
python app.py
```

El servidor se ejecutará en:

```txt
http://127.0.0.1:5000
```

