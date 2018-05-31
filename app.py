# -*- coding: utf-8 -*-
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

### Migrate ###
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

### Admin ###
from models import *

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, **kwargs):
        return redirect(url_for('security'), next=request.url)



admin = Admin(app)
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))

### Flask-security ###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)