import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.append('/usr/local/apache2/htdocs/3mgui/')
sys.path.append('/usr/local/apache2/htdocs/3mgui/lib/python3.12/site-packages')

from main import app as application

application.secret_key = 'oi23jr9avi'