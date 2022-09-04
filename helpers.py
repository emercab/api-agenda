from sqlalchemy.inspection import inspect


class Serializer(object):
    # Esta clase convertirá la lista de objetos devuelto en la query de sqlalchemy
    # a un diccionario que facilitará la conversión a formato JSON
    
    def serialize(self):
        # Retorno con dict aprehension todos los items de la lista
        # en formato diccionario {clave: valor}
        return {
            c: getattr(self, c) for c in inspect(self).attrs.keys()
        }

    @staticmethod
    def serialize_list(list):
        return [item.serialize() for item in list]
