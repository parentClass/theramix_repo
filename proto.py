from gevent import monkey; monkey.patch_all()
from bottle import run, route, static_file, request
import tenjin
from tenjin.helpers import *
from pymongo import MongoClient


@route('/')
def index():
	return static_file('index.hmtl')




client = MongoClient("52.175.35.161", 27017)
db = client.danielsarabusing
engine = tenjin.Engine(path=['./statics'])
run(server='gevent', host="localhost", port=8001, debug=False)