from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from helpers import Serializer

# Clase Base de la que heredarán todas las clases que van a mapear de la DB
Base = declarative_base()

# Adicionalemnte, cada clase que representa mis tablas en la DB heredará
# también de la clase Serializer de mi helper para facilitar la conversión
# de la respuesta a formato JSON

@dataclass
class Usuario(Base, Serializer):
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


class Pertenece(Base, Serializer):
    id: int
    id_usuario: int
    id_contacto: int

    # Estrucutra de la tabla con la que voy a mapear
    __tablename__ = "pertenece"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    id_contacto = Column(Integer, nullable=False)
    