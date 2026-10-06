# Proyecto Modulo 1 Programación III

**Desarrolladores:** Bryan E. Gonzalez Hincapie - Salomé Chavez Suarez

**Docente:** Alejandro Rodas Vasquez

## Objetivo

Consultar casos de COVID-19 en Colombia mediante la API oficial de Datos Abiertos,
procesarlos con `pandas` y presentarlos en la consola.

## Estructura

```text
ProyectoAPI/
├── api/
│   ├── __init__.py
│   └── cliente_api.py
├── ui/
│   ├── __init__.py
│   └── interfaz.py
├── main.py
├── requirements.txt
└── README.md
```

## Entorno virtual

```bash
cd /home/ian/Documents/PrograIII/ProyectoAPI_PrograIII/
python3 -m venv .venv-ProyectoAPI
source .venv-ProyectoAPI/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```
