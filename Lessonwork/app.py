# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# access sqlite database
engine = create_engine('sqlite:///hawaii.sqlite')

# reflect db into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link to db
session = Session(engine)

# set up flask
app = Flask(__name__)

