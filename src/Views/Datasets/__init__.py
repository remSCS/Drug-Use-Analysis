from flask_restplus import Namespace, Resource, fields
import pandas as pd
import os

namespace = Namespace("Dataset", "Relative to the data we had to use")

dataset_model = namespace.model(
    "dataset", {"data": fields.Raw(readonly=True, description="dataset columns")},
)


@namespace.route("/columns")
class basic_dataset(Resource):
    @namespace.marshal_list_with(dataset_model)
    @namespace.response(200, "Success")
    def get(self):
        """ Get an idea of the columns we were working with """
        df = pd.read_csv(os.getcwd() + "\\src\\Data\\drug_consumption.data")
        demographic_columns = ["Age","Gender","Education_Level","Country","Ethnicity"]
        personality_colomns = ["Nscore","Extraversion","Oscore","Ascore","Cscore","Impulsive","SS"]
        feature_columns = demographic_columns + personality_colomns
        drugs_columns = ["Alcohol","Amphet","Amyl","Benzos","Caffeine",
        "Cannabis","Chocolat","Cocaine","Crack","Ecstasy","Heroin","Ketamine",
        "Legalh","LSD","Meth","Mushrooms","Nicotine","Semer","VSA"]
        legal_drugs= ["Alcohol", "Caffeine", "Chocolat", "Nicotine"]
        illegal_drugs= ["Amphet","Amyl","Benzos","Cannabis","Cocaine","Crack","Ecstasy",
        "Heroin","Ketamine","Legalh","LSD","Meth","Mushrooms","Semer","VSA"]
        all_columns = feature_columns + drugs_columns
        df.columns = ["ID"] + all_columns
        
        output = {"data": {i: df.columns[i - 1] for i in range(1, len(df.columns) + 1)}}
        return output