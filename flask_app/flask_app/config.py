import os

## Connection details from ENV variables
postgres_user = os.getenv("POSTGRES_USER", "default_pg_user")
postgres_password = os.getenv("POSTGRES_PASSWORD", "default_pg_password")
postgres_host = os.getenv("POSTGRES_HOST", "127.0.0.1")
postgres_host_port = os.getenv("POSTGRES_HOST_PORT", "5432")
postgres_db = os.getenv("POSTGRES_DB", "default_pg_db")

# Connect to the MYSQL database
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    postgres_user,
    postgres_password,
    postgres_host,
    postgres_host_port,
    postgres_db
)

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
