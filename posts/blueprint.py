# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template

from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder='templates')

# http://localhost/blog/
@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

# http://localhost/blog/<slug>
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = Post.tags
    return render_template('posts/post_detail.html', post = post,tags=tags)

# http://localhost/blog/<slug>
@posts.route('/<slug>')
def tag_detail(slug):
    tags = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tags = tags, posts = posts)
