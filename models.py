from sqlalchemy import String, Integer, Column,Float

from database import Base


class TablaData(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer)
    departamento = Column(String(255))
    codigoEntidad = Column(Integer)
    entidad = Column(String(255))
    dimension = Column(String(255))
    subcategoria = Column(String(255))
    indicador = Column(String(255))
    datoNumerico = Column(Float)
    ano = Column(Integer)
    mes = Column(String(255))
    fuente = Column(String(255))

class hoteles(Base):
    __tablename__="hoteles"
    id=Column(Integer,primary_key=True,index=True)
    Numero_del_RNT=Column(Integer)
    Estado=Column(String)
    Municipio=Column(String)
    Departamento=Column(String)
    Nombre_Comercial=Column(String)
    Categoria=(String)
    Subcategoria=Column(String)
    Direccion_Comercial=Column(String)
    Correo_Electronico=Column(String)
    Habitaciones=Column(Integer)
    Camas=Column(Integer)
    Empleados=Column(Integer)

class municipios(Base):
    __tablename__="municipios"
    id=Column(Integer,primary_key=True,index=True)
    entidad=Column(String)


