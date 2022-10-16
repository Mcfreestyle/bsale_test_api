"""
  This module supplies these functions views:
    `get_products`,
    `get_products_by_category`
"""

from views import app_views
from flask import make_response, jsonify, abort, request
from engine.db_storage import DBStorage

@app_views.route('/products', methods=['GET'])
async def get_products():
  """
    file: documentation/products/products.yml
  """
  storage = DBStorage()

  search_var = request.args.get('search')
  if search_var:
    products = await storage.find('product', search_var)
  else:
    products = await storage.all('product')
  return make_response(jsonify(products), 200)

@app_views.route('/categories/<int:category_id>/products', methods=['GET'])
async def get_products_by_category(category_id):
  """
    file: documentation/products/products_by_category.yml
  """
  storage = DBStorage()
  category = await storage.get('category', category_id)
  if not category:
    abort(404)

  category_products = []
  products = await storage.all('product')
  for product in products:
    if product['category'] == category['id']:
      category_products.append(product)
  
  return make_response(jsonify(category_products), 200)
