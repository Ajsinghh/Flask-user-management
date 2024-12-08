# Flask User Management Application

This project is a simple Flask-based application that performs CRUD operations on a MySQL database. The application is designed to demonstrate API development, database interaction, and Git version control practices.

## Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Database Schema](#database-schema)
3. [SQL Queries](#sql-queries)
4. [Git Workflow](#git-workflow)
5. [Contributing](#contributing)


## Setup Instructions
1. First created virtual environment and activate it.
2. Then installed Flask and other dependecies like SQLAlchemy and dotenv
3. Then configured MySql Databse
4. Run the flask application using command "flask run"

## Database Schema
Database Name :- users
Table Name :- users

Column Name	         Data Type	    Description
id	                   INT	        Primary Key (Auto-Inc)
name	             VARCHAR	    User's name
email	             VARCHAR	    User's email
role	             VARCHAR	    User's role

## SQL Queries
1. To insert sample data:-
INSERT INTO users (name, email, role) VALUES
('Alice', 'alice@example.com', 'Admin'),
('Bob', 'bob@example.com', 'User'),
('Charlie', 'charlie@example.com', 'Manager');

2. To retrieve all users:-
SELECT * FROM users;

3. Retrieve a Specific User by ID:-
SELECT * FROM users WHERE id = <id>;


## Git Workflow
1. Intialize git repository:- git init
2. Create and switch to a new branch :- git checkout -b assignment
3. Stage and commit changes:- git add . and git commit -m "message"
4. Push the branch to the remote repository:- 
   git remote add origin <repository_url>
   git push -u origin assignment


## Contributing
1. Fork the repository.
2. Create a new branch for your feature:-
   git checkout -b feature/<feature-name>
3. Commit your changes and push them to your fork.
4. Create a pull request to the original repository.