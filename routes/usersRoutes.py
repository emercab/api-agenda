from flask import Flask, jsonify, request
from flask import Blueprint
from controllers.userController import selectUser


users_api = Blueprint("users_api", __name__)


@users_api.route("/users", methods=["GET"])
def getUsers():
    # Recojo los parámetros que recibe este endpoint
    params = request.args
    email = params["email"]
    password = params["password"]
    # Llamo al controlador para que busque al usuario y devuleva la respuesta
    result = selectUser(email, password)
    return jsonify({
        "result": result,
    })
