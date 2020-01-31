from flask import Flask,request,render_template
import os
import cv
import numpy as np
import base64
from DataBasse import database


app = Flask(__name__)
ob=database()


@app.route("/", methods = ["GET"])
def home():
        return "WEB SERVICES"

#View Attendance from sqlite db
@app.route("/p/<prs>", methods = ["GET"])
def present(prs):
        return ob.get_AttendanceID(1)

#Get Image From APP INTO webservices
@app.route("/a", methods = ["POST"])
def get():

        #Decode Image
        data = base64.b64decode(request.form['img']) #Post json from Android app with key 'img' so it will have the value -> image
        #Pass Image into cv Class into process Method
        cv.process(data)
        return "done"

if __name__ == "__main__":
    app.run()