from flask_restplus import Namespace, Resource, fields
from config import raiseError
from modelling import defaultValue
from flask import send_file
from hook import find_file
import pickle
import pandas as pd

namespace = Namespace("Model")

payload = namespace.model(
    "model",
    {
        "Age": fields.Integer(
            description="""Age""",
            required=True,
        ),
        "Gender": fields.Integer(
            description="""Gender: if it is a male use 1 and female use 0.""",
            required=True,
        ),
        "Education": fields.Integer(
            description="""Education:
                        1: idividual left school before 16 years
                        2: idividual left school at 16 years
                        3: idividual left school at 17 years
                        4: idividual left school at 18 years
                        5: idividual went to some college or university, no certificate or degree
                        6: idividual has a professional certificate/ diploma
                        7: idividual has a university degree
                        8: idividual has a masters degree
                        9: idividual has a doctorate degree""",
            required=True,
        ),
        "Country": fields.String(
            description="""Country: Australia / Canada / Ireland / USA / UK / NZ / Other""",
            required=True,
        ),
        "Ethnicity": fields.String(
            description="""Ethnicity: Asian / Black / Mixed-Black-Asian / Mixed-White-Asian / Mixed-White-Black / White / Other""",
            required=True,
        ),
        "Nscore": fields.Integer(
            description="""Nscore: Neurotism score related to whether the patient has these characteristic: Anxiety, Angry/Hostility, Depression, Timidity, Impulsivity, Vulnerability 
            \n12-60""",
            required=True,
        ),
        "Escore": fields.Integer(
            description="""Escore: Extraversion level realted to Warmth/kindness, Gregariousness, Assertiveness, Activity, Excitment Seeking, Positive Emotion
            \n16-59""",
            required=True,
        ),
        "Oscore": fields.Integer(
            description="""Oscore: Open mindness level related to Fantasy, Aesthetics, Feelings, Actions, Ideas, Values/liberalism
            \n24-60""",
            required=True,
        ),
        "Ascore": fields.Integer(
            description="""Ascore: Agreeableness level related to Trust, Straightforwardness, Altruism, Compliance, Modesty, Tendermindedness
            \n12-60""",
            required=True,
        ),
        "Cscore": fields.Integer(
            description="""Cscore: Conscientiousness related to Competence, Order, Dutifulness, Achievement Striving, Self-Discipline, Deliberation
            \n17-59""",
            required=True,
        ),
        "SS": fields.Integer(
            description="""SS: Barrat Impulsiveness Test \nFactors: Attention, Cognitvity, Motor, Perseverance, Self-Control.
             \n71-249""",
            required=True,
        )})

@namespace.route("/Logistic_Regression")
class LGR(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """ Predict drugs used with model based on Logistic Regression """
        try:
            payload = defaultValue(payload=namespace.payload, flag=False)
            
            model_logreg_file = "src\\Models\\model_logreg.sav"
            with open(model_logreg_file, "rb") as file:
                model_logreg = pickle.load(file)
            payload = pd.DataFrame(payload.value, index=["0"])
            pred = model_logreg.predict(payload)
            print(payload)
            return pred

        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}

@namespace.route("/KNN")
class KNNModel(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """ Predict drugs used with model based on KNN """
        try:
            payload = defaultValue(payload=namespace.payload, flag=False)
            model_fn = "src\\Models\\model_logreg.sav"
            with open(model_fn, "rb") as file:
                print("here after")
                model = pickle.load(file)
            payload = pd.DataFrame(payload.value, index=["0"])
            pred = model.predict(payload)
            output = {"response": pred[0]}
            return output

        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}

@namespace.route("/Decision_Tree")
class Decision_TreeModel(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """ Predict drugs used with model based on Regression Trees """
        try:
            payload = defaultValue(payload=namespace.payload, flag=False)
            model_fn = "src\\Models\\model_decision_tree.sav"
            with open(model_fn, "rb") as file:
                model = pickle.load(file)
            payload = pd.DataFrame(payload.value, index=["0"])
            pred = model.predict(payload)
            output = {"response": pred[0]}
            return output

        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}

@namespace.route("/Random_Forest")
class Random_ForestModel(Resource):
    @namespace.doc(body=payload)
    @namespace.response(200, "Success")
    def post(self):
        """ Predict drugs used with model based on Random Forest """
        try:
            payload = defaultValue(payload=namespace.payload, flag=False)
            model_fn = "src\\Models\\model_random_forest.sav"
            with open(model_fn, "rb") as file:
                model = pickle.load(file)
            payload = pd.DataFrame(payload.value, index=["0"])
            pred = model.predict(payload)
            output = {"response": pred[0]}
            return output

        except Exception as e:
            if raiseError.JSONERROR in e.__str__():
                return {"response": {"error": raiseError.JSONMESSAGE}}
            elif raiseError.TYPEERROR in e.__str__():
                return {"response": {"error": raiseError.TYPEMESSAGE}}