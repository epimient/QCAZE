# 愛 QCAZE - Sistema de Gestión de Préstamos (API REST)

Sistema backend desarrollado en Python (FastAPI) y Supabase para la gestión de préstamos. 
El proyecto fue refactorizado recientemente desde una interfaz gráfica local con Tkinter hacia un entorno de API REST moderna y escalable.

## Descripción

QCAZE es un sistema desarrollado en Python para la gestión de préstamos personales. La API permite registrar clientes, calcular automáticamente el interés quincenal, almacenar la información en una base de datos Supabase y administrar el estado de cada préstamo de manera programática.

Este proyecto fue desarrollado como una solución para agilizar el control de préstamos realizados manualmente, reduciendo errores y mejorando la organización de la información.

---

## 經 Tecnologías Utilizadas

### Lenguaje de Programación
* Python 3.12

### Base de Datos
* Supabase
* PostgreSQL

### Framework Backend
* **FastAPI**: Framework web moderno y de alto rendimiento.
* **Uvicorn**: Servidor ASGI para poner en marcha la aplicación.
* **Pydantic**: Para la validación de esquemas de datos.

### Entorno y Dependencias
* **Python-dotenv / Pydantic-settings**: Manejo seguro de credenciales con `.env`.

---

## 🚀 Instalación y Uso

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd QCAZE
```

2. Crear y activar el entorno virtual local:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar las dependencias listadas:
```bash
pip install -r requirements.txt
```

4. Configurar las credenciales. Renombra o crea un archivo `.env` en la raíz con tus variables de Supabase:
```env
SUPABASE_URL=tu_url_escondida
SUPABASE_KEY=tu_apikey_escondida
```

5. Iniciar la aplicación:
```bash
uvicorn main:app --reload
```

Una vez que el servidor se encuentre ejecutándose, dirígete a `http://localhost:8000/docs` para visualizar la documentación interactiva SwaggerUI generada por FastAPI y probar cada funcionalidad fácilmente.

---

## 經 Estructura del Proyecto

```text
📁QCAZE/
│
├── main.py           # Entrada principal de la API FastAPI y configuración de CORS
├── routes.py         # Endpoints de la API (POST, GET, PATCH, DELETE)
├── schemas.py        # Modelos Pydantic para la validación de Requests y Responses
├── conexion.py       # Interfaz con la base de datos Supabase
├── config.py         # Configuración y Settings para llamar las credenciales del .env
├── .env              # Variables de entorno ignoradas en git
├── .gitignore        # Ignora archivos basura y credenciales para el repositorio
├── requirements.txt  # Lista de librerías utilizadas
└── README.md
```

---

## Funcionalidades Implementadas

### Registrar Préstamo (`POST /prestamos`)
Permite ingresar:
* Nombre del cliente.
* Monto prestado.

El sistema calcula automáticamente:
* Interés quincenal del 5%.
* Total a pagar.

### Visualizar Préstamos (`GET /prestamos`)
Muestra un arreglo JSON con todos los préstamos documentados en Supabase.

### Eliminar Préstamo (`DELETE /prestamos/{id}`)
Permite eliminar el registro especificado.

### Marcar como Pagado (`PATCH /prestamos/{id}/pagar`)
Permite cambiar el estado de un préstamo de "Activo" a "Pagado".

---

## Fórmula Utilizada

Interés quincenal:
**Interés = Monto × 5%**

Ejemplo:
* Monto: $100.000
* Interés: $5.000
* Total a pagar: $105.000

---

## Posibles Mejoras Futuras

* Configurar porcentaje de interés dinámico en el body.
* Aplicar mora automática.
* Integración con un frontend (React / Next.js) para consumir esta API.
* Historial de pagos.
* Autenticación con tokens JWT.
* Dashboard estadístico de los préstamos.

---

## Autor

Proyecto desarrollado por Rodolfo Manga y Justin Myrs.  
Año: 2026.
