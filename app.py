import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://boot:b00tUser@myfirstcluster-qugxt.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_breakfast')
def get_breakfast():
    return render_template("breakfast.html", breakfast=mongo.db.breakfast.find())

    
@app.route('/get_lunch')
def get_lunch():
    return render_template("lunch.html", lunch=mongo.db.lunch.find())

@app.route('/get_desert')
def get_desert():
    return render_template("desert.html", desert=mongo.db.desert.find())

@app.route('/get_dinner')
def get_dinner():
    return render_template("dinner.html", dinner=mongo.db.dinner.find())

@app.route('/addrecipe')
def addrecipe():
    return render_template('addrecipe.html')




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)