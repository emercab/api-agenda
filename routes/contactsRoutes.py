from flask import Flask, jsonify, request
from flask import Blueprint
from controllers.contactController import selectContacts
from helpers import Serializer


contacts_api = Blueprint("contacts_api", __name__)


@contacts_api.route("/contacts", methods=["GET"])
def getContacts():
    # Recojo los parámetros que recibe este endpoint
    params = request.args
    id_usario = params["id_usuario"]
    campo = params["campo"]
    orden = params["orden"]
    contacts = selectContacts(id_usario, campo, orden)
    # Serializo la respuesta con el método estático de la clase Serialize
    # para que se pueda convertir a JSON sin problemas
    contacts = Serializer.serialize_list(contacts)
    return jsonify(contacts)
