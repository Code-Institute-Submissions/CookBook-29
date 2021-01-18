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
    if request.method == 'POST':
        # check if email already exists in db
        user = mongo.db.users.find_one(
            {'email': request.form.get('email').lower()})

        if user:
            flash('Email already used')
            return redirect(url_for('signup'))

        register = {
            'name': request.form.get('name').lower(),
            'email': request.form.get('email').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)
        if mongo.db.users.find_one({'email': user}) is not None:
            user_id = str(user['_id'])
            session['user_id'] = str(user_id)
            flash('Registration Successful')
            return redirect(url_for('myRecipes', user_id=user_id))

    return render_template('pages/checkuser.html', register=True)



@app.route('/myrecipes/<user_id>', methods=['GET', 'POST'])
def myRecipes(user_id):
    # grab the session user's name and email from db
    if session['user_id']:
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        recipes = mongo.db.recipes.find({'user_id': user_id})
        if recipes:
            name = user['name']
            count_recipes = recipes.count()

        return render_template('pages/myrecipes.html', name=name, recipes=recipes, count_recipes=count_recipes)

    return redirect(url_for('pages/signin'))


@app.route('/logout')
def logout():
    """
    Allows the user to log out
    Takes user back to home
    """
    flash('You have been logged out')
    session.clear()
    return redirect(url_for('signin'))


@app.route('/addrecipe/', methods=["GET", "POST"])
def addRecipe():
    if request.method == "POST":
        recipe = {
            "user_id": session['user_id'],
            "name_recipe": request.form.get("recipe"),
            "category": request.form.get("category"),
            "time":request.form.get("time"),
            "yield": request.form.get("yield"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps")
        }
        mongo.db.recipes.insert_one(recipe)
        print("Recipe Successfully Added")
        flash("Recipe Successfully Added")
        return redirect(url_for("myRecipes", user_id=session['user_id']))

    return render_template("pages/addrecipe.html", user_id=session['user_id'])


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
