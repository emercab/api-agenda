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


def insertContact(id_usuario, nombre, apellidos, direccion, email, telefono):
    # Inserta un nuevo contacto en la DB con los valores que recibe, primero
    # lo inserta en la tabla contacto y luego en la tabla pertenece. Si tuvo
    # éxito retorna True, en caso contrario, False.
    
    try:
        # Creo un objeto de la clase Contacto que tendrá los datos del 
        # contacto y luego será mapeado con la tabla
        contact = Contacto(
            nombre = nombre,
            apellidos = apellidos,
            direccion = direccion,
            email = email,
            telefono= telefono,
        )
        
        # Me conecto a la DB
        session = conectar()

        # Inserto el objeto contacto a la tabla Contacto de la DB
        session.add(contact)

        # Necesario para que el cambio en la tabla se haga efectivo
        session.commit()

        # Necesario para realziar otra transacción en la DB cuando ya se
        # ha hecho una
        session.refresh(contact)

        # Ahora preparo los valores que se van a insertar en la tabla
        # pertenece: id_contacto e id_usuario
        # Primero, obtengo el id_contacto del registro que se acabó de
        # insertar
        id_contacto = contact.id

        # Ahora se crea un objeto de la clase Pertenece para insertarlo en DB
        pertenece = Pertenece(
            id_usuario = id_usuario, # Valor recibido como parámetro
            id_contacto = id_contacto,
        )

        # Lo inserto a la tabla
        session.add(pertenece)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        session.close()
    
    return True

