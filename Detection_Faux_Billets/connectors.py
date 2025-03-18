import pandas as pd 
import duck_db as db 

def sql_reader(query:str):
  return db.sql(query).df()

