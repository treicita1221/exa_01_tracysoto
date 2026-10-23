"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación II
Period.......: 3-2026
Document.....: cls_Jugador.py
Goals........: Clase Jugador; cada jugador tiene su propia pila de naipes (composición)
Professor....: Jorge Ruiz (york)
Student......: Tracy Soto Castrillo
================================================================================================="""
from cls_Stack import cls_Stack


class cls_Jugador:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self.partida = cls_Stack()          # composición: el jugador TIENE una pila
        self._naipes_obtenidos = []         # naipes que va sacando durante el juego

        # Validación: la pila debe estar vacía antes de usarse
        if not self.partida.isempty():
            raise RuntimeError("La partida debe iniciar vacía.")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def naipes_obtenidos(self) -> list:
        return self._naipes_obtenidos

    def tiene_naipes(self) -> bool:
        return not self.partida.isempty()

    def sacar_naipe(self) -> str:
        """Saca el naipe del tope de su pila y lo guarda en sus naipes obtenidos."""
        naipe = self.partida.pop()
        self._naipes_obtenidos.append(naipe)
        return naipe

    def vaciar_partida(self) -> None:
        """Deja la pila vacía al terminar el juego."""
        while not self.partida.isempty():
            self.partida.pop()

    def __str__(self) -> str:
        return self._nombre
