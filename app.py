# Import Flask and dependencies
from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create an app, being sure to pass __name__
app = Flask(__name__)
# To update secret key, use the config file and ignore config inyour gitignore file
app.config['SECRET_KEY'] = "Placeholder"

# Create a Form class
class CharacterNameForm(FlaskForm):
    name = StringField("Enter your Heroe's Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def index():
    a = 4
    b = 6
    c = a + b
    return render_template("index.html", number = c)

c = 15

# Creat name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = CharacterNameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
        name = name,
        form = form,
        number = c)

# practice calling in a db like its just python, use what you would do from just jupyter notebook and then try to simply create a route where a variable is called


# @ app.route ("/Name")
# def name ():
#     # enter your name here
#     return (update to DB), the next sheet

# Let's make the path for the character sheet
# First one, enter your name
# it gets saved to the DB
# moves to the next page
# name

# Second one, pick your ancestry, it will be predefined
# ancestry will impat base HP, and some stats

# so lets say we have more than one feat that gives you HP, you can create a field called additional mod.. yeah so every entry would need to have set to fill up everything.. and then after each update for a potentially new stat, add a new var to the table and update NAs to 0 (maybe keep it at NA, maybe that wont be an issue? That's also where you could use an NLP program to identify key words, see if it has the related tag and maybe make a list of anything where teh count of the tag word is high, suggest tags for the entry? That could be cool. Do the character sheet first and then check out the assisted.. get the list of tags he plans to have from Laz... anyway you are getting a head of yourse;f.

