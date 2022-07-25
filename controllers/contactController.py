from flask import session
from db import conectar
from helpers import Serializer
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
            contacts =session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
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

    # Serializo la respuesta con el método estático de la clase Serialize
    # para que se pueda convertir a JSON sin problemas
    contacts = Serializer.serialize_list(contacts)

    return contacts


def selectContact(id):
    # Retorna la info del contacto al que corresponda la id
    try:
        # Me conecto a la DB
        session = conectar()

        # Ahora armo la consulta del contacto
        my_contact = session.query(Contacto).filter(Contacto.id == id).all()

        # Valido que haya encontrado al contacto revisando la cantidad de
        # elementos del list devuelto
        if len(my_contact) > 0:
            # Facilito y evito errores en la conversión a JSON
            return Serializer.serialize_list(my_contact)
        else:
            return {"error": "No se encontró ningún contacto con esa id."}
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        session.close()


def searchContact(id_usuario, texto):
    # Retorna los resultados de búsqueda por el texto dado de los 
    # contactos de un usuario
    
    try:
        # Me conecto a la DB
        session = conectar()

        # Ahora armo la consulta de los contactos
        contacts = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto)\
            .filter(Pertenece.id_usuario == id_usuario)\
            .filter((Contacto.nombre.ilike(f"%{texto}%")) | (Contacto.apellidos.ilike(f"%{texto}%")) |\
                (Contacto.direccion.ilike(f"%{texto}%")) | (Contacto.email.ilike(f"%{texto}%")))\
            .order_by(Contacto.nombre).all()
    except Exception as e:
        print(f"Error: {e}")
        return {"Error": "Error al consultar datos de la DB." }
    finally:
        session.close()
    
    # Reviso los resultados del query
    if len(contacts) > 0:
        # Encontró contactos y los serializo
        return Serializer.serialize_list(contacts)
    else:
        # No encontró contactos, se devuelve diccionario vacío
        return {}


