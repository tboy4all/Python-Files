from flask import Flask, render_template, request # we are now importing just more than Flask!

apptest = Flask(__name__)

# @apptest.route('/')
# def greet():
# 	return "Hello Coders!"

# @apptest.route('/name/<person>')
# def say_name(person):
# 	return f"How are you {person}!!!"

# @apptest.route('/name/<int:num>')
# def number(num):
# 	return f"Your Number is {num}!!!"

@apptest.route('/')
def welcome():
	names_of_instructors = ["Sam", "Idris", "Aisha"]
	random_name = "Kaffy"
	return render_template('index.html', names=names_of_instructors, name=random_name)

@apptest.route('/second')
def second():
	return "WELCOME TO THE SECOND PAGE!"

@apptest.route('/title')
def title():
	return render_template('title.html')

# we need a route to render the form
@apptest.route('/show-form')
def show_form():
	return render_template('first-form.html')

# we need to do something when the form is submitted
@apptest.route('/data')
def print_name():
	first = request.args.get('first')
	last = request.args.get('last')
	return f"You put {first} {last}"