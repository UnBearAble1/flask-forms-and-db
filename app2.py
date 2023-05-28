import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///ancestry.db")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save the reference to the table, for ancestry, the table is ancestry

Ancestry = Base.classes.ancestry

# Create the session
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    placeholder
    ''')

# Name, str mod, dex mod
@app.route("/elf")
def elf():
    ancestry = session.query(Ancestry.str_mod).all()

    return jsonify(ancestry)


