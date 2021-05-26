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

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

recent_date = (session.query(Measurement.date).order_by(Measurement.date.desc()).first())
recent_date = list(np.ravel(recent_date))[0]

recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')

recent_year = int(dt.datetime.strftime(recent_date, '%Y'))
recent_month = int(dt.datetime.strftime(recent_date, '%m'))
recent_day = int(dt.datetime.strftime(recent_date, '%d'))

year_earlier = dt.date(recent_year, recent_month, recent_day) - dt.timedelta(days=365)
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
    results = session.query(Measurement.date, Measurement.prcp, Measurement.station).\
                filter(Measurement.date >='2016-08-23').\
                order_by(Measurement.date).all()

    prcp_data = []
    for result in results:
        prcp_dict = {result.date: result.prcp, 'Station': result.station}
        prcp_data.append(prcp_dict)
    return jsonify(prcp_data) 
    session.close()
    
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    session = Session(engine)
    results = session.query(Station.name).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)
    session.close()
    
@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
                filter(Measurement.date >= '2016-08-23').\
                order_by(Measurement.date).all()

    temp_data = []
    for result in results:
        temp_dict = {result.date: result.temp, 'Station': result.station}
        temp_data.append(temp_dict)
    return jsonify(temp_data)
    session.close()


def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    session = Session(engine)
    results = session.query().all() 
    session.close()

   
    return jsonify()


if __name__ == '__main__':
    app.run()