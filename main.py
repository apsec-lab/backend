from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import router as users_router
from products import router as products_router

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.include_router(users_router.router)
app.include_router(products_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)