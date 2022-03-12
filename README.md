# milestone3-mabsi2

## Project Description

My Movie Explorer utilizes the TMDB API and MediaWiki API in order to dynamically fetch specified attributes and display them on a web application. It also provides users with a link to the movie's corresponding Wikipedia page for additional information! Futher, this webpage utilizes databases and flask-login in order to maintain user sessions, allow users to login / signup, navigate through the website and leave comments when desired.

## Run Locally

If someone were to want to run this app, he/she would need to obtain unique keys (specified under installation requirements) and create a .env file to place the key in. He/She would also need to download the necessary libraries which are listed later.

* pip3 install flask
* pip3 install requests
* pip3 install python-dotenv

* pip3 install psycopg2-binary
* pip3 install flask_sqlalchemy
* pip3 install flask_login

These are the keys needed to run My Movie Explorer:
* tmdb_key is a unique api key that is used to dynamically fetch movie information.
* DATABASE_URL is used to connect to backend server for heroku postgresql database.
* SECRET_KEY allows flash notifications to be sent to user.

## Setup

* Create account in order to 
* Create .env file and add unique tmdb_key as: tmdb_key = "users api_key"
* add database url as: export DATABASE_URL="user's database_url"
* add secret_key as: SECRET_KEY="user's secret key"
* Now create a database:
    * Run 'git init' and 'heroku create' to set up Heroku app and git repository
    * Run 'heroku addons:create heroku-postgresql:hobby-dev
    * Run 'heroku config' to get database url (copy and paste it into .env file and make sure to change 'POSTGRES' to 'POSTGRESQL' in the url)

## PostgreSQL Setup

* brew install postgresql
* brew services start postgresql
* psql -h localhost  # this is just to test out that postgresql is installed okay - type "\q" to quit
* pip3 install psycopg2-binary
* pip3 install Flask-SQLAlchemy==2.1

## React Setup
* brew update
* brew install node
* pip3 install npm
* npm install react

## Run Locally (milestone 3)
* npm ci
* npm run build
* python3 app.py


## Heroku Setup

* /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)  # install Homebrew
* brew tap heroku/brew && brew install heroku  # install Heroku CLI

## Flask Framework

The flask framework made building this web application simple because of its built in tools and methods such as render_template to connect to the html file. 

## Imported Libraries

1.	I imported random so that every time the user refreshes the page, a movie appears unsystematically.
2.	I had to import the get_movie_data method from a separate file to fetch the movie information for the app. 
3.	The os module was used to interact with my .env file to ensure my API key was kept private.
4.	Flask was imported in order to provide a framework for the web application and to handle app routing.
5.	I imported operator to effectively fetch the genre data.
6.	I imported requests and by using specified parameters and the base_url, the library was able to get the request and convert the response to JSON. 
7.	I had to import load_dotenv and find_dotenv from dotenv in order to locate the .env file then read and make the environment variable accessible.
8. I also imported SQLAlchemy from flask_sqlalchemy in order to make the process simple when working with the database and setting up database models.
9. I imported flask-login built in classes and methods such as UserMixin, LoginManager, login_required, login_user, logout_user,
    current_user in order to handle logging in / logging out and to keep track of user sessions.
10. I also had to import useState and useEffect from 'react' in order to allow state variables and the use of side effects in the components.
    
## Methods

In order to dynamically fetch and display the movie data and wikipedia links on my webpage, I used two functions: get_movie_data and get_wiki_data
  * get_movie_data: 
    * This function works by passing in a parameter (movie_id), which is a randomized movie ID from the list in app.py
    * The file is able to access the movie data using the base_url with the specified movie_id and parameter(api_key) from the TMDB database.
    * Then using requests, the program gets the http response and configures it into JSON.
    * The method then takes the block of JSON data and filters the info to get the wanted information by defining the movies' title, tagline and genre(s).

  * get_wiki_data:
    * This function works similarly to the function above, yet it calls the Wiki API rather than TMDB.
    * It functions by passing in a movie title and uses its own base_url and parameters to get JSON response.
    * Then, it filters the JSON response so that the requested information can be returned, which in this case is the Wikipedia URL for each movie.

  * delete_comment:
    * This function is used to delete reviews of the current user on the UI only.

  * save_changes:
    * This function is used to delete reviews of the current user from the actual database.

## How Login Works

When a user first clicks on the link, he/she is directed to a welcome page which includes two hyperlinks where he/she is expected to either choose to login or signup. Once the user enters a username, the database checks if the username is existing through the login method. If it is not yet in the database, the user is redirected to a signup page, using routing, where the username can be registered. Once the user is successfully logged in, he/she is able to access all of the movie data and is also able to leave a review that includes a rating and comment through the reviews method.
  
## Database

For milestone 2, I created two tables, one for the user and one for reviews. The user class was used to store existing usernames while the reviews class was used to store reviews such as ratings and comments made by existing users.

## Questions

1. What are at least 3 technical issues you encountered with your project milestone? How did you fix them? 
  
    * One issue I had while working on this project was figuring out how to remove a review from the list of the current user.
      * In order to fix this issue, I referenced a code snippet found on www.robinwieruch.de.
   
    * Another issue I encountered was that my alert that notifies users when their changes have been saved kept popping up before making any changes / deleting.
       * To fix this issue, I included a mapping function within the onClick () => save_changes(review). Without doing this, my alert would pop up whenever the page loaded instead of when the save changes button was clicked.

    * The third issue was figuring out how to save the changes to the database when a user edits / deletes his/her comments on the webpage.
       * To fix this solution, I referenced the StackOverflow link that John provided under the "fetch" section.
  
2. What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?
    
    * The hardest part of the project across all milestones was figuring out how to make the users' reviews editable.
    
    * The most useful thing I learned across all milestones to me was learning how to create and interact with a database in addition to learning how to dynamically fetch data.
   
## Heroku

Once my movie explorer was complete, I used Heroku to deploy my web app to the server and successfully use my API key while keeping it private. Without using Heroku, no one would be able to access my app since it would only be saved on the local server.

### Heroku URL (milestone 2): 
https://pacific-shelf-05398.herokuapp.com/ 
