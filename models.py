# -*- coding: utf-8 -*-
from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin

### Преобразование для ЧПУ ###
def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


### Таблица тегов ###
post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )


### Посты ###
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # ID
    title = db.Column(db.String(140))               # Заголовок
    slug = db.Column(db.String(140), unique=True)   # URL ЧПУ
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now()) # Дата создания

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


### Тэги ###
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # ID
    name = db.Column(db.String(100))                # Заголовок
    slug = db.Column(db.String(100), unique=True)   # URL ЧПУ

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)


    def __repr__(self):
        return '{}'.format(self.name)


### FLASK_SECURiTY ###

roles_users = db.Table('roles_users',
                     db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                     db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                     )
### Пользователи ###
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))