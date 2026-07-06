import os
import sys

# Add the project directory to python path
sys.path.append(os.path.dirname(__file__))

from my_app.wsgi import application

# Vercel expects the handler to be named 'app'
app = application
