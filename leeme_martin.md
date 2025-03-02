# Hice un workspace para todo menos frontend y otro para frontend.

# En lo que no es frontend se encuentra: .venv, backend, modelosdb, alembic.ini,database.py y el dockercompose

# En la carpeta de frontend tuve la mala idea de también crear ahi un ambiente virtual venv, pero la verdad es que ahi no se corre python sino puto javascript. No hace ningún daño pero puede ser borrado.

# Se supone que ya cambié para siempre la configuracion en VSCode de que la rama inicial de los repositorios no será aster, sino main.

# Esta bueno requirements.txt para de inicio hacer un pip install apuntando a ese archivo.

# Línea para iniciar el ambiente virual de python

> .\.venv\Scripts\activate

# Para que alembic realice las migraciones, en la ruta raiz ejecutar

> alembic revision --autogenerate -m "..."
> alembic upgrade head

# FastApi es muy fácil, creo que no necesito hacer comentarios; lo único es la forma de correr el uvicorn porque se debe establecer el path en la ruta padre para que vea el folder de los modelos

> $env:PYTHONPATH = (Get-Location).Path; uvicorn backend.main:app --reload

# En el main.py de FastAPI hay un llamado a app.add_middleware el cual es miu relevante porque le dice que puede recibir peticiones de host:puerto del frontend.

# Si bien la creación del frontend es con react, es con la variante Vite + React que se instala y se corre el servidor con comandos distintos a react puro.

# Para correr el frontend, desde la ruta de la app de react ejecutar

> npm run dev

# En la ruta raiz del frontend (aquí llamado my-react-app) se tuvo que crear un archivo .env para indicar > a Vite el endpoint ( o endpoints) del backend que va a ocupar. Aunque hice pruebas comentando esa línea y no afectó la ejecución de la app; seguramente porque en App.jsx esta la siguiente línea **const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/tasks";**

# Del docker compose para la bd de Postgress correr los comandos desde la ruta raiz-

> docker-compose up -d
> docker ps
> docker-compose down
