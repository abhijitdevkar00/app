import os
import numpy as np
import flask
import pickle
from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return flask.render_template('index.html')


def Valuepredictor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,49)
    model=pickle.load(open("model_pickle", "rb"))
    result=model.predict(to_predict)
    return result[0]


@app.route('/result',methods=['POST'])
def predict():
    if request.method=='POST':
        to_predict_list=request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list=list(map(int, to_predict_list))
        result=ValuePredictor(to_predict_list)
        
        
        if int(result)==1:
            
            prediction='Genuen'
        else:
            prediction='Fraud'
            
            
            return render_template("result.html",prediction=prediction)
 
if __name__== "__main__":
    app.run(debug=True)
            
       
            
           
        
         


