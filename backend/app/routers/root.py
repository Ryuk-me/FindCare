from fastapi import APIRouter


router = APIRouter(
    tags=['Root']
)


@router.get('/')
async def root():
    return {"success": 200}
