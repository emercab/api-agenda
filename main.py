from crypt import methods
from flask import Flask, jsonify, request
from flask import Blueprint
from routes.usersRoutes import users_api
from routes.contactsRoutes import contacts_api


app = Flask(__name__)
app.register_blueprint(users_api)
app.register_blueprint(contacts_api)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
