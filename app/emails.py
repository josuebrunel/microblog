from app import mail
from flask.ext.mail import Message

from flask import render_template
from config import ADMINS

from threading import Thread
from decorators import async

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):

    msg = Message(subject, sender, recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)

def follower_notification(followed, follower):

    response  = send_email(
        "[Microblog] {0} is now following".format(follower.nickname),
        ADMINS[1],
        [followed.email],
        render_template('follower_email.txt', user= followed, follower= follower),
        render_template('follower_email.html', user= followed, follower= follower)
    )
    print(response)

    