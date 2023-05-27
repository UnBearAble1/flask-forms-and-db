import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///ancestry.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Station = Base.classes.station

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
    return ('''hi''')
