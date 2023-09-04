import os
from pathlib import Path
import logging
from datetime import datetime

filedir = "LOGS"
filename = f"template_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
filepath = os.path.join(filedir, filename)

PROJECT_NAME = "books_recommender"

os.makedirs(filedir, exist_ok=True)

with open(filepath, "w") as f:
    pass

logging.basicConfig(
    filename=filepath, 
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)


logging.info("Project template creation🪄🪄 begin.....")


PATHS = [
    "README.md",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/logger.py",
    f"src/{PROJECT_NAME}/exception.py",
    "app.py",
    "main.py",
    ".github/workflows/.gitkeep",
    "params.yaml",
    "research/research01.ipynb",
    "research/research02.ipynb",
    "config/config.yaml",
    "templates/index.html",
    "static/css/style.css",
    "static/images",
    "static/js/script.js",
]

for path in PATHS:
    path = Path(path)
    filedir, filename = os.path.split(path)
    
    if filedir != '' and not os.path.exists(filedir):
        os.makedirs(filedir)
        logging.info(f"{filedir} dir creation successful.")
    
    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
            pass
    else:
        logging.info(f"{filename} is already exists")


logging.info("Folder✉️✉️ creation successful")