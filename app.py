from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yogikadikar@localhost/todo'

db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text= db.Column(db.String(250))
    complete= db.Column(db.Boolean)

    


@app.route('/')
def index():
   return render_template('index.html')

if(__name__) == "__main__":
    app.run(debug=True)
