import random
# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
          ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
          ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
          ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]]


def repartir_naipes(jugadores: list) -> None:
    """Reparte un naipe a la vez a cada jugador, al azar y sin repetir,
    hasta que la pila de cada jugador esté llena (10 naipes)."""

    # Copia de la baraja en una sola lista (para no dañar la baraja original)
    disponibles = [naipe for palo in baraja for naipe in palo]

    # Mientras algún jugador tenga espacio en su pila, seguimos repartiendo
    while any(not jugador.partida.isfull() for jugador in jugadores):
        for jugador in jugadores:
            if not jugador.partida.isfull():
                naipe = random.choice(disponibles)   # naipe al azar
                disponibles.remove(naipe)            # se quita para que nadie más lo tenga
                jugador.partida.push(naipe)
