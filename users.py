import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField

class Users:

    base_url = "http://127.0.0.1:8000/users/"

    class UserForm(FlaskForm):
        name = StringField('Nome')
        username = StringField('Username')
        email = EmailField('Email')
        adress = StringField('Endereco')
        phone = StringField('Telefone')
        website = StringField('Website')
        company = StringField("Empresa")
        submit = SubmitField('Enviar')

    def listUsers(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def getUser(self, user_id):
        url = self.base_url + str(user_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def createUser (self, user_data):
        url = self.base_url
        response = requests.post(url, json = user_data)

        if response.status_code == 201:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        
    def updateUser (self, user_id, user_data):
        url = self.base_url + str(user_id) + "/"
        response = requests.put(url, data = user_data)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        
    def deleteUser (self, user_id):
        url = self.base_url + str(user_id)
        response = requests.delete(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")