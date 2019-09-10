
import os
from flask import Flask, request, json, abort
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='localhost', port=6379, db=0)

# TODO
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
# sentry_sdk.init(
#     dsn="https://2ba68720d38e42079b243c9c5774e05c@sentry.io/1316515",
#     integrations=[FlaskIntegration()],
#     release=os.environ.get("VERSION")
# )


@app.route('/greet', methods=['GET'])
def greeter():
    try:
        print('GREETINGS')

        global r
        r.set('foo', 'bar')
        print(r.get('foo'))
    except Exception as err:
        abort(500)

    return 'Success'