"""Formularios de entrada de texto."""

import getpass

from utils import limpiar, log

MOTORES = {
    "mysql": "mysql",
    "mariadb": "mysql",
    "postgres": "postgres",
    "postgresql": "postgres",
    "pg": "postgres",
}

PUERTOS = {"mysql": 3306, "postgres": 5432}


def pedir(etiqueta, secreto=False, obligatorio=True):
    while True:
        if secreto:
            valor = getpass.getpass(f"{etiqueta}: ")  # no se muestra al escribir
        else:
            valor = input(f"{etiqueta}: ").strip()

        if valor or not obligatorio:
            return valor
        print("  Este campo no puede estar vacío.")


def pedir_motor():
    while True:
        valor = input("motor de base de datos [mysql/postgres]: ").strip().lower()
        if valor in MOTORES:
            return MOTORES[valor]
        print("  Motor no reconocido. Usa mysql o postgres.")


def pedir_puerto(defecto):
    while True:
        valor = input(f"port [{defecto}]: ").strip()
        if not valor:
            return str(defecto)
        if valor.isdigit() and 1 <= int(valor) <= 65535:
            return valor
        print("  El puerto debe ser un número entre 1 y 65535.")


def formulario_login():
    limpiar()
    print("=== Iniciar sesión en base de datos ===\n")

    dbtype = pedir_motor()
    datos = {
        "dbtype": dbtype,
        "host": pedir("host"),
        "name": pedir("name"),
        "port": pedir_puerto(PUERTOS[dbtype]),
        "password": pedir("password", secreto=True, obligatorio=False),
        "db": pedir("db"),
    }

    # Nunca se loguea la contraseña
    log(f"login capturado: motor={datos['dbtype']} host={datos['host']} "
        f"port={datos['port']} name={datos['name']} db={datos['db']}")
    return datos
