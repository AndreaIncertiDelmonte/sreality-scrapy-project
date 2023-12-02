from flask import Flask, render_template

from models import Flat, db

def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database

    @app.route('/')
    def flats_listing():
        flats = Flat.query.all()

        return render_template("index.html", flats=flats)
    
    return app

app = create_app()

if __name__ == '__main__':  # Running the app
    app.run(host='0.0.0.0', port=8080, debug=True)















#if __name__ == '__main__':
#	print("Start server")
#	app.run(host='0.0.0.0', port=8080)





def create_app():
    # create and configure the Flask app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://pgu_scrapy:scrapy_pgu@0.0.0.0:5432/sreality_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)

    @app.route('/')
    def hello():
        flats = Flat.query.all()
        print(flats)
        
        return render_template("index.html", flats=flats)

    return app