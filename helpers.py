from sqlalchemy.inspection import inspect


class Serializer(object):
    def serialize(self):
        # Retorno con dict aprehension todos los items de la lista
        # en formato diccionario {clave: valor}
        return {
            c: getattr(self, c) for c in inspect(self).attrs.keys()
        }

    @staticmethod
    def serialize_list(list):
        return [item.serialize() for item in list]
