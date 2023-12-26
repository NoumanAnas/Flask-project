# define API's
from flask import render_template, request, redirect
from flask_app import app


@app.route('/')
def home():
    return "<h1>This is home page</h1>"