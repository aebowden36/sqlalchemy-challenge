import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():

    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    
    session = Session(engine)
    results = session.query().all() 
    session.close()
    # Calculate the date 1 year ago from last date in database
    
    # Query for the date and precipitation for the last year
    
    # Dict with date as the key and prcp as the value
   
    
    
    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    
    session = Session(engine)
    results = session.query().all() 
    session.close()
    
    # Unravel results into a 1D array and convert to a list
    some_variable_stations_list = list(np.ravel(results)) # check this function
    return jsonify()


@app.route("/api/v1.0/temperatureObservation")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    session = Session(engine)
    results = session.query().all() 
    session.close()

    
    return jsonify()


def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    session = Session(engine)
    results = session.query().all() 
    session.close()

   
    return jsonify()


if __name__ == '__main__':
    app.run()