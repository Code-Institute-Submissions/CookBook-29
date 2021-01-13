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
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'name' : request.form.get('name').lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                    session['user'] = request.form.get('name').lower()
                    flash('Welcome {}'.format(
                        request.form.get('name').capitalize()))
                    return redirect(url_for('myRecipes', username=session['user']))

            else:
                #invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('sign'))

        else:
            #username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('signin'))

    return render_template('signin.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
