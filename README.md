# wearyWeazel

Interfaz simple, CLI primero, para leer datos de bases SQL (PostgreSQL y MySQL/MariaDB).

> **Estado: desarrollo temprano.** Hoy solo hace el inicio de sesión: pide los datos, se conecta a la base y termina. La lectura de datos viene después.

## Qué hace hoy

- Menú en terminal navegable con flechas.
- Formulario de inicio de sesión: motor, host, usuario, puerto, contraseña y base de datos.
- Conexión a **PostgreSQL** y **MySQL/MariaDB**.
- Mensajes de error claros si algo falla (clave incorrecta, servidor caído, driver sin instalar). Espera máximo 10 segundos al conectar.

## Qué no hace (todavía)

- No muestra ni consulta datos.
- No guarda historial de conexiones.


## Requisitos

- Python 3.10 o superior
- Una base PostgreSQL o MySQL/MariaDB a la que tengas acceso

## Instalación

```bash
git clone <URL-DEL-REPO>
cd <carpeta-del-repo>
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

| Tecla | Acción |
|---|---|
| Flecha arriba / abajo | Moverse |
| Enter / flecha derecha | Elegir |
| Flecha izquierda / Esc | Volver o salir |

Al iniciar sesión te pregunta:

| Campo | Qué poner |
|---|---|
| motor | `mysql` o `postgres` (también acepta `mariadb`, `postgresql`, `pg`) |
| host | Dirección del servidor, por ejemplo `localhost` |
| name | Tu **usuario** de la base de datos |
| port | Enter para el puerto por defecto (postgres: 5432, mysql: 3306) |
| password | Tu contraseña (no se muestra al escribir) |
| db | Nombre de la base de datos |

### Depuración

```bash
python main.py --debug              # imprime teclas y estado en stderr
python main.py --debug --no-clear   # además, no limpia la pantalla
python main.py -d 2> debug.log      # manda el debug a un archivo
```

El modo debug nunca imprime la contraseña.

## Estructura

```
main.py            Entrada y flujo principal
menu.py            Menú con flechas
forms.py           Formularios y validación de datos
utils.py           Flags, log de depuración y limpieza de pantalla
db/dbhandler.py    Conexión a PostgreSQL y MySQL/MariaDB
requirements.txt   Dependencias
```

## Licencia

[GNU AGPL-3.0](LICENSE)
