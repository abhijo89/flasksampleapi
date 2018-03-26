__author__ = 'abhilash'
import os
import logging
from flask import Flask
from raven.contrib.flask import Sentry

logger = logging.getLogger(__name__)

sentry = Sentry(
    dsn='https://7a2f721ff53a46188279fc5ddd009638:dc397b4102be46e7bee0180709c80fdf@sentry.io/623555',
    logging=True,
    level=logging.INFO,
)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
sentry.init_app(app)

@app.route('/')
def hello():
    raise Exception("Demo Exception !")
    return "Hello World!"



@app.route('/<name>')
def hello_name(name):
    logger.warning("This is an error !", exc_info=1)
    return "Hello {}! You are awesome!".format(name)

if __name__ == '__main__':
    app.run()
