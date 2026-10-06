"""Console user interface."""

from __future__ import annotations
import pandas as pd

def solicitar_datos() -> tuple[int, str, str | None, str | None]:
    """Request search filters and record limit."""
    departamento = input(
        "Department to search (e.g. BOGOTA, ANTIOQUIA): "
    ).strip().upper()
    while True:
        try:
            limite = int(input("Number of records to display: "))
            if limite > 0:
                break
        except ValueError:
            pass
        print("Enter a positive integer.")

    tipo_contagio = input(
        "Type of transmission (optional, e.g. IMPORTADO, COMUNITARIA): "
    ).strip().capitalize() or None
    estado = input(
        "Status (optional, e.g. LEVE, GRAVE, FALLECIDO): "
    ).strip().capitalize() or None
    return limite, departamento, tipo_contagio, estado


def mostrar_casos(casos: pd.DataFrame) -> None:
    """Print the records using format() for specific columns."""
    if casos.empty:
        print("No records found for the given criteria.")
        return

    print("\n{:<25} | {:<20} | {:<5} | {:<15} | {:<10} | {:<20}".format(
        "Ciudad de ubicación", "Departamento", "Edad", "Tipo", "Estado", "País de procedencia"
    ))
    print("-" * 105)

    for _, fila in casos.iterrows():
        ciudad = str(fila.get('ciudad_municipio_nom', 'N/A'))[:24]
        depto = str(fila.get('departamento_nom', 'N/A'))[:19]
        edad = str(fila.get('edad', 'N/A'))[:4]
        tipo = str(fila.get('fuente_tipo_contagio', 'N/A'))[:14]
        estado = str(fila.get('estado', 'N/A'))[:9]
        pais = str(fila.get('pais_viajo_1_nom', 'N/A'))[:19]
        if pd.isna(fila.get('pais_viajo_1_nom')): pais = 'N/A'

        print("{:<25} | {:<20} | {:<5} | {:<15} | {:<10} | {:<20}".format(
            ciudad, depto, edad, tipo, estado, pais
        ))
