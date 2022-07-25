from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from helpers import Serializer

# Clase Base de la que heredarán todas las clases que van a mapear de la DB
Base = declarative_base()


@dataclass
class Usuario(Base):
    id: int
    nombre: str
    apellidos: str
    email: str
    password: str

    # Estrucutra de la tabla con la que voy a mapear
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return \
            f"id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, "\
            f"email={self.email}, password={self.password}"


class Contacto(Base, Serializer):
    # Uso la clase Serializer de mi helper para facilitar la creación
    # de la respuesta de consultas en formato JSON
    id: int
    nombre: str
    apellidos: str
    direccion: str
    email: str
    telefono: str
    fechaCreacion: datetime

    # Estrucutra de la tabla con la que voy a mapear
    __tablename__ = "contacto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String)
    direccion = Column(String)
    email = Column(String)
    telefono = Column(String)
    fechaCreacion = Column(DateTime, default=datetime.today())


    def __repr__(self):
        return \
            f"Contacto(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, "\
            f"direccion={self.direccion}, email={self.email}, telefono={self.telefono}, "\
            f"fechaCreacion={self.fechaCreacion})"


class Pertenece(Base):
    id: int
    id_usuario: int
    id_contacto: int

    # Estrucutra de la tabla con la que voy a mapear
    __tablename__ = "pertenece"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_contacto = Column(Integer, nullable=False)
    