import argparse

from AlumnoMasBajo import Alumno
from AlumnoMasBajo import AlumnoMasBajo
from DivisionYConquista import DivisionYConquista
from Grafo import biblioteca
from Grafo.grafo import Grafo


def ejecutar_raiz_entera(numero):
    print(DivisionYConquista.parte_entera_raiz(numero))


def parsear_alumnos(entradas):
    alumnos = []
    for entrada in entradas:
        nombre, altura = entrada.split(":", maxsplit=1)
        alumnos.append(Alumno(nombre, float(altura)))
    return alumnos


def ejecutar_alumno_mas_bajo(alumnos_raw):
    alumnos = parsear_alumnos(alumnos_raw)
    indice = AlumnoMasBajo.indice_mas_bajo(alumnos)
    alumno = alumnos[indice]
    print(f"indice={indice} nombre={alumno.nombre} altura={alumno.altura}")


def construir_grafo(vertices, aristas):
    grafo = Grafo()
    for vertice in vertices:
        grafo.agregar_vertice(vertice)

    for arista in aristas:
        origen, destino = arista.split(":", maxsplit=1)
        grafo.agregar_arista(origen, destino)

    return grafo


def ejecutar_bipartito(vertices, aristas):
    grafo = construir_grafo(vertices, aristas)
    print(biblioteca.es_bipartito(grafo))


def crear_parser():
    parser = argparse.ArgumentParser(
        description="CLI para ejecutar ejemplos del repositorio RPLTDA"
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_raiz = subparsers.add_parser(
        "raiz",
        help="Calcula la parte entera de la raiz cuadrada de un numero",
    )
    parser_raiz.add_argument("numero", type=int)

    parser_alumno = subparsers.add_parser(
        "alumno",
        help="Obtiene el alumno mas bajo de una lista nombre:altura",
    )
    parser_alumno.add_argument(
        "alumnos",
        nargs="+",
        help="Lista de alumnos con formato nombre:altura",
    )

    parser_bipartito = subparsers.add_parser(
        "bipartito",
        help="Verifica si un grafo no dirigido es bipartito",
    )
    parser_bipartito.add_argument(
        "--vertices",
        nargs="+",
        required=True,
        help="Vertices del grafo",
    )
    parser_bipartito.add_argument(
        "--aristas",
        nargs="+",
        required=True,
        help="Aristas con formato origen:destino",
    )

    return parser


def main():
    parser = crear_parser()
    args = parser.parse_args()

    if args.comando == "raiz":
        ejecutar_raiz_entera(args.numero)
    elif args.comando == "alumno":
        ejecutar_alumno_mas_bajo(args.alumnos)
    elif args.comando == "bipartito":
        ejecutar_bipartito(args.vertices, args.aristas)


if __name__ == "__main__":
    main()
