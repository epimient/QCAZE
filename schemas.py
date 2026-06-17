from pydantic import BaseModel

class PrestamoCreate(BaseModel):
    nombre_cliente: str
    monto: int

class PrestamoResponse(BaseModel):
    id: int
    nombre_cliente: str
    monto: int
    interes: int
    total_pagar: int
    fecha_prestamo: str
    estado: str
