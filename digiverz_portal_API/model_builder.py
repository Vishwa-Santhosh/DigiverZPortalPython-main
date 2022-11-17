from array import array
from turtle import color
from typing import Collection
from unittest import result
from urllib import request
from digiverz_portal_API.FlaskRestAPI import test_db
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import bson
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import json
from bson import json_util
from flask import jsonify, request
import numpy as np
from flask_cors import CORS, cross_origin
from bson.json_util import dumps

def model_builder_endpoint(endpoints):
    @endpoints.route("/mbresult", methods=['GET'])
    @cross_origin()
    def find_all_people():
        resp = {}
        collection = test_db.modelbuilder
        users = collection.find() 
        output = [{'age':user['age'], 'gender':user['gender'], 'bmi':user['bmi'], 'children':user['children'], 'smoker':user['smoker'], 'region':user['region'], 'result':user['result']} for user in users]
        resp ['data']=output
        
        return  resp #json.loads(json_util.dumps(user))  #jsonify(json_util.dumps(user))

    @endpoints.route("/modelBuilder", methods=['POST','GET'])
    def model_builder_pickel():

        collection = test_db.modelbuilder
       
        _req = request.get_json()
        _gender = _req['gender']
        _region = _req['region']
        _children = _req['children']
        _smoker = _req['smoker']
        _age = _req['age']
        _bmi = _req['bmi']
        _gendercode=_req['gender']
        _smokercode=_req['smoker']
        _regioncode=_req['region']

         #*importing the pickel file********
        if _gender == "male": 
            _gendercode=0
        else:
            _gendercode=1

        if _smoker == "yes": 
            _smokercode=0
        else:
            _smokercode=1

        if _region == "southeast": 
            _regioncode=0
        elif _region == "southwest":
            _regioncode=1
        elif _region == "northeast":
            _regioncode=2   
        else:
            _regioncode=3        

        print (_age,_gendercode,_bmi,_children,_smokercode,_regioncode)
        
        input_data = (int(_age),_gendercode,float(_bmi),_children,_smokercode,_regioncode) #*(age,sex,bmi,children,smoker,region)

        # changing input_data to a numpy array
        
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


        with open(r"C:\Users\wishwa\Desktop\PythonPractice-main\digiverz_portal_API\digiverz_portal.pkl", 'rb') as file:
            data = pickle.load(file)
        
        regressor_loaded = data["data"]
        
        y_prediction = regressor_loaded.predict(input_data_reshaped)
        
        print (y_prediction)
        mbresult = np.array_str(y_prediction)

        if  request.method == 'POST':
                    inserted_id = collection.insert_one({ 'age': _age,'gender': _gender.capitalize(),'bmi': _bmi, 'children': _children, 'smoker': _smoker, 'region': _region, 'result':mbresult}).inserted_id
                    print(inserted_id)
                    resp = jsonify("user inputs added succesfully")
                    resp.status_code = 200

        resp = jsonify("user inputs added succesfully")

        resp.status_code = 200

        return resp    
    
    return endpoints