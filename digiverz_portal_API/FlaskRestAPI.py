import collections
from http import client
from inspect import _void
import pprint
from tokenize import Name
from dotenv import load_dotenv, find_dotenv
import os
import sys
import bson
import pickle
import pprint
import seaborn as sns

from pymongo import MongoClient
load_dotenv(find_dotenv())
from flask import Flask
import datetime
import json
import numpy as np
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS
from flask import jsonify, request
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename  
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, lit,regexp_replace,substring,to_timestamp,to_date,col
from pyspark.sql.types import DoubleType,StringType
from sklearn.preprocessing import LabelEncoder
from pyspark.sql.types import *
#from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
app = Flask(__name__)


CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'






#***************************************monogDB client***********************************************************


password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://digiverz:digiverz@cluster0.pbat0bd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
test_db = client.DigiverZ_Portal
collections = test_db.list_collection_names()
# print(collections)
#*spark session.................................................

#*exctracting data from mongodb and setting pandas dataframe

   
# collection=test_db.file
# record = collection.find_one({'_id':ObjectId('6340252034bbeaeb2a18cb49')})
# with open(record, 'rb') as pickle_file:
#     content = pickle.load(pickle_file)
#     df =  pd.DataFrame(list(content))
#     print(df)   








#*****************************************************************REST API Assignment *****************************************************************************

#all User list
def project_api_routes(endpoints):
  




#******Business_logic



    




    @endpoints.route("/user", methods=['GET'])
    
    def find_all_peopl():
        collection = test_db.login
        user = collection.find() 
        
        
        return json.loads(json_util.dumps(user))

    if __name__ == "__main__":
        app.run(debug=True)
    return endpoints