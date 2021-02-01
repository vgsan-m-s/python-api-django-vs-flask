# run command ::
# - pip install flask
# - python vg_test_app.py

import json
import flask
from flask_cors import CORS
from flask import request, jsonify, send_file

app = flask.Flask(__name__)
CORS(app)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>First Web/API</h1><p>Hello world!</p>"

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'
    },
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'
    },
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'
    }
]

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# API looks like - http://127.0.0.1:5000/api/v1/resources/books?id=2
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/api/v1/devices/all', methods=['GET'])
def api_devices_all():
    with open('data/devices.json') as f:
        data = json.load(f)
        return jsonify(data)

        
@app.route('/api/v1/device/<int:device_id>/user_log/all', methods=['GET'])
def api_device_user_log_all(device_id):
    with open('data/device_user_log.json') as f:
        data = json.load(f)
        data = [x for x in data if x['device_id'] == device_id]
        if len(data) > 0:
            data = data[0]
        else:
            data = {}
        return jsonify(data)

@app.route('/api/v1/device/<int:device_id>/user_log/<int:user_log_id>/download')
def downloadUserLog(device_id, user_log_id):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "data/device_user_log.json"
    return send_file(path, as_attachment=True, attachment_filename=(str(device_id) + str(user_log_id) + '.json'))

# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     return send_from_directory(directory=uploads, filename=filename)

#app.run()
app.run(host="0.0.0.0")