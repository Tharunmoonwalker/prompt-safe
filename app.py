from flask import Flask, flash, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from untitled11 import evaluate_input
from flask_migrate import Migrate
app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Secret key 
app.config['SECRET_KEY'] = "The secret key is a secret"

# Initialize the database    
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Create model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    feedback = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a string representation
    def __repr__(self):
        return '<Name %r>' % self.name

# Form Class
class UserForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    feedback = TextAreaField('Feedback:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = UserForm()

    # Form validation
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Your form was successfully submitted")
    return render_template("name.html", name=name, form=form)

@app.route('/users/add', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data, feedback=form.feedback.data)
            db.session.add(user)
            db.session.commit()
            flash("User added successfully with feedback")
        else:
            user.feedback = form.feedback.data
            db.session.commit()
            flash("User feedback updated successfully")
        return redirect(url_for('add_user'))
    
    our_users = Users.query.order_by(Users.date_added).all()
    return render_template('add_user.html', form=form, our_users=our_users)

@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        evaluation_result = evaluate_input(user_input)
        return render_template('index.html', result=evaluation_result)
    return render_template('index.html', result='')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.route('/article')
def article():
    return render_template('article.html')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
