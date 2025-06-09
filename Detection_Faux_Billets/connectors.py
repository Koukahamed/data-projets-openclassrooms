import duckdb as db


def sql_reader(query: str):
    return db.sql(query).df()
