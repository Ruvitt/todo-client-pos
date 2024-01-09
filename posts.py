import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, BooleanField, SelectField

class Posts:
    base_url = "http://127.0.0.1:8000/posts/"

    class PostForm(FlaskForm):
        user = StringField('Usuario')
        title = StringField('Titulo')
        body = StringField('Descricao')
        submit = SubmitField('Enviar')

    def listPosts(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def getPost (self, post_id):
        url = self.base_url + str(post_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def createPost (self, post_data):
        url = self.base_url
        response = requests.post(url, json = post_data)

        if response.status_code != 201:
            print(f"Failed to create post: {response.content}")
        else:
            print(f"Post created: {response.json()}")

    def updatePost (self, post_id, post_data):
        url = self.base_url + str(post_id) + "/"
        response = requests.put(url, data = post_data)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        
    def deletePost (self, post_id):
        url = self.base_url + str(post_id)
        response = requests.delete(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        