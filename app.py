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
        existing_email = mongo.db.users.find_one(
            {'email' : request.form.get('email').lower()})

        if existing_email:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_email['password'], request.form.get('password')):
                    session['userEmail'] = existing_email['email'].lower()
                    flash('Welcome {}'.format(
                        existing_email['name'].capitalize()))
                    return redirect(url_for('myRecipes', email=session['userEmail']))

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
        existing_email = mongo.db.users.find_one(
            {'email' : request.form.get('email').lower()})

        if existing_email:
            flash('Email already used')
            return redirect(url_for('signup'))

        register = {
            'name': request.form.get('name').lower(),
            'email': request.form.get('email').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session['user'] = request.form.get('name').lower()
        flash('Registration Successful')
        return redirect(url_for('myRecipes', name=session['user']))

    return render_template('signup.html')


@app.route('/myrecipes/<email>', methods=['GET', 'POST'])
def myRecipes(email):
    # grab the session user's name and email from db
    name = mongo.db.users.find_one(
        {'email': session['userEmail']})['name']

    if session['userEmail']:
        return render_template('myrecipes.html', name=name)

    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
