from flask import Flask
from Views import blueprint as ep

app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = "list"
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.register_blueprint(ep)
app.run(debug=True)