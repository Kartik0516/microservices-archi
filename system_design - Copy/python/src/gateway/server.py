import os, gridfs, pika, json # type: ignore
from flask import Flask, request, send_file
from flask_pymongo import PyMongo # type: ignore
from auth import validate
from auth_svc import access # type: ignore
from storage import util # type: ignore
from bson.objectid import ObjectId # type: ignore

server = Flask(__name__)

mongo_video = PyMongo(server, uri="mongodb://host.minikube.internal:27017/videos")

fs_videos = gridfs.GridFS(mongo_video.db)
fs_mp3s = gridfs.GridFS(mongo_mp3.db) # type: ignore

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err
