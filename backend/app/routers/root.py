from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    tags=['Root'],
    redirect_slashes=False
)
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


@router.get('/')
async def root():
    return {"success": 200}
