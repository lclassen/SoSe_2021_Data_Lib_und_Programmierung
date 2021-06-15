# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:49:35 2021

@author: User
"""

from flask import Flask

print(__name__)
app = Flask(__name__) 

@app.route("/")
def start_page():
    return "<p>Hello World! Hope you are good!!!</p>"
