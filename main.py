from flask import Flask,render_template,request
import json
import pickle
import numpy as np
from app.utils import prediction

app=Flask(__name__)

@app.route("/cover",methods = ["POST","GET"])
def start():
    return render_template("insurance.html")

@app.route("/predict",methods = ["POST","GET"])
def predict_price():
   data=request.form
   pred_obj = prediction()
   predicted_cover = pred_obj.predict_cover(data)
   print(predicted_cover)

   return (predicted_cover)

@app.route("/123")
def demo():
    return "edited"

if __name__ == "__main__":
    app.run(debug=True)