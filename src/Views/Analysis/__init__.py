from flask import send_file
from flask_restplus import Namespace, Resource, fields
from hook import find_file

namespace = Namespace(
    "Data_Analysis",
    "This is where you can find what we have plotted in order to understand the data we are dealing with.",
)

@namespace.route("/AgeCannabis")
class target_composition(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Cannabis consumption in funtion of age """
        TRUE_PATH = find_file(
            fullname="AgeCannabis", extension=".png", path="img/",
        )
        print(TRUE_PATH)

        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/AllDrugsConsumption")
class drug_composition(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Plot of the consumption of each drug """
        TRUE_PATH = find_file(
            fullname="AllDrugsConsumption", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/BinaryClassification")
class Education_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Binary classification """
        TRUE_PATH = find_file(
            fullname="BinaryClassification", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/Consumption1")
class Age_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ 1st plot of the consumption of some of the drugs """
        TRUE_PATH = find_file(
            fullname="Consumption1", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/Consumption2")
class Ethnicity_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ 2nd plot of the consumption of some of the drugs """
        TRUE_PATH = find_file(
            fullname="Consumption2", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/Consumption3")
class Gender_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ 3rd plot of the consumption of some of the drugs """
        TRUE_PATH = find_file(
            fullname="Consumption3", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/Consumption4")
class Escore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ 4th plot of the consumption of some of the drugs """
        TRUE_PATH = find_file(
            fullname="Consumption4", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/DemographicCountFrequency")
class Nscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Demographic infographic """
        TRUE_PATH = find_file(
            fullname="DemographicCountFrequency", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/DemographicPies")
class Oscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Demographic pie chart """
        TRUE_PATH = find_file(
            fullname="DemographicPies", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/DrugCorrelation")
class Cscore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Drug consumption correlation """
        TRUE_PATH = find_file(
            fullname="DrugCorrelation", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/DrugProfileCorrelation")
class Ascore_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Drug usage in correlation to a type of profile """
        TRUE_PATH = find_file(
            fullname="DrugProfileCorrelation", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/FrequentConsumers")
class Impulsiveness_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Frequent consumers """
        TRUE_PATH = find_file(
            fullname="FrequentConsumers", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)

@namespace.route("/FrequentConsumersYear")
class nscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Consumers within the last year """
        TRUE_PATH = find_file(
            fullname="FrequentConsumersYear", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)

@namespace.route("/FrequentConsumersDecade")
class SS_vs_Target(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Consumers within the last decade"""
        TRUE_PATH = find_file(
            fullname="FrequentConsumersDecade", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)

@namespace.route("/PersonalityHeatmap")
class escore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Heatmap of the personalities interviewed """
        TRUE_PATH = find_file(
            fullname="PersonalityHeatmap", extension=".png", path="img\\New",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/PersonnalityCountFrequency")
class oscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Inforgraphic of the personalities interviewed """
        TRUE_PATH = find_file(
            fullname="PersonnalityCountFrequency", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)


@namespace.route("/SSCannabis")
class cscore_drugs(Resource):
    @namespace.response(200, "Success")
    def get(self):
        """ Cannabis usage in function of SS """
        TRUE_PATH = find_file(
            fullname="SSCannabis", extension=".png", path="img/",
        )
        return send_file(TRUE_PATH, cache_timeout=2)