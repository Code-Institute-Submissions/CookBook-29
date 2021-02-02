# **CookBook**

![multi platform](wireframes/multiplatform.png)

## **Project Goal**

This is a web application that implements the principles of the C.R.U.D. cycle are defined as CREATE, READ/RETRIEVE, UPDATE, and DELETE, the application allows users to add recipes to the panel, update it and eventually delete them. A user needs to registrate to be able to add recipes.
Happy Code! 👨‍💻 Happy days!

  ## Table of contents 
* [UX](#ux)🎯
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)🎨
        * [Fonts](#fonts)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)👨‍🔧
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)🤖
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)👀
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)
    
### **User Goals**

* This web application has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a clear dashboard where I can see all the different recipes I have created. 
* I want to have a profile for me where I can create, update and delete recipes. 
* I want to see the recipes even if I don't have registered.
* The web application has to be user friendly.
* Visually appealing web application.

### **User Stories**

* As a user, I would like to be able to register for the web application so I can have my personal environment.
* As a user, I want to login after I created an account and see my previous inserted information.
* As a user, I want a home dashboard page that shows the latest recipes added.
* As a user, I want to see the recipes without log in.
* As a user, I want to be able to search recipes.
* As a user, I want the web application to be easy to use. 
* As a user, I want the process to add / edit / delete info to be easy.

### **Site owners Goals**
* To have an appealing web application where recipes can be shared between users.
* To have a great functionality so the user feels like this web application helps them in their day-to-day life. 
* To make the web application where people can share experience about their recipes.

### **User Requirements and Expectations**

#### Requirements

* Easy to navigate by using the few buttons.
* Appealing dashboard with a functional overview.
* Easy way to add a recipe to the dashboard.
* Ability to edit and delete existing recipes.

#### Expectations

* When you have multiple recipes, it should be easy to navigate between them.
* To have a dashboard where all the necessary information is visible.
* It should be easy to add another recipe.

### **Design Choices**🎨

