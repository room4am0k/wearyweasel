"""Utilidades comunes: flags globales, log de depuración y terminal."""

import os
import sys

# Flags globales. Solo main.py los escribe (utils.DEBUG = ...).
DEBUG = False
NO_CLEAR = False


def log(*args):
    # Va a stderr para no mezclarse con el menú
    if DEBUG:
        print("[debug]", *args, file=sys.stderr)


def limpiar():
    if NO_CLEAR:
        log("limpiar() omitido (--no-clear)")
        return
    os.system("cls" if os.name == "nt" else "clear")
