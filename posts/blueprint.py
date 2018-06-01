# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template
from models import Post, Tag
from flask import request, redirect
from .forms import PostForm
from app import db
from flask import url_for
from flask_security import login_required
from flask import redirect, url_for, request


posts = Blueprint('posts', __name__, template_folder='templates')


''' Создание поста '''
# http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print ('Something wrong')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


''' Редактирование поста '''
# http://localhost/blog/edit
@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


# http://localhost/blog/
@posts.route('/')
def index():
    # Поиск
    search = request.args.get('search')
    page = request.args.get('page')

    if page and page.isdigit(): # Если переменная имеет значение и переменная является цифрой
        page = int(page) # Преобразуем переменную в цифру
    else: # Иначе ...
        page = 1 # Даем значение переменной 1

    # если выполняется поиск
    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search))
    else: # иначе...
        #Выводим все посты
        posts = Post.query.order_by(Post.created.desc())

    # пагинация
    pages = posts.paginate(page=page, per_page=5)
    # Выводим шаблон
    return render_template('posts/index.html', posts=posts, pages=pages)


# http://localhost/blog/<slug>
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# http://localhost/blog/<slug>
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
