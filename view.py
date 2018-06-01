# -*- coding: utf-8 -*-
from app import app
from flask import render_template

# http://localhost/
@app.route('/')
def index():
    return render_template('base.html')

# http://localhost/about
@app.route('/about')
def about():
    return render_template('about.html')

# http://localhost/contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


### PAGE 404 ###
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404