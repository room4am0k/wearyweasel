"""Menú navegable con flechas."""

import readchar

from utils import limpiar, log


def menu(titulo, opciones):

    seleccion = 0

    while True:
        limpiar()
        log("Clean!")
        print(f"=== {titulo} ===\n")

        for i, opcion in enumerate(opciones):
            indicador = " > " if i == seleccion else "   "
            print(f"{indicador}{opcion}")

        tecla = readchar.readkey()
        log(f"tecla={tecla!r} seleccion={seleccion}")

        match tecla:

            case readchar.key.UP:
                seleccion = (seleccion - 1) % len(opciones)

            case readchar.key.DOWN:
                seleccion = (seleccion + 1) % len(opciones)

            case readchar.key.LEFT:
                log("retorno: back (LEFT)")
                return "back"

            case readchar.key.RIGHT | readchar.key.ENTER:
                log(f"retorno: {seleccion}")
                return seleccion

            case readchar.key.ESC:
                log("retorno: back (ESC)")
                return "back"
