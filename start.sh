#!/bin/bash

# Ejecutar el script de instalación
python install.py

# Iniciar la aplicación
uvicorn main:app --host 0.0.0.0 --port 800