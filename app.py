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
@app.route('/home')
def home():
    recipes = mongo.db.recipes.find()
    return render_template('home.html', recipes=recipes)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {'email' : request.form.get('email')})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                    session['user'] = existing_user['email'].lower()
                    recipes = mongo.db.recipes.find()
                    flash('Welcome {}'.format(
                        existing_user['name'].capitalize()))
                    return redirect(url_for('myRecipes', email=session['user'], recipes=recipes))

            else:
                #invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('signin'))

        else:
            #username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('signin'))

    return render_template('signin.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {'email' : request.form.get('email')})

        if existing_user:
            flash('Email already used')
            return redirect(url_for('signup'))

        register = {
            'name': request.form.get('name').lower(),
            'email': request.form.get('email').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)
        recipes = mongo.db.recipes.find()
        # put the new user into 'session' cookie
        session['user'] = request.form.get('email').lower()
        flash('Registration Successful')
        return redirect(url_for('myRecipes', email=session['user'], recipes=recipes))

    return render_template('signup.html')


@app.route('/myrecipes/<email>', methods=['GET', 'POST'])
def myRecipes(email):
    # grab the session user's name and email from db
    email = mongo.db.users.find_one(
        {'email': session['user']})['email']
    recipes = mongo.db.recipes.find()

    if session['user']:
        return render_template('myrecipes.html', email=session['user'], recipes=recipes)

    return redirect(url_for('signin'))


@app.route('/logout')
def logout():
    # remove user from session cookies
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('signin'))


@app.route('/addrecipe/', methods=["GET", "POST"])
def addRecipe():
    if request.method == "POST":
        recipe = {
            "email_user": session['user'],
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
        return redirect(url_for("myRecipes", email=session['user']))

    return render_template("addrecipe.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
