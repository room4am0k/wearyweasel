"""Conexión a bases de datos (PostgreSQL y MySQL/MariaDB)."""

from utils import log

TIMEOUT = 10  


def pg_conn(data):
    import psycopg
    return psycopg.connect(
        host=data["host"],
        port=int(data["port"]),
        dbname=data["db"],
        user=data["name"],
        password=data["password"],
        connect_timeout=TIMEOUT,
    )


def my_conn(data):
    import pymysql
    return pymysql.connect(
        host=data["host"],
        port=int(data["port"]),
        database=data["db"],
        user=data["name"],
        password=data["password"],
        connect_timeout=TIMEOUT,
    )


def incoming(data):
    try:
        match data["dbtype"]:
            case "mysql":
                conn = my_conn(data)
            case "postgres":
                conn = pg_conn(data)
            case _:
                print(f"Motor no soportado: {data['dbtype']!r}")
                return None
    except ImportError as e:
        print(f"Falta el driver ({e.name}). Instálalo con: pip install -r requirements.txt")
        return None
    except Exception as e:
        print(f"No se pudo conectar: {e}")
        log(f"error de conexión: {type(e).__name__}")
        return None

    print("Conexión exitosa.")
    log(f"conectado: motor={data['dbtype']} host={data['host']} db={data['db']}")
    return conn
