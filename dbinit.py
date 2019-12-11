import sys

import psycopg2 as dbapi2
from configs import db_url


def read_sql_from_file(filename: str) -> list:
    with open(filename, 'r') as f:
        content = f.read()
        content = content.split(';')
        content = [row + ";" for row in content]
    return content


def initialize():
    try:
        with dbapi2.connect(db_url) as connection:
            with connection.cursor() as cursor:
                print("Connected...", file=sys.stderr)

                drop_statements = read_sql_from_file('drop.sql')
                for statement in drop_statements:
                    if len(statement) > 5:
                        cursor.execute(statement)
                print("Drop tables...", file=sys.stderr)

                create_statements = read_sql_from_file('data_base.sql')
                for statement in create_statements:
                    if len(statement) > 5:
                        cursor.execute(statement)
                print("Create tables...", file=sys.stderr)


    except (Exception, dbapi2.Error) as error:
        print("Error while connecting to PostgreSQL: {}".format(error), file=sys.stderr)


if __name__ == "__main__":
    initialize()
