from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
 
# Create flask instance 
app = Flask(__name__)
 
# add databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ancestry2.db'
app.config['SECRET_KEY'] = "placeholder"
 
# Initialiaze the database
db = SQLAlchemy(app)

# Create the Models
class Profile(db.Model):
    # Id : Field which stores unique id for every row in
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

#  Create a From class (this is for an intake, mostly for me to test stuff and then once I can try to upload items into the db, should work...
#  then once i get this stuff working, I'll check out that prettyprint dudes thing)

#  Create a From class to enter stuff in teh db
class ProfileForm(FlaskForm):
    first_name = StringField("first Name", validators=[DataRequired()])
    last_name = StringField(" last Name", validators=[DataRequired()])
    age = IntegerField("age", validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route("/")
def welcome():
    return(
    '''
    placeholder
    ''')

@app.route("/test", methods=['GET', 'POST'])
def add_profile():
    first_name = None
    form = ProfileForm()
    if form.validate_on_submit():
        profile = Profile.query.filter_by(first_name=form.first_name.data).first()
        if profile is None:
            profile = Profile(first_name=form.first_name.data, last_name=form.last_name.data, age=form.age.data)
            db.session.add(profile)
            db.session.commit()
        first_name = form.first_name.data
        form.first_name.data = ''
        form.last_name.data = ''
        form.age.data = ''
    our_profiles = Profile.query.order_by(Profile.first_name)
    return render_template('add_profile.html',
                           form = form,
                           first_name = first_name,
                           our_profiles=our_profiles)

if __name__ == '__main__':
    app.run(debug=True)