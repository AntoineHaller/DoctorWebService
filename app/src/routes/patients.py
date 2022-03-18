from fastapi import APIRouter, Depends
from config.db import conn
from src.models.patients import patients
from src.schemas.patients import Patient
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet

router = APIRouter(
    prefix="/patients",
    tags=["patients"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)


@router.get(
    "/{id}",
    response_model=Patient,
    description="Get one patients with Id",
)
def get_patient(id: str):
    return conn.execute(patients.select().where(patients.c.id == id)).first()

@router.get(
    "",
    response_model=List[Patient],
    description="Get all patients",
)
def get_patients():
    return conn.execute(patients.select()).fetchall()


@router.post(
    "",
    response_model=Patient, 
    description="Create patient")
def create_patient(patient: Patient):
    new_patient = {"id_doctor": patient.id_doctor, "id_patient": patient.id_patient}
    result = conn.execute(patients.insert().values(new_patient))
    return conn.execute(patients.select().where(patients.c.id == result.lastrowid)).first()


@router.delete(
    "/{id}",
    status_code=HTTP_204_NO_CONTENT
)
def delete_patient(id: int):
    conn.execute(patients.delete().where(patients.c.id == id))
    return conn.execute(patients.select().where(patients.c.id == id)).first()
