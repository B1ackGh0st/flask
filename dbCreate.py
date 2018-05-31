# -*- coding: utf-8 -*-

from app import db
from app import user_datastore
from models import User
from app import user_datastore

user = User.query.first()
user_datastore.create_role(name='admin', description='Administrator')
db.session.commit()

from models import Role
role = Role.query.first()
user_datastore.add_role_to_user(user, role)
db.session.commit()

'''
p = Post(title = 'Заголовок первого поста', body='Контент первого поста')
db.session.add(p)
db.session.commit()
p
p1 = Post(title = 'Заголовок второго поста', body='Контент второго поста')
db.session.add(p1)
db.session.commit()
p1
p2 = Post(title = 'Заголовок третьего поста', body='Контент третьего поста')
db.session.add(p2)
db.session.commit()
p2
'''

