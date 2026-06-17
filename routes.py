from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date
from conexion import supabase
from schemas import PrestamoCreate, PrestamoResponse

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=PrestamoResponse)
def registrar_prestamo(prestamo: PrestamoCreate):
    interes = prestamo.monto * 5 // 100
    total = prestamo.monto + interes

    response = supabase.table("Prestamos").insert({
        "nombre_cliente": prestamo.nombre_cliente,
        "monto": prestamo.monto,
        "interes": interes,
        "total_pagar": total,
        "fecha_prestamo": str(date.today()),
        "estado": "Activo"
    }).execute()

    if not response.data:
        raise HTTPException(status_code=400, detail="Error al registrar el préstamo")
    
    return response.data[0]

@router.get("/", response_model=List[PrestamoResponse])
def obtener_prestamos():
    response = supabase.table("Prestamos").select("*").execute()
    return response.data

@router.patch("/{id}/pagar", response_model=PrestamoResponse)
def marcar_pagado(id: int):
    response = supabase.table("Prestamos").update({
        "estado": "Pagado"
    }).eq("id", id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    
    return response.data[0]

@router.delete("/{id}")
def eliminar_prestamo(id: int):
    response = supabase.table("Prestamos").delete().eq("id", id).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado o ya eliminado")
    return {"detail": "Préstamo eliminado exitosamente"}
