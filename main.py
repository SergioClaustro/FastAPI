from fastapi import FastAPI
from typing import Optional

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el endpoint con un parámetro de consulta opcional
@app.get("/nombres")
async def obtener_nombres(filtro: Optional[str] = None):
    nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
    
    # Si se proporciona un filtro, solo devuelve los nombres que lo contengan
    if filtro:
        nombres = [nombre for nombre in nombres if filtro.lower() in nombre.lower()]
    
    return {"nombres": nombres}

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
