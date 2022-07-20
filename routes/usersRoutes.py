from flask import Flask, jsonify, request
from flask import Blueprint


users_api = Blueprint("users_api", __name__)


@users_api.route("/users", methods=["GET"])
def prueba2():
    return "Users"
