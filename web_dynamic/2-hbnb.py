"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
from models import storage
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('web_dynamic/2-hbnb.py')
@app.route('/2-hbnb')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('2-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
