from app import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'josue'}
    return render_template("index.html",title= 'home', user= user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, providers= app.config['OPENID_PROVIDERS'])