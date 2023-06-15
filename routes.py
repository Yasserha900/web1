from flask import render_template, request
from app import app, db
from app.models import Post, Tag
from datetime import datetime
from app.forms import EditProfileForm

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()  # Laden Sie alle Posts aus der Datenbank
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)  # Laden Sie den Post mit der gegebenen ID
    return render_template('post.html', post=post)

@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first_or_404()  # Laden Sie den Tag mit dem gegebenen Namen
    return render_template('tag.html', tag=tag)
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)