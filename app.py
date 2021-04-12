import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    """ Landing page with search index for all recipes """
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


@app.route("/get_recipes")
def get_recipes():
    """ Page showing all recipes. Generates a list from the database """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search function that searches the database for text
        in the recipe titles, ingredients and tags """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """ Takes a recipe ID and shows a page displaying
        all recipe details for a user to follow. Finds
        a recipe in the database by its ID """
    show = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    show_comments = list(mongo.db.comments.find({"recipe_id": recipe_id}))
    return render_template("recipe.html", recipe=show, comments=show_comments)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Registration function that checks if a user already
        exists and adds a user to the databse so they are registered."""
    if request.method == "POST":
        # check is username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Oops! Username already exists")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thank you for your registration")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Checks the user exists in the database and the password matches
        the hased password or redirects to log in page."""
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Oops! Incorrect username and/or password used.")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Oops! Incorrect username and/or password used.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Renders the users profile page which shows a list of
        the recipes that they have created."""
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    recipes = list(mongo.db.recipes.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Logs a user out by clearing the session """
    # remove user from session cookies
    flash("You have logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """ Allows only a registered user to add a recipe. If they are
        not registered or logged in they are redirected to the
        registration form."""
    try:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if session["user"]:

            if request.method == "POST":
                recipe = {
                    "recipe_name": request.form.get("recipe_name"),
                    "ingredients": request.form.get("ingredients"),
                    "method": request.form.get("method"),
                    "prep_time": request.form.get("prep_time"),
                    "tags": request.form.get("tags").split(", "),
                    "image_url": request.form.get("image_url"),
                    "created_by": session["user"]
                }
                mongo.db.recipes.insert_one(recipe)
                flash("Recipe successfully created")
                return redirect(url_for("get_recipes"))
            return render_template("add_recipe.html", username=username)

    except:
        flash("Please register or log in to start adding recipes")
        return render_template("register.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:

        recipe_to_be_updated = mongo.db.recipes.find_one_or_404(
                {"_id": ObjectId(recipe_id)})

        if session["user"] == recipe_to_be_updated["created_by"]:

            if request.method == "POST":
                submit = {
                    "recipe_name": request.form.get("recipe_name"),
                    "ingredients": request.form.get("ingredients"),
                    "method": request.form.get("method"),
                    "prep_time": request.form.get("prep_time"),
                    "tags": request.form.get("tags").split(", "),
                    "image_url": request.form.get("image_url"),
                    "created_by": session["user"]
                }
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
                flash("Recipe successfully updated")
                return redirect(url_for('recipe', recipe_id=recipe_id))

        return render_template(
            "edit_recipe.html", recipe=recipe_to_be_updated, username=username)

    return render_template("register.html")


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """ Removes a recipe from the database and notifies the user."""
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("profile", username=username))


# publish comment and storing in own comments collection in DB
@app.route("/add_comment/<r_id>", methods=["GET", "POST"])
def add_comment(r_id):
    """ Allows a registered user to add a comment to a recipe by using the recipe_id. """
    if "user" in session:
        if request.method == "POST":
            username = mongo.db.users.find_one(
                        {"username": session["user"]})["username"]
            # insert the comment to the database
            comment = {
                'recipe_id': r_id,
                'created_by': username,
                'comment': request.form.get("comment"),
                'posted': datetime.now(tz=None).strftime("%d-%b-%Y (%H:%M)")
            }
            mongo.db.comments.insert_one(comment)
            flash("Thank you, comment successfully published")
            return redirect(url_for("recipe", recipe_id=r_id))

    flash("Please log in to add comments")
    return redirect(url_for("login"))


@app.errorhandler(404)
def handle_404(exception):
    """ Error function if a link is no longer usable """
    return render_template("404.html", exception=exception)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

