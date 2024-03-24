from flask import Flask  # type: ignore
from markupsafe import escape  # type: ignore


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


# para executar o código no terminal "flask --app <script> run --debug"