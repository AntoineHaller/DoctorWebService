
from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    id: Optional[int]
    id_doctor: str
    id_patient: str