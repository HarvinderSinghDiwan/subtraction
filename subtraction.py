# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 04:19:02 2022

@author: Harvi
"""


from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/subtraction")
def subtract():
    args=request.args
    x=int(args.get('x'))
    y=int(args.get('y'))
    result={"first_number":x,"second_number":y,"subtraction":(x-y)}
    return  jsonify(result), {'Content-Type': 'application/json; charset=utf-8'}
app.run(debug=False,port=92)
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
