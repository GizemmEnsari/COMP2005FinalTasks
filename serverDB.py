from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
server_db = SQLAlchemy(app)



class Info(server_db.Model):
    clickedRunButton = server_db.Column(server_db.Integer)
    revertSuccesfulCode = server_db.Column(server_db.String)
#
# class User(server_db.Model):
#     id = server_db.Column(server_db.Integer)