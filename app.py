# from the flask library import a class named Flask
from flask import Flask, render_template, request

# create an instance of the Flask class
# app = Flask(__name__)

# # listen for a route to `/` - this is known as the root route
# @app.route('/')

# # when this route is reached (through the browser bar or someone clicking a link, run the following function)
# def hello():
# 	# this `return` is the response from our server. We are responding with the text "Hello World"
#     return "Hello World!"

# @app.route('/name')
# def welcome():
#     return "Welcome to our application!"

app = Flask(__name__)

# @app.route('/')
# def hello():
# 	return "Hello!"

# @app.route('/hi')
# def hi():
# 	return "Hi!"

# @app.route('/bye')
# def bye():
# 	return "Bye!"

# @app.route('/')
# def home():
# 	return "Welcome!"

# #let's make up a parameter called name. Its value is going to be WHATEVER someone requests, but we will respond with the string "The name is" along with the value in the URL.
# @app.route('/name/<person>')
# def say_name(person):
# 	return f"The name is {person}"

# # since all URL parameters are strings, we can convert them right away to another data type in our route definition
# @app.route('/name/<int:num>')
# def favorite_number(num):
# 	return f"Your favorite number is {num}, which is half of {num * 2}"

@app.route('/')
def welcome():
	names_of_instructors = ["Alaba", "Idris", "Aisha"]
	random_name = "Kaffy"
	return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
	return "WELCOME TO THE SECOND PAGE!"

@app.route('/title')
def title():
	return render_template('title.html')

# we need a route to render the form
@app.route('/show-form')
def show_form():
	return render_template('first-form.html')

# we need to do something when the form is submitted
@app.route('/data')
def print_name():
	first = request.args.get('first')
	last = request.args.get('last')
	return f"You put {first} {last}"