from os import getenv
from re import M

ENV = getenv("PY_ENV", "DEV")

BE_HOST = getenv("BE_HOST", "0.0.0.0")
BE_PORT = int(getenv("BE_PORT", 5000))
API_KEY = getenv("API_KEY","")

MYSQL_HOST = getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(getenv("MYSQL_PORT", 3306))
MYSQL_USER = getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD", "root")
MYSQL_DATABASE = getenv("MYSQL_DATABASE", "tunevibe")
                 