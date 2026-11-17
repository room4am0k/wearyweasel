
import argparse

import utils
import dbhandler
from forms import formulario_login
from menu import menu
from utils import log


def parse_args():
    p = argparse.ArgumentParser(description="weazel")
    p.add_argument("-d", "--debug", action="store_true",
                   help="imprime teclas y estado a stderr")
    p.add_argument("--no-clear", action="store_true",
                   help="no limpia la pantalla entre redibujados")
    return p.parse_args()


def main():
    resultado = menu(
        "weazel",
        ["Iniciar sesión en base de datos"]
    )
    log(f"resultado={resultado!r}")

    match resultado:

        case 0:
            datos = formulario_login()
            conn = dbhandler.incoming(datos)  # None si no se pudo conectar
            log(f"conn={'abierta' if conn else 'None'}")


        case "back":
            log("salió sin elegir")


if __name__ == "__main__":
    args = parse_args()
    utils.DEBUG = args.debug
    utils.NO_CLEAR = args.no_clear
    main()
