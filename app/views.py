from flask import render_template, flash, redirect, request, session, url_for, g, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import RegistrationForm, LoginForm
from app import app, db, lm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	msg = {'message': 'Welcome to the H2O Application'}
	title = 'Home'
	return render_template('index.html', user=user,title=title, msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	for i in form:
		print i
	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data, form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
        	return redirect(url_for('index'))
	form = LoginForm(request.form)
#	for i in form:
#		print i
	username = form.Username.data
	password = form.Password.data
#	print username
#	print password
	if request.method == 'POST' and form.validate():
		user = User.query.filter_by(username=username, password=password).first()
		if user is None:
			flash('Username/Password is incorrect.')
                	redirect(url_for('login'))
		else:
			if user.password == form.Password.data:
				#user.authenticated = True
				db.session.add(user)
				login_user(user)
				flash('Thanks for logging in.')
				return redirect(request.args.get('next') or url_for('index'))
	return render_template('login.html', title='Log In', form=form)

@app.before_request
def before_request():
        g.user = current_user

#@app.after_login
#def after_request:


@app.route("/logout", methods=["GET"])
@login_required
def logout():
	"""Logout the current user."""
	logout_user()
	flash('Thanks for using the H2O app')
	return render_template("logout.html")

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
