import os
import test
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
app = Flask(__name__)

@app.route('/lyrics')
def result():
	return test.test()
	




@app.route('/', methods = ['GET', 'POST'])
def hello():
	return  render_template("getInput.html")








if __name__ == '__main__':
    app.run(debug=True)
