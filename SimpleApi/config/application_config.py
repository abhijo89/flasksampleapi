__author__ = 'abhilash'
import hashlib
import socket
from SimpleApi.app import app

from flask.ext.mongoengine import MongoEngine


app.config['TESTING'] = True
app.config['SECRET_KEY'] = hashlib.md5(socket.gethostname() + '7h!5 !5 5@m673 C0D3').hexdigest()
app.debug = True
app.config['DEBUG_TB_PANELS'] = (
    'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
    'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
    'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel'
)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['MONGODB_SETTINGS'] = {
    'db': 'Store',
}
mongo_db = MongoEngine(app)