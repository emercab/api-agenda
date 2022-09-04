from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URI = 'postgresql://root_agenda:clave123@localhost:5432/db_agenda'
DATABASE_URI = 'postgresql://hhnwjsboimbvlc:fd239bec602218aa520022f327f2e496970022cbfb21ee9aa843c439358f3dad@ec2-44-207-126-176.compute-1.amazonaws.com:5432/d8ss09popabq8e'

def conectar():
    # Conecto a la DB
    engine = create_engine(DATABASE_URI)
    
    # Creo un pull de conexiones a partir del engine
    Session = sessionmaker(bind=engine)
    
    # Creo una sesión concreta
    s = Session()

    if s != None:
        print("DB connection successful.")
    else:
        print("Error to connect to DB.")

    return s
