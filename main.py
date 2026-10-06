"""Application entry point."""

from api.cliente_api import obtener_casos
from ui.interfaz import mostrar_casos, solicitar_datos


def ejecutar_pruebas() -> None:
    """Run a minimal API connectivity test."""
    prueba = obtener_casos(2, "BOGOTA", estado="LEVE")
    if len(prueba) > 2:
        raise RuntimeError("The API returned more records than requested.")
    print("Tests passed\n")


def main() -> None:
    """Run tests and start the console interface."""
    ejecutar_pruebas()
    limite, departamento, tipo_contagio, estado = solicitar_datos()
    mostrar_casos(
        obtener_casos(limite, departamento, tipo_contagio, estado)
    )


if __name__ == "__main__":
    main()
