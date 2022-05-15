from fastapi import APIRouter


router = APIRouter(
    tags=['Root'],
    redirect_slashes=False
)


@router.get('/')
async def root():
    return {"success": 200}
