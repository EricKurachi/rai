import os

from flask import Flask
from raisite.forms_tab import TabForm
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

    @app.route("/tabela", methods=['GET','POST'])
    def tabela():
      forms_tab = TabForm()
      if forms_tab.validate_on_submit():
         patient_weight = forms_tab.weight.data
         patient_height = forms_tab.height.data
         patient_gender = forms_tab.gender.data
         if patient_gender == 'fem':
             pid_patient = 45.5+0.91*(100*patient_height-152.4)
         else:
             pid_patient = 50+0.91*(100*patient_height-152.4)
         print(pid_patient)
      else:
          print(forms_tab.errors)
      return render_template('tab.html', forms_tab=forms_tab)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
