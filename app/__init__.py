import os
import sys

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
from api import Thread
api = Api(app)
api.add_resource(Thread, "/thread/<string:thread_id>")
