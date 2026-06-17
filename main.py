from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as prestamos_router

app = FastAPI(
    title="QCAZE - Sistema de Préstamos API",
    description="API para la gestión de préstamos de clientes usando FastAPI y Supabase.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prestamos_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de QCAZE - Sistema de Préstamos"}
