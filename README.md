# La Bayeta de la Fortuna

Bienvenido al proyecto "La Bayeta de la Fortuna". Esta aplicación web sencilla te proporcionará un mensaje auspicioso aleatorio cada vez que accedas a ella. Para desarrollar y desplegar la aplicación, aseguraremos la eficiencia en el manejo del código, la colaboración y la publicación de distintas versiones. Además, nos aseguraremos de que el entorno de ejecución sea consistente en local y en un servidor.

## Tabla de Contenidos

- [La Bayeta de la Fortuna](#la-bayeta-de-la-fortuna)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Tecnologías](#tecnologías)
  - [Requisitos](#requisitos)
  - [Configuración del Entorno](#configuración-del-entorno)
  - [Desarrollo Colaborativo](#desarrollo-colaborativo)
  - [Ejecución](#ejecución)
    - [Python](#python)
    - [Docker](#docker)

## Tecnologías

- Python
- FastAPI
- Git
- Docker
- Docker Compose

## Requisitos

Asegúrate de tener instalados los siguientes elementos antes de comenzar:

- Python (con virtual environment - venv)
- Git
- Docker

## Configuración del Entorno

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/asaura08/pps_python_git_docker.git
cd pps_python_git_docker
```

2. Ejecuta el script `setup.sh` para crear el entorno virtual y ejecutar la aplicación de forma local sin Docker:

```bash
./setup.sh
```

## Desarrollo Colaborativo

Trabajaremos colaborativamente utilizando Git. Asegúrate de seguir estas prácticas:

- Crea ramas para nuevas funcionalidades o correcciones: `git checkout -b nombre-de-la-rama`
- Commitea tus cambios de forma descriptiva: `git commit -m "Añadida funcionalidad X"`
- Publica tus cambios en tu repositorio: `git push origin nombre-de-la-rama`
- Abre Pull Requests para revisión y mezcla de cambios

## Ejecución

Esta app se puede ejecutar de dos formas: con Python o con Docker.


Accede a la aplicación desde tu navegador en [http://localhost:8000](http://localhost:8000).

### Python

Si prefieres ejecutar la aplicación con Python, asegúrate de tener Python instalado y sigue estos pasos:

1. Ejecuta el script `setup.sh` para crear el entorno virtual y ejecutar la aplicación de forma local sin Docker:

```bash
./setup.sh
```

2. Si ya has ejecutado el script anterior, puedes activar el entorno virtual con el siguiente comando:

```bash
source venv/bin/activate
```

3. Ejecuta la aplicación:

```bash
uvicorn app:app --reload
```

### Docker


Si prefieres ejecutar la aplicación con Docker, asegúrate de tener Docker-compose y sigue estos pasos:

1. Levanta los contenedores:

```bash
docker-compose up -d
```

Accede a la aplicación desde [http://localhost:8000](http://localhost:8000).

¡Disfruta de la fortuna que te brinda La Bayeta de la Fortuna! 🌟