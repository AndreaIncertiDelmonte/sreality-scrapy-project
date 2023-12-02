# Connect to the MYSQL database
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://scrapy_u:scrapy_p@db:5432/sreality_db'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
