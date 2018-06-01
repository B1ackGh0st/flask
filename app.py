# -*- coding: utf-8 -*-
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user
from flask import redirect, request, url_for

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

### Migrate ###
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### Admin ###
from models import *

# Разграничение доступа к одминки и ее функциям
class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # next='' <- Сыылка куда будет перенапровлятся пользователь
        return redirect( url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generated_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)

class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body']

class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name']


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))


### Flask-security ###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)