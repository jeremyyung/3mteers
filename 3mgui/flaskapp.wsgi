import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/FlaskApp/')

from main import app as application

application.secret_key = 'oi23jr9avi'