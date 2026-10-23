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

        # Pendiente: aquí se analiza la expresión con la pila
        print(f"Expresión capturada: {expresion}")

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
