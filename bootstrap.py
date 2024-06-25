from os import system, path
from db.db import ClickhouseHandler

from sqlalchemy import text


def read_script(filepath: str) -> text:
    """get sql from file"""
    try:
        f = open(file=filepath, mode="r")

        return text(f.read())
    except Exception as e:
        return text(f"select {str(e)}")


if __name__ == "__main__":
    db = ClickhouseHandler()

    with db as session:
        create_table = session.execute_sql(sql=read_script(filepath="scripts/sql/create_table_uk_paid.sql"))