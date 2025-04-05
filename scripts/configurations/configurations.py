from configparser import ConfigParser
from scripts.constants.constants import conf_file

parser = ConfigParser()
parser.read([conf_file])


class Service:
    host = parser.get("SERVICES","host")
    port = int(parser.get("SERVICES","port"))

class Database:
    host = parser.get("SQL_DATABASE", "host")
    port = int(parser.get("SQL_DATABASE", "port"))
    username = parser.get("SQL_DATABASE", "username")
    password = parser.get("SQL_DATABASE", "password")
    database_name = parser.get("SQL_DATABASE", "database_name")
