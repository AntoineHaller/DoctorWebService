from fastapi import APIRouter, Depends
from config.database import conn
from src.models.doctors import doctors
from src.schemas.doctors import Doctor
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)

@router.get(
    "/{id}",
    response_model=Doctor,
    description="Get one single doctor with the id",
)
def get_doctors(id: str):
    return conn.execute(doctors.select().where(doctors.c.id == id)).first()

@router.get(
    "",
    response_model=List[Doctor],
    description="Get all doctors",
)
def get_doctors():
    return conn.execute(doctors.select()).fetchall()



@router.get(
    "/{speciality}/{city}",
    response_model=List[Doctor],
    description="Get one single doctor with his speciality and city",
)
def get_doctors_by_speciality_and_id(speciality: str, city: str):
    return conn.execute(doctors.select().where(doctors.c.doctor_speciality == speciality).where(doctors.c.doctor_city == city)).fetchall()


@router.post(
    "",
    response_model=Doctor, 
    description="Create doctor")
def create_doctor(doctor: Doctor):
    new_doctor = {"name": doctor.doctor_name, "city": doctor.doctor_city, "speciality": doctor.doctor_speciality}
    result = conn.execute(doctors.insert().values(new_doctor))
    return conn.execute(doctors.select().where(doctors.c.id == result.lastrowid)).first()


@router.put(
    "/{id}",
    response_model=Doctor, 
    description="Update doctor with Id"
)
def update_doctor(doctor: Doctor, id: int):
    conn.execute(
        doctors.update()
        .values(id_doctor=doctor.id_doctor, url=doctor.url, order=doctor.order)
        .where(doctors.c.id == id)
    )
    return conn.execute(doctors.select().where(doctors.c.id == id)).first()


@router.delete(
    "/{id}",
    status_code=HTTP_204_NO_CONTENT
)
def delete_doctor(id: int):
    conn.execute(doctors.delete().where(doctors.c.id == id))
    return conn.execute(doctors.select().where(doctors.c.id == id)).first()
