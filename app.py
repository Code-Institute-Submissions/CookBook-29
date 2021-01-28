import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def home():
    recipes = mongo.db.recipes.find()
    return render_template('pages/home.html', recipes=recipes)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Allow user to 
    get into the webapplication
    """
    if request.method == "POST":
        # check if email already exists in db
        user = mongo.db.users.find_one(
            {'email' : request.form.get('email')})
        if user:
            # ensure hashed password matches user input
            if check_password_hash(user['password'], request.form.get('password')):
                user_id = str(user['_id'])
                session['user_id'] = str(user_id)
                return redirect(url_for('myRecipes', user_id=user_id))
            else:
                # invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('signin'))
        else:
            # username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('signin'))

    return render_template('pages/checkuser.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    Allow user to 
    sign up the webapplication
    """
    if request.method == 'POST':
        # check if email already exists in db
        user_email = mongo.db.users.find_one(
            {'email': request.form.get('email').lower()})

        if user_email:
            flash('Email already used')
            return redirect(url_for('signup'))

        register = {
            'name': request.form.get('name').lower(),
            'email': request.form.get('email').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)
        if mongo.db.users.find_one({'email': user_email}) is not None:
            user = mongo.db.users.find_one({'email': user_email})
            user_id = str(user['_id'])
            session['user_id'] = str(user_id)
            flash('Registration Successful') 
            return redirect(url_for('myRecipes', user_id=user_id))

    return render_template('pages/checkuser.html', register=True)


@app.route('/recipes/', methods=['GET', 'POST'])
def recipes():
    """
    Lead to recipes
    """
    recipes = mongo.db.recipes.find()
    return render_template('pages/recipes.html', recipes=recipes)
    

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """
    Lead to recipe info
    """
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('pages/recipe_info.html', recipe=recipe)


@app.route('/myrecipes/<user_id>', methods=['GET', 'POST'])
def myRecipes(user_id):
    """
    Lead to myrecipes page
    """
    # grab the session user's name and email from db
    if session['user_id']:
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        recipes = mongo.db.recipes.find({'user_id': user_id})
        name = user['name']
        return render_template('pages/myrecipes.html', name=name, recipes=recipes)

    return redirect(url_for('pages/signin'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    recipes = mongo.db.recipes.find({'$text': {'$search': query}})
    return render_template('pages/home.html', recipes=recipes)


@app.route('/search', methods=['GET', 'POST'])
def search_recipes():
    query = request.form.get('query')
    recipes = mongo.db.recipes.find({'$text': {'$search': query}})
    return render_template('pages/recipes.html', recipes=recipes)


@app.route('/recipe/add/<user_id>', methods=["GET", "POST"])
def addRecipe(user_id):
    """
    Add a Recipe and
    Takes user back to My Recipes
    """
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    recipe_image = request.form.get('recipe_image')
    print(recipe_image)
    if recipe_image == "":
        image_default = "https://natashaskitchen.com/wp-content/uploads/2012/09/cookbook.jpg"
    else:
        image_default = recipe_image

    if request.method == "POST":
        submit = {
            "user_id":  user_id,
            "name_recipe": request.form.get("recipe"),
            "category": request.form.get("category"),
            "time":request.form.get("time"),
            "yield": request.form.get("yield"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "created_by": user['name'],
            "recipe_image": image_default
        }
        mongo.db.recipes.insert_one(submit)
        flash("Recipe Successfully Added")
        return redirect(url_for("myRecipes", user_id=session['user_id']))

    return render_template("pages/recipe.html", user_id=session['user_id'], add=True )


@app.route('/recipe/edit/<user_id>/<recipe_id>', methods=['GET', 'POST'])
def editRecipe(user_id, recipe_id):
    """
    Edit recipe and 
    Salve the new one
    """
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if request.method == "POST":
        submit = {
            "user_id":  user_id,
            "name_recipe": request.form.get("recipe"),
            "category": request.form.get("category"),
            "time":request.form.get("time"),
            "yield": request.form.get("yield"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "created_by": user['name'],
            "recipe_image": request.form.get('recipe_image')
        }
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("myRecipes", user_id=session['user_id']))

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('pages/recipe.html', 
                            user_id=session['user_id'],    
                            recipe=recipe)


@app.route('/recipe/delete/<recipe_id>')
def deleteRecipe(recipe_id):
    """
    Delete recipe and
    Takes user back to My Recipes
    """
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe Successfully Deleted')
    return redirect(url_for("myRecipes", user_id=session['user_id']))


@app.route('/logout')
def logout():
    """
    Allows the user to log out
    Takes user back to home
    """
    flash('You have been logged out')
    session.clear()
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
