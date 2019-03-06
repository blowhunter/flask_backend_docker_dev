from flask import Flask

def create_app():
    from . import api, models

    app = Flask(__name__, instance_relative_config=True)
    api.init_app(app)
    models.init_app(app)

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)