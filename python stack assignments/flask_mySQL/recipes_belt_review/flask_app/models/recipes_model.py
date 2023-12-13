from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask_app.models import user_model
from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.Date_Cooked = data["Date_Cooked"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def create_recipy(cls, data):
        
        query = """
                    INSERT INTO recipes (name, description,instruction,Date_Cooked,under_30,user_id)
                    VALUES (%(name)s,%(description)s,%(instruction)s,%(Date_Cooked)s,%(under_30)s,%(user_id)s);
                """
        

        results = connectToMySQL(DB_NAME).query_db(query, data)
        return results
    @classmethod
    def get_all(cls):

        query = """
                        SELECT * FROM recipes
                        JOIN users
                        ON recipes.user_id = users.id ;
                """
        results = connectToMySQL(DB_NAME).query_db(query)

        all_recipes = []

        for row in results:
            this_recipe = cls(row)
            # fix up the hero ambiguity for the hero
            # prepare the data for the contructor

            user_data = {
                **row,
                "id": row["users.id"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }

            this_user = user_model.User(user_data)
            this_recipe.user = this_user
            all_recipes.append(this_recipe)

        return all_recipes
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM recipes WHERE id = %(id)s;
        """
        result = connectToMySQL(DB_NAME).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from recipes where id=%(id)s;
        """
        return connectToMySQL(DB_NAME).query_db(query,data)

    @classmethod
    def edit_recipe(cls, data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instruction= %(instruction)s , Date_Cooked = %(Date_Cooked)s, under_30= %(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DB_NAME).query_db(query, data)