I made a research in [Jenn David Design](https://jenndavid.com/colors-that-influence-food-sales-infographic/ "jenndavid.com") website, where I found that a mix of red, orange and light brown would be a nice look for a web application that present recipes. Then I have used [Coolors](https://coolors.co/ "Coolors.co") to come up with a pallete of colors that I already had chosen.

![palette](https://github.com/alychinque/CookBook/blob/master/wireframes/palette.png)

#### Fonts

I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") in order to find appropriate fonts for my web application.
For the titles and subtitles, I have used the font [Redressed](https://fonts.google.com/specimen/Redressed "Redressed") 
and for the main text I have used [Bodoni Moda](https://fonts.google.com/specimen/Bodoni+Moda "Bodoni Moda") and for the brand I have used [Patua One](https://fonts.google.com/specimen/Patua+One).

#### Structure

I have chosen to use [Boootstrap](https://getbootstrap.com/) to create an overall structure for my website. 
Bootstrap provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page. 

## **Wireframes and Flowcharts**👨‍🔧

### **Wireframes**
I used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website. 

You can find my wireframes below:

#### Desktop Wireframes
* [Wireframes](wireframes/desktop.pdf)

#### Mobile Wireframes
* [Wireframes](wireframes/mobile.pdf)

### **Flowcharts**

I have decided to make a flowchart to completely understand each step of the process. 
I have used [Draw.io](https://draw.io/) to make this flowchart which you can view below: 

* [Flowchart](wireframes/flowchart.pdf)

### **Database Structure**

I have created an database entities in [Draw.io](https://draw.io/)
* [Database](wireframes/data.png)

I also have used MongoDB to set up the database for this project with the following collections: 

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
name     | String
email    | String
password | String

#### **Recipe:**

Key             | Value
----------------|-----------
_id             | ObjectId
user_id         | String
name            | String
category        | String
time            | String
yield           | String
ingredients     | String
step1           | String
step2           | String
step3           | String


## **Features**🤖

### **Existing Features**

* Registration functionality
* Sign-In and Out functionality
* Add multiple recipes per user 
* CRUD Functions:
    * Create: possibility to add various recipes and reviews.
    * Read: dashboard where you can view the recipes and its reviews.
    * Update: possibility to update the recipes.
    * Delete: possibility to delete the recipes.
* Search recipes.

### **Features to be implemented**

* Have a fucionality to insert images within the recipes.
* Have a more extensive user profile with, profile image, preferences and email to which you can send updates, newsletters etc.
* Have a 'forget password' functionality.
* Include a confirm password to make sure the user has chosen the password he/she wanted. 
* Have a functionality to rate the recipes.

## **Technologies used**👀

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### **Libraries and Frameworks**

* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)

### **Tools**
* [Git](https://git-scm.com/)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)


## **Testing**

### **Registration**

#### User story: As a user, I would like to be able to register for the website so I can add my recipes

* **Plan**  
I want to create a account to be able to add, read, update and delete recipes.

* **Implementation**  
I created a form where the user can add their name, email, and choose a password. 
I have used the pattern attribute to only allow certain characters for the name, email, and password. 
Correct feedback will be displayed whenever the user doesn't meet the pattern critera. 
Before creating the new account, I will check in the database if the email already exists. 
If so, correct feedback will be displayed to the user so he can choose another username. 
Password will be stored with the help of the password generate hash so it is stored safely.
After the registration was succesfull, the user will be redirected to the My Recipes page to add their first recipe.
In case the user wrongfully clicked on register instead of sign-in, a link to the sign-in page is provided so the user doesn't have to go back. 

I have used a variable (register) to make the difference between the register and sign-in form.
When register is equal to True, I added the span which explains the requested format.
By implementing this, I have managed to merge the register and sign-in form into 1 form which simplifies my code. 


* **Test**  
I have tried to create an account with an already existing email. Correct feedback is displayed.
Whenever I didn't meet the pattern criteria, the correct feedback was displayed, explaining which charachters etc are allowed. 
User acccount is created whenever all criteria was met and user is being redirect to My Recipes.


* **Result**  
Registration form is working as planned and user information is stored safely in the mongodb Users collection.
Feedback provided stands out nicely to inform the user. 
Redirection to blank My Recipe works as well as planned so the user can choose to add its recipe right away. 
Tested the registration on various browers and devices and the form is responsive and userfriendly. 

* **Verdict**
The test has passed all the criteria and works like planned.


### **Sign In**

#### User story: As a user, I want to login after I created an account and see my previous inserted information.

* **Plan**  
My plan is to create a login form where the user can fill in its email and password.
After signing in, the user will be redirected to the My Recipe page where the user can see the previously inserted recipes.
In case the user doesn't have any Recipe added to its profile, a message will be displayed with "no recipes added" and a link to add first recipe.

* **Implementation**  
I created a form where the user can fill in its email and password which will be verified with the information stored in the database. 
When the wrong information is being filled in, the correct feedback will be provided to the user. 
In case the user wrongfully clicked on sign-in instead of register, a link to the register page is provided so the user doesn't have to go back. 

* **Test**  
Signing in with the correct email and password works as planned and the correct page will be displayed. 
When the user fills in the wrong email and/or password, the same message is being displayed on the screen. 
Also here the feedback message didn't stand out well enough so I have changed the color to red. 
Redirecting to register page and 'back to homepage' link works as well. 

* **Result**  
Sign-in form is working as planned and the input is being verified correctly with the stored information of the database.
Redirection to the correct page works as well as planned so the user can either add a recipe on My Recipes page or view its previously inserted recipes.
Tested the sign-in form on various browers and devices and the form is responsive and userfriendly. 
Feedback provided to the user stands out nicely. 

* **Verdict**    
The test has passed all the criteria and works like planned.


#### User story: As a user, I want a home dashboard page that shows the latest recipes added.

* **Plan**
My plan was create a home page that shows the latest recipes added, even for user that are not subscribe, they can have access to the home page
and they can see the recipes.

* **Implementation** 
I created a panel with the last six recipes added, I used a for reverse to get the recipes backwords.

* **Test** 
As planned every user with credentials or not can have access to the recipes.
 
* **Result**  
It works just fine and show the user the last six recipes as planned.
 
* **Verdict**    
The test has passed all the criteria and works like planned.


#### User story: As a user, I want to be able to search recipes.

* **Plan**
The plan is create a search bar where users can search recipes by nome of the recipe or ingredients.

* **Implementation** 
First I added a search bar to home and recipes pages, then I created indexes to search in mongo db so that user can search by name of the recipe or ingredients.
Then I created two functions in app.py, one for for search in the home page and another to search in the recipes page.

* **Test** 
I have testing the search functionality with empty field, with a wrong word, and with a word in the database and all response was correct.
 
* **Result** 
The result was satisfactory it shows the correct output depends on the input.
 
* **Verdict**
The test has passed all the criteria and works like planned.


#### User story: As a user, I want the web application to be easy to use. 

* **Plan**
The plan is create an application user friendly, where the user can find everything easily. Also an application responsive.

* **Implementation** 
I create a home page with a panel showing the last six recipes. The user can easily find a navbar where they can sign in, sign up or chech the whole page with recipes. 
If the user sign in they can add a recipe and after that edit or delete it easily. also they can logout.

* **Test** 
Every panel loads well and the experience is good and smooth.
 
* **Result** 
The result is good, it works well through different devices.
 
* **Verdict**
The test has passed all the criteria and works like planned.
 
 
### Add
 
#### User story: As a user, I want the process to add / edit / delete info to be easy.

* **Plan**
The plan is once the user gain access to the application they can add a recipe.

* **Implementation** 
In the first access the user will be presented with a message saying "No recipes Added" and under that "Add a recipe click here" and by clicking on there it will lead you to the recipe/add page. If the user already have recipes added they can access the recipe/add page by clicking on the navigation bar.
Once in the recipe/add page the user will see a form with different fields such as; name of the recipe, category, ingredients, steps, and etc.
The user can a add a picture by adding a URL if they do not add a picture it automaticaly adds a default picture.

* **Test** 
I added multiples recipes from different users. 
 
* **Result** 
The result is good, I can add recipes that are stored in mongo db.

* **Verdict**
The test has passed all the criteria and works like planned.


### Edit
 
#### User story: As a user, I want the process to add / edit / delete info to be easy.

* **Plan**
The plan is once the user add a recipe, they are able to edit it if they want.

* **Implementation** 
I used the same form that I use to add a recipe, I just add some ifs in case of it be add function or edit in order to differentiate. Once the user have a recipe added they can edit it. In the page My Recipes there is a edit button to each recipe. 

* **Test** 
I edit different recipes from different accounts.
 
* **Result** 
The result is good, I can edit my own recipes and then store the new one in mongo db.

* **Verdict**
The test has passed all the criteria and works like planned.


### Delete
 
#### User story: As a user, I want the process to add / edit / delete info to be easy.

* **Plan**
The plan is to delete any recipe that the user added previously.

* **Implementation** 
In the page My Recipes there is a delete button to each recipe. The user can delete any recipe that they had added. The function will removes the recipe from the database mongo db.

* **Test** 
I delete different recipes from different accounts.
 
* **Result** 
The result is good, I can delete my own recipes and then store them from the database in mongo db.

* **Verdict**
The test has passed all the criteria and works like planned.


### Logout

* **Plan**
The plan is to logout of an account.

* **Implementation** 
Once the user is logged in they can logout just clicking on the logout up in the navigation bar.

* **Test** 
I logout from different accounts.
 
* **Result** 
The result is good, I can logout of the application.

* **Verdict**
The test has passed all the criteria and works like planned.


## **Bugs**

### **Add an image as default**

* **Bug**  
When the user is adding a new recipe and they do not have a URL of the recipe image to add, it would break the style because a small default picture would be displayed instead. 

* **Fix**
I created a statement inside the addRecipe function that checks if the field Recipe Image is empty, if so it adds a default URL to a variable called recipe_image and this variable is assigned to the dictionary that will be sent to the database mongoDB. I also include this statement to the editRecipe function in case of the user edit a recipe and delete the URL of the image.

* **Verdict**
Now an image default is correctly added and displayed.


### **Materialize**

* **Bug**  
 It is not a properly bug, but it is a bit trick to get things in place.

* **Fix**
After some days struggling to get things in place, my alternative was switch to bootstrap which for me was a better option.

* **Verdict**
Now everything is in place working responsively.


## **Deployment**

### Local Deployment

I have created the CockBook project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/alychinque/CookBook.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/alychinque/CookBook/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called Recipes
    * Set up the following collection: users
    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a [Password Generator](https://passwordsgenerator.net/) in order to have a secure secret key. 
    I personlly recommend a length of 24 characters and exclude Symbols.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
    
### To deploy your project on Heroku, use the following steps: 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 

## **Credits**

* A big thanks to my mentor Simen [Eventyret](https://github.com/Eventyret)
* A big thanks to [Stackoverflow](https://stackoverflow.com/)
