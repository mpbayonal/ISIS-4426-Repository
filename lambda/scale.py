import json
import os
import requests
import heroku3

def scaleTo1(event, context):

    heroku_conn = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
    app = heroku_conn.app('designmatch4')
    app.process_formation()['worker'].scale(1)


def scaleTo2(event, context):
    heroku_conn = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
    app = heroku_conn.app('designmatch4')
    app.process_formation()['worker'].scale(2)


def scaleTo3(event, context):

    heroku_conn = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
    app = heroku_conn.app('designmatch4')
    app.process_formation()['worker'].scale(3)


def scaleTo4(event, context):

    heroku_conn = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
    app = heroku_conn.app('designmatch4')
    app.process_formation()['worker'].scale(4)
