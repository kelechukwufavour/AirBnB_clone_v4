#!/usr/bin/python3
"""Flask app to generate complete HTML page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
from models import storage
import uuid
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/0-hbnb')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
