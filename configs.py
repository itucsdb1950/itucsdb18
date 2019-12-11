import os.path
import sys

DSN_kk = {'user': "postgres",  # DSN for Kutay Karakamış
          'password': "123",
          'host': "127.0.0.1",
          'port': "5432",
          'database': "scholar"
          }

DSN_efo = {'user': "postgres",  # DSN for Furkan Güvenç
           'password': "1234",
           'host': "127.0.0.1",
           'port': "5432",
           'database': "hebe2"
           }

DSN_mfy = {'user': "postgres",  # DSN for Mehmet Fatih Yıldırım
           'password': "1234",
           'host': "127.0.0.1",
           'port': "5432",
           'database': "hebe2"
           }


#  postgres//user:pw@host:port/database

def get_url(DSN):
    connection_url = "dbname={} user={} password={} host={} port={}".format(DSN['database'], DSN['user'],
                                                                            DSN['password'], DSN_kk['host'],
                                                                            DSN['port'])

    return connection_url


kk_connection_url = get_url(DSN_kk)
efo_connection_url = get_url(DSN_efo)
mfy_connection_url = get_url(DSN_mfy)

HOME_PATH = os.path.expanduser("~").lower()  # home url of pc
db_url = str()

try:
    if 'kutay' in HOME_PATH:  # Pc of Kutay Karakamış
        db_url = kk_connection_url
    elif 'someone' in HOME_PATH:  # Pc of Enes Furkan Örnek TODO: değiştir home path ine göre
        db_url = efo_connection_url
    elif 'fatih' in HOME_PATH:  # Heroku TODO: değiştir home path ine göre
        db_url = mfy_connection_url
    elif 'app' in HOME_PATH:  # Heroku
        db_url = os.getenv("DATABASE_URL")
except Exception as e:
    print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
    sys.exit(1)
