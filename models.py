from app import db
from datetime import datetime

class Post(db.Mode):

    id = db.Column(db.integer, primary_key = True)
    title = db.Column(db.String(140)) #
    slug = db.Column(db.String(140), unique=True) # URL ЧПУ
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.nuw())

    def __init__(self, *args, **kwargs):
        super(Post, self), __init__(*args, **kwargs)
        self.slug = generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)