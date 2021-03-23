from flask import Flask

def myapp():
    app = Flask(__name__, template_folder="template", static_folder="static")
    #template folder refer to html template folder
    #static folder refer to static folder which has sub folder as images / site assets

    app.config["SECURITY_KEY"] = "8169500307shryumomo"

    from .views import view

    app.register_blueprint(view, url_prefex = "/")

    return app