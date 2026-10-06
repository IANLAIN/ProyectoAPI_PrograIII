"""Socrata API client."""

from __future__ import annotations
from typing import Any
import pandas as pd
from sodapy import Socrata

DOMAIN = "www.datos.gov.co"
DATASET_ID = "gt2j-8ykr"

def obtener_casos(
    limite: int,
    departamento: str,
    tipo_contagio: str | None = None,
    estado: str | None = None,
) -> pd.DataFrame:
    """Fetch filtered COVID-19 records."""
    if limite < 1:
        raise ValueError("The limit must be greater than zero.")

    filtros: dict[str, str] = {"departamento_nom": departamento.upper()}
    if tipo_contagio:
        filtros["fuente_tipo_contagio"] = tipo_contagio.capitalize()
    if estado:
        filtros["estado"] = estado.capitalize()

    with Socrata(DOMAIN, None) as cliente:
        registros: list[dict[str, Any]] = cliente.get(
            DATASET_ID,
            limit=limite,
            **filtros
        )

    return pd.DataFrame.from_records(registros)
