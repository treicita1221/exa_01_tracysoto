"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación II
Period.......: 3-2026
Document.....: problema1.py
Goals........: Evaluar si una expresión matemática tiene bien escritos sus paréntesis ( ) [ ] { }
Professor....: Jorge Ruiz (york)
Student......: Tracy Soto Castrillo
================================================================================================="""
from cls_Stack import cls_Stack

# Diccionario: para cada símbolo que CIERRA, cuál es el que lo ABRE
PARES = {")": "(", "]": "[", "}": "{"}
ABREN = "([{"


def vaciar_pila(pila: cls_Stack) -> None:
    """Saca todos los elementos que queden en la pila, para dejarla vacía."""
    while not pila.isempty():
        pila.pop()


def evaluar_expresion(expresion: str, pila: cls_Stack) -> tuple:
    """Revisa la expresión con la pila.
    Devuelve (True, mensaje) si está bien escrita o (False, mensaje) si está mal."""

    # Validación: la pila debe estar vacía ANTES de usarla
    if not pila.isempty():
        vaciar_pila(pila)

    resultado = (True, "La expresión está bien escrita.")

    for posicion, caracter in enumerate(expresion, start=1):
        if caracter in ABREN:
            # Si abre un paréntesis, lo guardamos en la pila
            if pila.isfull():
                resultado = (False, f"Demasiados paréntesis anidados (máximo 10) en la posición {posicion}.")
                break
            pila.push(caracter)

        elif caracter in PARES:
            # Si cierra, la pila NO puede estar vacía (si no, nunca se abrió)
            if pila.isempty():
                resultado = (False, f"Cierra '{caracter}' en la posición {posicion}, pero nunca se abrió.")
                break
            # El último que se abrió debe ser del mismo tipo
            abierto = pila.pop()
            if abierto != PARES[caracter]:
                resultado = (False, f"Abre con '{abierto}' pero cierra con '{caracter}' en la posición {posicion}.")
                break
    else:
        # Si terminó de recorrer y quedaron paréntesis abiertos en la pila, nunca se cerraron
        if not pila.isempty():
            resultado = (False, f"Abre '{pila.peek()}' pero nunca lo cierra.")

    # Validación: la pila debe quedar vacía AL FINALIZAR su uso
    vaciar_pila(pila)
    if not pila.isempty():
        raise RuntimeError("La pila no quedó vacía.")

    return resultado


def main() -> None:
    print()
    print("Evaluación de expresiones matemáticas")
    print("=====================================")

    pila = cls_Stack()

    while True:
        expresion = input("\nDigite la expresión (o 'salir' para terminar): ").strip()
        if expresion.lower() == "salir":
            break
        if expresion == "":
            print("Debe escribir una expresión.")
            continue

        bien, mensaje = evaluar_expresion(expresion, pila)
        print(("✔ " if bien else "✘ ") + mensaje)

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
