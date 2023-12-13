from flask import Flask
app = Flask(__name__)
app.secret_key = "this a secret key !!!"
DB_NAME='users_schema'