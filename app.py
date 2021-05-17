

from redis import StrictRedis
from flask import Flask

app = Flask(__name__)


def conection():
    conection = StrictRedis(host='localhost', port=6379)
    if(conection.ping()):
        print('conection ok')
    else:
        print('no conection')

@app.route('/')
def index():
    conection()
    return "hola mundo"



if(__name__ == '__main__'):
    app.run(host='localhost', port=5000, debug=False)