import duckdb as db
import pandas as pd


def sql_reader(query: str):
    return db.sql(query).df()
