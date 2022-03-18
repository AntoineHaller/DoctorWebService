from sqlalchemy import create_engine, MetaData
import os
DB_URI = "mysql+pymysql://user:password@localhost:3306/db"
engine = create_engine(DB_URI)

meta = MetaData()
conn = engine.connect()