#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:36:10 2018

@author: sapansoni
"""

from flask import Flask ,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True,host='127.0.0.1',port=5000)
