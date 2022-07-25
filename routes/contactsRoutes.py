from flask import jsonify, request
from flask import Blueprint
import controllers.contactController as contactsController


contacts_api = Blueprint("contacts_api", __name__)


@contacts_api.route("/contacts", methods=["GET"])
def getContacts():
    # Recojo los parámetros que recibe este endpoint
    params = request.args
    id_usario = params["id_usuario"]
    campo = params["campo"]
    orden = params["orden"]
    contacts = contactsController.selectContacts(id_usario, campo, orden)
    return jsonify(contacts)


@contacts_api.route("/contact", methods=["GET"])
def getContact():
    # Recojo los parámetros que recibe este endpoint
    params = request.args
    id = params["id"]
    contact = contactsController.selectContact(id)
    return jsonify(contact)


@contacts_api.route("/search_in_contacts", methods=["GET"])
def search_in_contacts():
    # Recojo los parámetros que recibe este endpoint
    params = request.args
    id_usuario = params["id_usuario"]
    texto = params["texto"]
    contacts = contactsController.searchContact(id_usuario, texto)
    return jsonify(contacts)
