from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

doctors = Table(
    "doctor",
    meta,
    Column("id", Integer, primary_key=True),
    Column("doctor_name", String(45)),
    Column("doctor_city", Text),
    Column("doctor_speciality", Text),
)

meta.create_all(engine)