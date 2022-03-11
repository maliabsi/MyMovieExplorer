"""This is my movie explorer"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace
# pylint: disable=trailing-newlines
# pylint: disable=global-variable-undefined
# pylint: disable=bad-option-value,useless-object-inheritance
# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import random
import os
import flask
from flask_sqlalchemy import SQLAlchemy
import flask
from flask_login import (
    UserMixin,
    LoginManager,
    login_required,
    login_user,
    logout_user,
    current_user,
)
from tmdb import get_movie_data, get_wiki_data

app = flask.Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = "welcome"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __repr__(self):
        return "<User %r" % self.user_name

    def get_username(self):
        return self.user_name

    def get_id(self):
        return self.id


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    curr_username = db.Column(db.String(100))
    ratings = db.Column(db.String(10))
    comments = db.Column(db.String(100))
    movie_id = db.Column(db.Integer)


db.create_all()

# set up a separate route to serve the home.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/diff", methods=["GET", "POST"])
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


favMovies = [637649, 546554, 22803]


@app.route("/index")
@login_required
def get_movie():
    """This functions calls the methods from project1.py and renders it to the home.html"""
    rand = random.choice(favMovies)
    comments = Reviews.query.filter_by(movie_id=rand).all()
    num_comments = len(comments)
    title, tagline, final_genres, img_url, movie_id = get_movie_data(rand)
    wiki_data = get_wiki_data(title)
    return flask.render_template(
        "home.html",
        title=title,
        tagline=tagline,
        genres=final_genres,
        img_url=img_url,
        wiki_data=wiki_data,
        comments=comments,
        rand=rand,
        movie_id=movie_id,
        num_comments=num_comments,
    )


@app.route("/")
def welcome():
    return flask.render_template("welcome.html")


# checks if username exists, if it does then redirects user to index; if it does not exist, user receive flash message and is redirected to signup page
@app.route("/user_login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        data = flask.request.form
        currUser = Users.query.filter_by(
            username=data["curr_username"]
        ).first()  # filters the info from table
        if currUser is None:  # checks if username does not exist
            flask.flash("Username does not exist. Please sign up.")
            return flask.redirect(flask.url_for("signup"))
        else:
            login_user(currUser)
            return flask.redirect(flask.url_for("get_movie"))
    return flask.render_template("login.html")


@app.route("/user_logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("welcome"))


# checks if username already exists, if it does then user receives flash message and user must try different username; if it doesn't exist then user is logged in and redirected to index
@app.route("/user_signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        data = flask.request.form
        newUser = Users(username=data["new_username"])
        userTaken = Users.query.filter_by(username=newUser.username).first()
        if userTaken:
            flask.flash("Username already taken. Try again.")
            return flask.redirect(flask.url_for("signup"))
        db.session.add(newUser)
        db.session.commit()
        return flask.redirect(flask.url_for("get_movie"))
    return flask.render_template("signup.html")


@app.route("/user_reviews", methods=["GET", "POST"])
def reviews():
    if flask.request.method == "POST":
        curr_username = current_user.username
        movie_id = flask.request.form.get("movie_id")
        ratings = flask.request.form.get("rating")
        comments = flask.request.form.get("comment")
        comment = Reviews(
            curr_username=curr_username,
            movie_id=movie_id,
            ratings=ratings,
            comments=comments,
        )
        db.session.add(comment)
        db.session.commit()
    return flask.redirect(flask.url_for("get_movie"))


@bp.route("/getComments", methods=["GET", "POST"])
def get_comments():
    curr_user = current_user.username
    comments = Reviews.query.filter_by(curr_username=curr_user).all()
    list_comments = []
    for c in comments:
        dict_comments = {}
        dict_comments["id"] = c.id
        dict_comments["ratings"] = c.ratings
        dict_comments["comments"] = c.comments
        dict_comments["movie_id"] = c.movie_id
        list_comments.append(dict_comments)
    return flask.jsonify(list_comments)


app.register_blueprint(bp)

app.run(debug=True)
