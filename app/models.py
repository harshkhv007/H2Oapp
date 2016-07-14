from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(100), index=True, unique=True)
	password = db.Column(db.String(40), index=True, unique=True)
#	authenticated = db.Column(db.Boolean, default=False)

	def __init__(self, username, email, password):
		#super(User, self).__init__(**kwargs)
		self.username = username
		self.email = email
		self.password = password

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
        	return True

	@property
	def is_anonymous(self):
        	return False

	def get_id(self):
        	try:
	            return unicode(self.id)  # python 2
        	except NameError:
	            return str(self.id)  # python 3

	def __repr__(self):
		return '<User %r>' %(self.username)
