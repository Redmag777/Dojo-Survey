from dojo_survey.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_last_survey(cls):
        query = 'SELECT * FROM dojo ORDER BY dojo.id DESC LIMIT 1;'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojo (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);'
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True 
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("Favorite language must be chosen.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("Location must be chosen.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comment must be at least 3 characters.")
        return is_valid