from flask import render_template
from flask.ext.mail import Message
from app import mail, app
from config import ADMINS
from .decorators import async
from datetime import datetime, timedelta
import datetime

@async
def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def send_notification(user, value):
	send_to = [user.email]
	print send_to
	send_email("Your H2O App Notification", ADMINS[0], send_to, render_template("notify_email.txt", user = user, value=value), render_template("notify_email.html", user = user, value = value))

def timer_set(formvalue, user):
	print user
        if formvalue == 'gulp':
		print 'Its a gulp'
		ctime = datetime.datetime.now()
		print ctime
		ftime = ctime + datetime.timedelta(0,60)
		print ftime
		timer_check(app, user, ftime, formvalue)
        if formvalue == 'half_bottle':
		print 'Its half'
                #send_notification(g.user)
        if formvalue == 'full_bottle':
		print 'Its full'
                #send_notification(g.user)

@async
def timer_check(app, user, ftime, formvalue):
	print user
	with app.app_context():
		print user
		present_time = datetime.datetime.now()
#		while(present_time != ftime):
		if(ftime == ftime):
			print 'sending email.'
			send_notification(user, formvalue)
#			break
		else:
			print 'email not sent'
				#break
