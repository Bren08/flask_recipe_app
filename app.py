import os
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://boot:b00tUser@myfirstcluster-qugxt.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_breakfast')
def hello():
    return render_template("breakfast.html", breakfast=mongo.db.breakfast.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)