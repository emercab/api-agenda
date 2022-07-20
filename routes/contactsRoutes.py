from flask import Flask, jsonify, request
from flask import Blueprint


contacts_api = Blueprint("contacts_api", __name__)


@contacts_api.route("/contacts", methods=["GET"])
def prueba2():
    return "Contacts"
