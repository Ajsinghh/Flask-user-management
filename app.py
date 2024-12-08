from flask import Flask, render_template, request, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'fallback_secret_key')
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

from flask import request, redirect, url_for, flash

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')

        # Validate inputs
        if not name or not email or not role:
            flash('All fields are required!', 'error')
            return render_template('new_user.html')

        # Check for unique email
        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'error')
            return render_template('new_user.html')

        # Create a new user
        new_user = User(name=name, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash('User added successfully!', 'success')
        return redirect(url_for('users'))

    return render_template('new_user.html')

@app.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)  # Return a 404 error if the user is not found
    return render_template('user_detail.html', user=user)

if __name__  == "__main__":
    app.run(debug= True)
