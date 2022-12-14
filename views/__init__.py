"""
  Create a Blueprint object to manage app routes
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from views.categories import *
from views.products import *
