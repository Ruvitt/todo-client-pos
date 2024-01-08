from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
import users

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)

users_api = users.Users()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/')
def listUsers():
    users = users_api.listUsers()
    return render_template('users.html', usersList = users)

@app.route('/users/<int:user_id>/', methods = ['GET'])
def getUser(user_id):
    user = users_api.getUser(user_id)
    return render_template('users.html', user = user)

@app.route('/users/create/', methods = ['GET', 'POST'])
def createUser():
    form = users_api.UserForm()
    formName = "Usuario"

    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'username': form.username.data,
            'email': form.email.data,
            'adress': form.adress.data,
            'phone': form.phone.data,
            'website': form.website.data,
            'company': form.company.data
        }
        # enviar para a api
        users_api.createUser(user_data)
        return redirect(url_for('listUsers'))
    
    return render_template('create.html', form = form, formName = formName)

@app.route('/users/update/<int:user_id>/', methods = ['GET', 'POST'])
def updateUser(user_id):
    user = users_api.getUser(user_id)
    form = users_api.UserForm()
    formName = "Usuario"

    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'username': form.username.data,
            'email': form.email.data,
            'adress': form.adress.data,
            'phone': form.phone.data,
            'website': form.website.data,
            'company': form.company.data
        }
        # enviar para a api
        users_api.updateUser(user_id, user_data)
        return redirect(url_for('listUsers'))
    
    return render_template('update.html', form = form, user = user, formName = formName)

@app.route('/users/delete/<int:user_id>/', methods = ['GET', 'POST'])
def deleteUser(user_id):
    try:
        users_api.deleteUser(user_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('listUsers'))
    return redirect(url_for('listUsers'))