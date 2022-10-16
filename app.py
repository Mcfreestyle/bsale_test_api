"""
  Flask app
"""

from flask import Flask
from views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
  app.run(port=5000, debug=True)
