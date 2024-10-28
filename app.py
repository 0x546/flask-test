from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/test')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def contact():
    return render_template('welcome.html')

# login example
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

# Sample user for demonstration (In real applications, use a database)
users = {'user@example.com': generate_password_hash('password')}

class LoginForm(FlaskForm):
    email = StringField('Email', default='user@example.com', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email in users and check_password_hash(users[email], password):
            flash('Login successful!', 'success')
            return render_template('login.html', form=form, redirect_url='/')
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
