from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
import users, todos, posts, comments

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect(app)

users_api = users.Users()
todos_api = todos.Todos()
posts_api = posts.Posts()
comments_api = comments.Comments()

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
    
    return render_template('createUser.html', form = form, formName = formName)

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
    
    return render_template('updateUser.html', form = form, user = user, formName = formName)

@app.route('/users/delete/<int:user_id>/', methods = ['GET', 'POST'])
def deleteUser(user_id):
    try:
        users_api.deleteUser(user_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('listUsers'))
    return redirect(url_for('listUsers'))

@app.route('/todos/')
def listTodos():
    todos = todos_api.listTodos()
    usersList = users_api.listUsers()

    return render_template('todos.html', todosList = todos, usersList = usersList)

@app.route('/todos/<int:todo_id>/', methods = ['GET'])
def getTodo (todo_id):
    todo = todos_api.getTodo (todo_id)
    return render_template('todos.html', todo = todo)

@app.route('/todos/create/', methods = ['GET', 'POST'])
def createTodo():
    form = todos_api.TodoForm()
    formName = "Tarefa"
    users = users_api.listUsers()

    if form.validate_on_submit():
        todo_data = {
            'user': form.user.data,
            'title': form.title.data,
            'completed': form.completed.data
        }

        # enviar para a api
        todos_api.createTodo (todo_data)
        return redirect(url_for('listTodos'))
    
    return render_template('createTodo.html', form = form, formName = formName, users = users)

@app.route('/todos/update/<int:todo_id>/', methods = ['GET', 'POST'])
def updateTodo (todo_id):
    todo = todos_api.getTodo (todo_id)
    form = todos_api.TodoForm()
    formName = "Tarefa"
    users = users_api.listUsers()

    if form.validate_on_submit():
        todo_data = {
            'user': form.user.data,
            'title': form.title.data,
            'completed': form.completed.data
        }

        # enviar para a api
        todos_api.updateTodo (todo_id, todo_data)
        return redirect(url_for('listTodos'))
    
    return render_template('updateTodo.html', form = form, todo = todo, formName = formName, users = users)


@app.route('/todos/delete/<int:todo_id>/', methods = ['GET', 'POST'])
def deleteTodo (todo_id):
    try:
        todos_api.deleteTodo (todo_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('listTodos'))
    return redirect(url_for('listTodos'))

@app.route('/posts/')
def listPosts():
    posts = posts_api.listPosts()
    users = users_api.listUsers()

    return render_template('posts.html', postsList = posts, usersList = users)

@app.route('/posts/<int:post_id>/', methods = ['GET'])
def getPost (post_id):
    post = posts_api.getPost (post_id)
    return render_template('posts.html', post = post)

@app.route('/posts/create/', methods = ['GET', 'POST'])
def createPost():
    form = posts_api.PostForm()
    users = users_api.listUsers()
    formName = "Post"

    if form.validate_on_submit():
        post_data = {
            'user': form.user.data,
            'title': form.title.data,
            'body': form.body.data
        }

        # enviar para a api
        posts_api.createPost (post_data)
        return redirect(url_for('listPosts'))
    
    return render_template('createPost.html', form = form, formName = formName, users = users)

@app.route('/posts/update/<int:post_id>/', methods = ['GET', 'POST'])
def updatePost (post_id):
    post = posts_api.getPost (post_id)
    form = posts_api.PostForm()
    users = users_api.listUsers()
    formName = "Post"

    if form.validate_on_submit():
        post_data = {
            'user': form.user.data,
            'title': form.title.data,
            'body': form.body.data
        }

        # enviar para a api
        posts_api.updatePost (post_id, post_data)
        return redirect(url_for('listPosts'))
    
    return render_template('updatePost.html', form = form, post = post, formName = formName, users = users)

@app.route('/posts/delete/<int:post_id>/', methods = ['GET', 'POST'])
def deletePost (post_id):
    try:
        posts_api.deletePost (post_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('listPosts'))
    return redirect(url_for('listPosts'))

@app.route('/comments/')
def listComments():
    comments = comments_api.listComments()
    posts = posts_api.listPosts()

    return render_template('comments.html', commentsList = comments, postsList = posts)

@app.route('/comments/<int:comment_id>/', methods = ['GET'])
def getComment (comment_id):
    comment = comments_api.getComment (comment_id)
    return render_template('comments.html', comment = comment)

@app.route('/comments/create/', methods = ['GET', 'POST'])
def createComment():
    form = comments_api.CommentForm()
    formName = "Comentario"
    postsList = posts_api.listPosts()

    if form.validate_on_submit():
        comment_data = {
            'post': form.post.data,
            'name': form.name.data,
            'email': form.email.data,
            'body': form.body.data
        }

        # enviar para a api
        comments_api.createComment (comment_data)
        return redirect(url_for('listComments'))
    
    return render_template('createComment.html', form = form, formName = formName, postsList = postsList)

@app.route('/comments/update/<int:comment_id>/', methods = ['GET', 'POST'])
def updateComment (comment_id):
    comment = comments_api.getComment (comment_id)
    form = comments_api.CommentForm()
    formName = "Comentario"
    postsList = posts_api.listPosts()

    if form.validate_on_submit():
        comment_data = {
            'post': form.post.data,
            'name': form.name.data,
            'email': form.email.data,
            'body': form.body.data
        }

        # enviar para a api
        comments_api.updateComment (comment_id, comment_data)
        return redirect(url_for('listComments'))
    
    return render_template('updateComment.html', form = form, comment = comment, formName = formName, postsList = postsList)

@app.route('/comments/delete/<int:comment_id>/', methods = ['GET', 'POST'])
def deleteComment (comment_id):
    try:
        comments_api.deleteComment (comment_id)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for('listComments'))
    return redirect(url_for('listComments'))