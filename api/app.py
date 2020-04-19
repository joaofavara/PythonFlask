from flask import Flask, request, Response, jsonify
from database.db import initialize_db
from database.models import Music

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/test-database'
}

initialize_db(app)

@app.route('/', methods=['GET'])
def index():
    music = Music.objects().to_json()
    print(music)
    return Response(music, mimetype="application/json", status=200)

@app.route('/add', methods=['POST'])
def add_new_data():
    body = request.get_json()
    music = Music(**body).save()
    id = music.id
    return { 'id': str(id) }, 200

@app.route('/remove/<music_id>', methods=['DELETE'])
def remove_data(music_id):
    data = Music.objects(id=(music_id)).delete()
    return {'message': data }, 200

@app.route('/update/<music_id>', methods=['PUT'])
def update_data(music_id):
    body = request.get_json()
    Music.objects(id=(music_id)).update(**body)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
