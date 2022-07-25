from db import conectar
from models import Contacto, Pertenece


def selectContacts(id_usuario, campo, orden):
    # Selecciona todos los contactos del usuario con la id que recibe,
    # ordena los resultados por el campo que recibe con el sentido de
    # ordenamiento que recibe
    try:
        # Me conecto a la DB
        session = conectar()

        # Ahora armo las consultas dependiendo de los parámetros recibidos
        if campo == "ID" and orden == "ASC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all()
        elif campo == "NOMBRE" and orden == "ASC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()
        elif campo == "NOMBRE" and orden == "DESC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()
        elif campo == "APELLIDOS" and orden == "ASC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.apellidos).all()
        elif campo == "APELLIDOS" and orden == "DESC":
            contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.apellidos.desc()).all()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
    
    return contacts
