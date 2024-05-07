from fastapi import APIRouter

router = APIRouter()

@router.get("/artifacts/", tags=["artifacts"])
async def read_artifacts():
    return [ {"type": "Vase"}, {"type": "Gem"}]
