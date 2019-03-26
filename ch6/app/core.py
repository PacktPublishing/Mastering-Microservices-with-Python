from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

from . import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost'
db = SQLAlchemy(app)


@app.route("/api/videos/<id>")
def get_video(id):
    result = database.get_video(id, session=db.session)
    length = result.get('length', timedelta())
    result['length'] = length.seconds
    return jsonify(result)


@app.route("/api/videos", methods=['POST'])
def add_video():
    j = request.get_json()
    title = j.get('title')
    owner_id = j.get('owner')
    length = j.get('length')
    video_id = database.add_video(title, owner_id, length, session=db.session)
    return jsonify({'id': video_id})


@app.route("/api/video/<id>", methods=['PATCH'])
def edit_video(id):
    j = request.get_json()
    title = j.get('title')
    owner_id = j.get('owner_id')
    database.modify_video(id, title, owner_id, session=db.session)
    return jsonify({'id': id})


def run():
    return app

