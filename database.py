from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
URL_DATABASE="mysql+pymysql://root:Camacho19970+1@localhost:3306/datosBoyaca"
engine=create_engine(URL_DATABASE,pool_timeout=60)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base =declarative_base()