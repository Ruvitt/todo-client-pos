import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, BooleanField, SelectField

class Todos:
    base_url = "http://127.0.0.1:8000/todos/"

    class TodoForm(FlaskForm):
        user = StringField('Usuario')
        title = StringField('Tarefa')
        completed = BooleanField('Completo')
        submit = SubmitField('Enviar')

    def listTodos(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def getTodo (self, todo_id):
        url = self.base_url + str(todo_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Id invalido")
        
    def createTodo (self, todo_data):
        url = self.base_url
        response = requests.post(url, json = todo_data)

        if response.status_code != 201:
            print(f"Failed to create todo: {response.content}")
        else:
            print(f"Todo created: {response.json()}")
        
    def updateTodo (self, todo_id, todo_data):
        url = self.base_url + str(todo_id) + "/"
        response = requests.put(url, data = todo_data)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")
        
    def deleteTodo (self, todo_id):
        url = self.base_url + str(todo_id)
        response = requests.delete(url)

        if response.status_code == 200:
            return response.json()
        
        else:
            raise ValueError("Problema na execucao")