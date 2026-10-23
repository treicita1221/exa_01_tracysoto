"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación II
Period.......: 3-2026
Document.....: problema2.py
Goals........: Buscando a la Reina de Corazones (QC)
Professor....: Jorge Ruiz (york)
Student......: Tracy Soto Castrillo
================================================================================================="""
from time import sleep
from cls_Jugador import cls_Jugador
from Subrutinas import repartir_naipes

REINA_CORAZONES = "QC"
ANCHO = 12          # ancho de cada columna al imprimir
ESPERA = 2          # segundos entre un jugador y otro


def imprimir_encabezado(jugadores: list) -> None:
    for jugador in jugadores:
        print(f"{jugador.nombre:<{ANCHO}}", end="")
    print()
    print("-" * ANCHO * len(jugadores))


def jugar(jugadores: list):
    """Cada jugador saca un naipe por turno. Devuelve el ganador o None si nadie sacó la QC."""
    imprimir_encabezado(jugadores)

    while any(jugador.tiene_naipes() for jugador in jugadores):
        for jugador in jugadores:
            if jugador.tiene_naipes():
                naipe = jugador.sacar_naipe()
            else:
                naipe = ""
            print(f"{naipe:<{ANCHO}}", end="", flush=True)

            if naipe == REINA_CORAZONES:
                print()
                return jugador

            sleep(ESPERA)
        print()   # termina la fila (la ronda)

    return None


def main() -> None:
    print()
    print("Buscando a la Reina de Corazones")
    print("================================\n")

    # 1. Crear los 4 jugadores (cada uno crea su pila en el constructor)
    jugadores = [cls_Jugador(nombre) for nombre in ["Merlina", "Tío Lucas", "Pericles", "Homero"]]

    # 2. Repartir los naipes (función en Subrutinas.py)
    repartir_naipes(jugadores)

    # 3. Jugar
    ganador = jugar(jugadores)

    # 4. Resultado
    print()
    if ganador is not None:
        print(f"¡{ganador.nombre} encontró la Reina de Corazones y gana el juego!")

        # List comprehension: solo los naipes de Corazón (terminan en "C")
        corazones = [naipe for naipe in ganador.naipes_obtenidos if naipe.endswith("C")]
        # (Equivalente con lambda y filter:)
        # corazones = list(filter(lambda naipe: naipe.endswith("C"), ganador.naipes_obtenidos))

        print(f"Naipes de Corazón que acumuló {ganador.nombre}: {corazones}")
    else:
        print("Se acabaron los naipes y nadie sacó la Reina de Corazones. No hay ganador.")

    # 5. Validación: todas las pilas deben quedar vacías al final
    for jugador in jugadores:
        jugador.vaciar_partida()
        if not jugador.partida.isempty():
            raise RuntimeError(f"La pila de {jugador.nombre} no quedó vacía.")


if __name__ == "__main__":
    main()
