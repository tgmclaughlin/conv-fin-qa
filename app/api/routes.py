import logging

from fastapi import APIRouter, HTTPException

from app.service.data_service import get_json_by_id, find_all_ids

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/data")
async def get_data(option: str):
    result = get_json_by_id(option)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.get("/all_ids")
async def get_all_ids():
    return find_all_ids()
