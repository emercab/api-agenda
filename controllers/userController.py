from db import conectar
from models import Usuario


def selectUser(email, password):
    # Busca en base de datos un usuario con email y password que se le envía
    # En caso de encontrarlo, retorna su id, de no encontrarlo, retorna cero.
    id = 0
    try:
        session = conectar()
        # Hago la consulta a la DB con sqlalchemy
        user = session.query(Usuario).filter(Usuario.email == email, Usuario.password == password).all()
        if len(user):
            id = user[0].id;
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
    
    return id
