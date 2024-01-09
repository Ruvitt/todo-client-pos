import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, BooleanField, SelectField

class Comments:
    base_url = "http://127.0.0.1:8000/comments/"

    class CommentForm(FlaskForm):
        post = StringField('Post')
        name = StringField('Nome')
        email = StringField('Email')
        body = StringField('Descricao')
        submit = SubmitField('Enviar')

    def listComments(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def getComment (self, comment_id):
        url = self.base_url + str(comment_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def createComment (self, comment_data):
        url = self.base_url
        response = requests.post(url, json = comment_data)

        if response.status_code != 201:
            print(f"Failed to create comment: {response.content}")
        else:
            print(f"Comment created: {response.json()}")

    def updateComment (self, comment_id, comment_data):
        url = self.base_url + str(comment_id) + "/"
        response = requests.put(url, data = comment_data)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        
    def deleteComment (self, comment_id):
        url = self.base_url + str(comment_id)
        response = requests.delete(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")