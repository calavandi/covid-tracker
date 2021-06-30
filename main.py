from flask import Flask, request
import sqlite3
from models import Users

app = Flask(__name__)

@app.route("/")
def home():
    return "Covid tracker APP"

@app.route("/api/registerUser", methods=["POST"])
def register_user():
    user = Users()
    user_details = request.get_json()
    user.register_user(user_details['pinCode'], user_details['name'], user_details['phoneNumber'], "user")
    return request.get_json()

@app.route("/api/registerAdmin", methods=["POST"])
def register_admin():
    user = Users()
    user_details = request.get_json()
    user.register_user(user_details['pinCode'], user_details['name'], user_details['phoneNumber'], "admin")
    return request.get_json()
    

if __name__ == "__main__":
    app.run(debug=True, port=8080)