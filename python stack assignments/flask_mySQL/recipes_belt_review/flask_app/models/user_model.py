from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    # CONSTRUCTOR - Make Defaults
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

     # ========== CREATE USER ============
    @classmethod
    def create(cls, data):

        query = """ 
                    INSERT INTO users (first_name,  last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """

        return connectToMySQL(DB_NAME).query_db(query, data)

        # ========= GET USER BY ID ============
    @classmethod
    def get_by_id(cls, data):

        query = """ 
                    SELECT * FROM users
                    Where id = %(id)s;
                """

        results = connectToMySQL(DB_NAME).query_db(query, data)

        if len(results) < 1:
            return []
        return cls(results[0])

    @classmethod
    def get_by_email(cls, data):

        query = """ 
                    SELECT * FROM users
                    Where email = %(email)s;
                """

        results = connectToMySQL(DB_NAME).query_db(query, data)

        if len(results) < 1:
            return []
        return cls(results[0])

    # * =============== VALIDATIONS ================

    @staticmethod
    def validate(data):
        is_valid = True  # we assume this is true
        # Check the first name
        if len(data['first_name']) < 1:
            flash("First Name is Required !", "reg")
            is_valid = False
        # Check the last name
        if len(data['last_name']) < 1:
            flash("Last Name is Required !", "reg")
            is_valid = False
        # Check the email
        if len(data["email"]) < 1:
            is_valid = False
            flash("Email is Required !", "reg")
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!", "reg")
            is_valid = False
        # Check if the email already exists
        else:
            email_dict = {
                'email': data['email']
            }
            potential_user = User.get_by_email(email_dict)
            if potential_user:  # ! email is not unique
                is_valid = False
                flash("Email is already taken, hopefully by you !", "reg")

        if len(data["password"]) < 1:
            is_valid = False
            flash("Password is required !", "reg")
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("Passwords don't match !", "reg")

        return is_valid