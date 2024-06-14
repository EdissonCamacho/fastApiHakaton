from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class modelData(BaseModel):
    id:int
    codigo:int
    departamento:str
    codigoEntidad:str
    entidad:str
    dimension:str
    subcategoria:str
    indicador:str
    datoNumerico:float
    ano:int
    mes:int
    fuente:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close

db_dependency=Annotated[Session,Depends(get_db)]

@app.get("/getAll",status_code=status.HTTP_200_OK)
async def getAll(db:db_dependency):
    registros=db.query(models.TablaData).all()
    return registros

@app.get("/getByIndicador", status_code=status.HTTP_200_OK)
async def get_by_indicador(indicadorName: str, db: db_dependency):
    registros = db.query(models.TablaData).filter(models.TablaData.indicador == indicadorName).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given indicator")
    return registros
@app.get("/getByEntidad", status_code=status.HTTP_200_OK)
async def get_by_entidad(entidadName: str, db: db_dependency):
    registros = db.query(models.TablaData).filter(models.TablaData.entidad == entidadName).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given entity")
    return registros
@app.get("/getByAno", status_code=status.HTTP_200_OK)
async def get_by_ano(ano: int, db: db_dependency):
    registros = db.query(models.TablaData).filter(models.TablaData.ano == ano).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given year")
    return registros

@app.get("/getTopByIndicador", status_code=status.HTTP_200_OK)
async def get_top_by_indicador(indicadorName: str, db: db_dependency):
    registros = db.query(models.TablaData).filter(models.TablaData.indicador == indicadorName).order_by(models.TablaData.datoNumerico.desc()).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given indicator")
    return registros

@app.get("/getByEntidadIndicador", status_code=status.HTTP_200_OK)
async def get_by_entidad_indicador(entidadName: str, indicadorName: str, db: db_dependency):
    registros = db.query(models.TablaData).filter(
        models.TablaData.entidad == entidadName,
        models.TablaData.indicador == indicadorName
    ).order_by(models.TablaData.datoNumerico.desc()).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given entity and indicator")
    return registros

@app.get("/getTopByIndicadorAno", status_code=status.HTTP_200_OK)
async def get_top_by_indicador_ano(indicadorName: str, ano: int, db: db_dependency):
    registros = db.query(models.TablaData).filter(
        models.TablaData.indicador == indicadorName,
        models.TablaData.ano == ano
    ).order_by(models.TablaData.datoNumerico.desc()).all()
    if not registros:
        raise HTTPException(status_code=404, detail=f"No records found for the indicator '{indicadorName}' and year '{ano}'")
    return registros

#Hoteles

@app.get("/getAllHoteles",status_code=status.HTTP_200_OK)
async def getAll(db:db_dependency):
    registros=db.query(models.hoteles).all()
    return registros
@app.get("/getHotelesIn", status_code=status.HTTP_200_OK)
async def get_top_by_indicador(municipio: str, db: db_dependency):
    registros = db.query(models.hoteles).filter(models.hoteles.Municipio==municipio,models.hoteles.Subcategoria=="HOTEL").order_by(models.hoteles.Habitaciones.desc()).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given indicator")
    return registros

@app.get("/getAgenciasIn", status_code=status.HTTP_200_OK)
async def get_top_by_indicador(municipio: str, db: db_dependency):
    registros = db.query(models.hoteles).filter(models.hoteles.Municipio==municipio,models.hoteles.Subcategoria=="AGENCIA DE VIAJES Y DE TURISMO").order_by(models.hoteles.Habitaciones.desc()).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No records found for the given indicator")
    return registros

#Municipios

@app.get("/getAllMunicipios",status_code=status.HTTP_200_OK)
async def getAll(db:db_dependency):
    registros=db.query(models.municipios).order_by(models.municipios.entidad.asc()).all()
    return registros
