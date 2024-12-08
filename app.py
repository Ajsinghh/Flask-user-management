from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ajsingh@localhost/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f"<User {self.name}>"


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html',users=users)

if __name__  == "__main__":
    app.run(debug= True)
