"""
  This module supplies the `get_categories` function view
"""

from views import app_views
from flask import make_response, jsonify
from engine.db_storage import DBStorage

@app_views.route('/categories', methods=['GET'])
async def get_categories():
  """
    Get all categories
  """
  storage = DBStorage()
  categories = await storage.all('category')
  return make_response(jsonify(categories), 200)
