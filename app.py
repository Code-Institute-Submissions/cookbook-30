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
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    show = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    show_comments = list(mongo.db.comments.find({"recipe_id": recipe_id}))
    return render_template("recipe.html",
                            recipe=show, comments=show_comments)


@app.route("/register", methods = ["GET", "POST"])
def register():
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


@app.route("/login", methods = ["GET", "POST"])
def login():
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


@app.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username):
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
    # remove user from session cookies
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
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
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "prep_time": request.form.get("prep_time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("get_recipes"))


# publish comment and storing in own comments collection in DB
@app.route("/add_comment", methods=["GET", "POST"])
def add_comment():
    try:
        if request.method == "POST":

            if session["user"]:

                username = mongo.db.users.find_one(
                    {"username": session["user"]})["username"]

                r_id = request.args.get("recipe_id")

                recipe_comment = mongo.db.recipes.find_one(
                                    {"_id": ObjectId(r_id)})

                # insert the comment to the database
                comment = {
                    'recipe_id': r_id,
                    'created_by': session["user"],
                    'comment': request.form.get("comment"),
                    'posted': datetime.now(tz=None).strftime("%d-%b-%Y (%H:%M)")
                }
                mongo.db.comments.insert_one(comment)
                flash("Thank you, comment successfully published")
                mongo.db.recipes.find_one({"_id": ObjectId(r_id)})
                return render_template(
                            "recipe.html", username=username,
                            comment=comment, recipe=r_id)

    except:
        flash("Please register or log in to add comments")
        return render_template("register.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
