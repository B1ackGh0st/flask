# -*- coding: utf-8 -*-
import models
from app import db
db.create_all()
from models import Post

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
