import logging

from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health_check")
def health_check():
    return {"msg": "ok"}
