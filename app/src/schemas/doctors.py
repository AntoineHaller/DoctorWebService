
from typing import Optional
from pydantic import BaseModel

class Doctor(BaseModel):
    id: Optional[int]
    doctor_city: str
    doctor_name: str
    doctor_speciality: str