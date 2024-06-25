from decouple import config
from sqlalchemy import create_engine, text
from clickhouse_sqlalchemy import make_session


class ClickhouseHandler:
    def __init__(self):
        url = f"clickhouse://{config('CLICKHOUSE_USER')}:{config('CLICKHOUSE_PASSWORD')}@{config('CLICKHOUSE_HOST')}/" \
              f"{config('CLICKHOUSE_DB')}"

        self.engine = create_engine(url)
        self.session = None

    def __enter__(self):
        self.session = make_session(self.engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def ping(self):
        return self.session.execute(text("select 'pong';")).all()

    def execute_sql(self, sql: text):
        return self.session.execute(sql).all()
