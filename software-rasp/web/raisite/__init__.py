import os
from flask import Flask
from raisite.parametros import ParamForm
from flask import render_template, url_for, redirect

# creates the Flask instance
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'raisite.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    @app.route('/parametros', methods=('GET', 'POST'))
    def parametros():
        parametros = ParamForm()
        if parametros.validate_on_submit():
             rai_volume = parametros.inspiration_volume
             print(rai_volume)
        else:
             print(parametros.errors)
        return render_template('blog/param.html', parametros=parametros)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
