from flask import render_template
from flask.ext.mail import Message
from app import mail, app
from config import ADMINS
from .decorators import async

@async
def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def send_notification(user):
	send_to = [user.email]
	send_email("Your H2O App Notification", ADMINS[0], send_to, render_template("notify_email.txt", user = user), render_template("notify_email.html", user = user))
