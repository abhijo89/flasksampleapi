import os
import sys
from SimpleApi.config.application_config import app

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))


from views.view_api import *



if __name__ == '__main__':
    app.run()
