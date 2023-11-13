from flask import Flask
from extensions import client

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Register blueprints here
    from main import bp as main_bp
    app.register_blueprint(main_bp)


    @app.route('/')
    def test_page():
        return 'Healthy!'

    return app

if __name__ == '__main__':
	create_app(config_class=Config).run(host='0.0.0.0', port=5000)