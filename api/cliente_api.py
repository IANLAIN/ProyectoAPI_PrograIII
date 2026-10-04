"""Socrata API client."""

from __future__ import annotations
from typing import Any
import pandas as pd
from sodapy import Socrata

DOMAIN = "www.datos.gov.co"
DATASET_ID = "gt2j-8ykr"

def obtener_casos(limite: int, departamento: str) -> pd.DataFrame:
    """Fetch COVID-19 records filtered by department."""
    if limite < 1:
        raise ValueError("The limit must be greater than zero.")

    with Socrata(DOMAIN, None) as cliente:
        registros: list[dict[str, Any]] = cliente.get(
            DATASET_ID,
            limit=limite,
            departamento_nom=departamento.upper()
        )

    return pd.DataFrame.from_records(registros)
