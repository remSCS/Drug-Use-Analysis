from flask import Blueprint
from flask_restplus import Api
from Views.Datasets import namespace as ns1
from Views.Analysis import namespace as ns2
from Views.Models import namespace as ns3

blueprint = Blueprint("api", __name__, url_prefix="/v1")

api_extension = Api(
    blueprint,
    contact="Julie HIGELIN & Rémi Lombard",
    title="Drug consumption - Python for Data Analysis",
    version="2.3",
    description="The goal is to create a simple API that will be using our models to generate predictions.",
    doc="/doc",
)

api_extension.add_namespace(ns1)
api_extension.add_namespace(ns2)
api_extension.add_namespace(ns3)