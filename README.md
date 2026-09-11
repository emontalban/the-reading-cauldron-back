# The Reading Cauldron

The Reading Cauldron back, Es el backend de una aplicación full stack de biblioteca personal.

Este backend estará desarrollado con **Python Flask** y se encarga de gestionar la API, la conexión con la base de datos MySQL, la autenticación de usuarios y las operaciones de CRUD para los libros.

## Descripción del proyecto

The Reading Cauldron es una aplicación web donde cada usuario puede crear y gestionar su propia biblioteca personal.

El usuario podrá añadir libros, editarlos, eliminarlos, marcar su estado de lectura y guardar notas personales y asi llevar un registro de todos sus libros en una biblioteca privada.

## Tecnologías utilizadas

* Python
* Flask
* Flask-CORS
* MySQL
* REST API
* Git
* GitHub
## Estructura del proyecto

```text
the-reading-cauldron-back/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── schema.sql
│
├── routes/
│   ├── __init__.py
│   ├── home_routes.py
│   ├── db_routes.py
│   ├── books_routes.py
│   ├── user_routes.py
│   ├── auth_routes.py
│   └── library_routes.py
│
├── queries/
│   ├── __init__.py
│   ├── db_queries.py
│   ├── books_queries.py
│   ├── users_queries.py
│   └── library_queries.py
│
├── helpers/
    ├── __init__.py
    ├── auth_helpers.py
    └── library_validations.py


```
## Funcionalidades principales del backend

* Conexion con base de datos MySQL
* Registro de usuarios
* Login con JWT
* Inicio de sesión
* CRUD de libros
* Validaciones para los datos de la biblioteca

## Base de datos

La base de datos utilizada es:

the_reading_cauldron_db

Tablas principales:

- users
- books
- library

La tabla `library` conecta usuarios con libros y guarda información personal de lectura, como estado, formato, páginas leídas, valoración, notas y propiedad del libro.

## Instalación

- Clonar el repositorio
- Entrar en la carpeta del proyecto

- Crear el entorno virtual:

    ```bash
    py -m venv venv
    ```

- Activar el entorno virtual en Windows:

    ```bash
    .\venv\Scripts\activate
    ```

- Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

- Ejecutar el servidor

    ```bash
    python app.py
    ```

- El servidor se ejecutará en:

    ```txt
    http://127.0.0.1:5000
    ```

