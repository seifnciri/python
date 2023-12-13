from mysqlconnection import connectToMySQL
class USER:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def creat(cls, data):
        query ="""
        INSERT INTO users( first_name , last_name , email ) 
        VALUES ( %(first_name)s , %(last_name)s , %(email)s);"""
        return connectToMySQL('users_schema').query_db( query, data )
    @classmethod
    def show_users(cls):
        query="""
        SELECT * FROM users_schema.users;
        """
        raw_user=connectToMySQL('users_schema').query_db( query)
        u=[]
        for x in raw_user:
            u.append(cls(x))
        print(raw_user)
        return u
    @classmethod
    def show_one(cls, data):

        query = """
                    SELECT * FROM users_schema.users
                    WHERE id = %(id)s;
                """
        results = connectToMySQL("users_schema").query_db(query, data)
        # print(results)
        this_hero = cls(results[0])

        return this_hero