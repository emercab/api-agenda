from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://root_agenda:Paqcom04.@localhost:5432/db_agenda"

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
