from flask import Flask
from routes.usersRoutes import users_api
from routes.contactsRoutes import contacts_api


app = Flask(__name__)

# Vínculo al route de los endpoints de /users
app.register_blueprint(users_api)

# Vínculo al route de los endpoints de /contacts
app.register_blueprint(contacts_api)


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
