import os #for file operations
from pathlib import Path  #for path manipulations
import logging  #for logging messages

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:') # set up logging configuration

project_name="textSummarizer"

list_of_files = [
    ".github/workflows/.gitleep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trial.ipynb"]

# Function to create files and directories
for file_path in list_of_files:
    filepath=Path(file_path)
    filedir, filename = os.path.split(filepath)  # Split into directory and file name
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir}")

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
            logging.info(f"Creating file: {filepath}")
    else:
        logging.warning(f"File already exists: {filepath}")