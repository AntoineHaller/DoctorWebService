from fastapi import FastAPI
from src.routes.doctors import router as doctor
from src.routes.patients import router as patient
from src.routes.health import router as health
from config.openapi import tags_metadata
import os

app = FastAPI(
    title="Web Service",
    description="doctor web api",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(doctor)
app.include_router(patient)
app.include_router(health)
