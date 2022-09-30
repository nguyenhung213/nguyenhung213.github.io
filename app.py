from datetime import datetime
from email.policy import default
from flask import Flask,render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
        id = db.Column(db.Integer, primary_key= True)
        content = db.Column(db.String(200), nullable = False)
        Completed = db.Column(db.Integer, default = 0)
        date_created = db.Column(db.DateTime, default = datetime.utcnow)

        def __repr__(self):
            return '<Task %r>' % self.id


@app.route('/')
def main():

    return render_template('index.html')

@app.route('/signup')

def showSignUp():

    return render_template("signup.html")   

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8080',debug=True)