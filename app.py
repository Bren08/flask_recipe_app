import os
from flask import Flask, render_template, redirect, session, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://boot:b00tUser@myfirstcluster-qugxt.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for('view_recipe'))
    return render_template('login.html', recipes=mongo.db.users.find())


@app.route('/view_recipe')
def view_recipe():
   records=list(mongo.db.recipes.find())
   return render_template("cuisine_recipe.html", recipes=records)



   
@app.route('/add_recipe')
def add_recipe():
    return render_template("insert_recipe.html", categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
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
        'category_name':request.form.get('category_name'),
        'title':request.form.get('title'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('method'),
        'nutrition':request.form.get('nutrition'),
        'views':request.form.get('views'),
        'cooking_time':request.form.get('cooking_time'),
        'author':request.form.get('author'),
    })
    return redirect(url_for('view_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('view_recipe'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)