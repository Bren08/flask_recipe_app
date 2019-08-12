import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import TEXT
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

recipes =  mongo.db.recipes
the_recipe = mongo.db.recipes
categories = mongo.db.categories

mongo.db.recipes.create_index([('$**', 'text')])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/view_recipe')
def view_recipe():
   records=list(mongo.db.recipes.find())
   return render_template("cuisine_recipe.html", recipes=records)

@app.route('/view_individual_recipe/<recipe_id>', methods=['GET', 'POST'])
def view_individual_recipe(recipe_id):
    mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, {"$inc": {"views": 1}})
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('view_individual_recipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/add_recipe')
def add_recipe():
    return render_template("insert_recipe.html", categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    payload = request.form.to_dict()
    payload.update({"views": 0})
    recipes.insert_one(payload)
    return redirect(url_for('view_recipe'))

@app.route('/edit_recipe/<recipe_id>', methods=['GET','POST'])
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {"_id": ObjectId(recipe_id)},
    {
        'img_url':request.form.get('img_url'),
        'category_name':request.form.get('category_name'),
        'title':request.form.get('title'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('method'),
        'nutrition':request.form.get('nutrition'),
        'views':request.form.get('views'),
        'cooking_time':request.form.get('cooking_time'),
        'date_entered':request.form.get('date_entered'),
        'author':request.form.get('author'),
    })
    return redirect(url_for('view_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('view_recipe'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    title = request.form.get('search')
    find = ({ '$text': { '$search': title }})
    results = mongo.db.recipes.find(find)
    return render_template('cuisine_recipe.html', 
    recipes=results, count=results.count())

@app.route('/view_count/<recipe_id>', methods=['GET', 'POST'])
def view_count(recipe_id):
    view_count = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, {"$inc": {"views": 1}})
    return render_template('view_recipe.html', recipe=view_count)

@app.route('/dash')
def dash():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)