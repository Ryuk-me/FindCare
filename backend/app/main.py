from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Config import settings
from app.routers import root
from app.models import user_model, clinic_model, doctor_model, appointment_model
from app.database import engine
from app.routers.v1 import auth, user_router, doctor_router, clinic_router, appointment_router

user_model.Base.metadata.create_all(bind=engine)
clinic_model.Base.metadata.create_all(bind=engine)
doctor_model.Base.metadata.create_all(bind=engine)
appointment_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NextCare-API",
    version="1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "NextCare-API",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    # root_path=settings.BASE_API_V1
    # redoc_url=None,
    docs_url=settings.BASE_API_V1 + "/docs",
    openapi_url=settings.BASE_API_V1 + "/openapi.json",
)

# origins = ["http://localhost:3000",
#            'http://127.0.0.1:8009', 'http://127.0.0.1:8009/*']

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(user_router.router)
app.include_router(auth.router)
app.include_router(doctor_router.router)
app.include_router(clinic_router.router)
app.include_router(appointment_router.router)
