from flask import render_template, flash, redirect, request
from .forms import RegistrationForm, LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
	msg = {'message': 'Welcome to the H2O Application'}
	title = 'Home'
	return render_template('index.html', title=title, msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data, form.password.data)
		db_session.add(user)
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		flash('Thanks for logging in.')
		return redirect('/index')
	return render_template('login.html', title='Log In', form=form)
