from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.database import meta, engine

patients = Table(
    "patient",
    meta,
    Column("id", Integer, primary_key=True),
    Column("id_doctor", Text),
    Column("id_patient", Text),
)

meta.create_all(engine)