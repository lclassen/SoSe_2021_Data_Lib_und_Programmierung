# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:49:35 2021

@author: User
"""

from flask import Flask

print(__name__)
app = Flask(__name__) 

@app.route("/") # Start page
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info") # Information page
def show_info():
    return "<p>Some information</p>"

@app.route("/isbn/<isbn>")
def isbn_display(isbn):
    return "<p>ISBN given: </p>"
