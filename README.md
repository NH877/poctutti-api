# poctutti-api

Currently using Python, Flask, SQLAlchemy and Marshmallow.

### Entities

![Simple DER](https://i.imgur.com/WZOHpzG.png)

Product, Sales and Stores. 

### How to run it locally

```
python3 app.py
or
gunicorn --chdir app app:app
```
_I'm using --chdir to change the folder, the first 'app' is the folder, 
the second 'app' is the name of the file and the third one is the type._

### How to deploy it to Heroku
1- Create an app and a database for that app.  
2- Update the DATABASE_URI constant in the `config.py` file with your database credentials. Remember to use `postgresql://` instead of `postgres://`.  
3- Download the Heroku CLI and:   
- Login with your account `heroku login`
- Add the remote for your existing app `heroku git:remote -a example-app`
- Deploy your branch to Heroku `git push heroku main`  
That will give you the URL and it will be ready to use. There is a Postman collection with examples.
