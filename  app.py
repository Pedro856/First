from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('rembember me')

@app.route('/')
def index():
    return render_template('bora.html')

@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

app.run(debug=True)