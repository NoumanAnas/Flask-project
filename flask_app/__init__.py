# initialize the package and can contain code that sets up the package's internal state

# from flask import Flask
# from flask_app.config import Config


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

    
#      # Import and register views and models
#     from flask_app import views, models
#     # Additional setup code, such as registering blueprints, initializing extensions, etc.

#     return app


from flask import Flask
from flask_app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Import views and models after creating the app instance
from flask_app import views, models

# Additional setup code...
