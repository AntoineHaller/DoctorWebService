from fastapi import APIRouter
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet

my_key = Fernet.generate_key()
f = Fernet(my_key)
router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)

@router.get("",description="Get health")
def get_health():
    return {"API STATUS":"OK"}