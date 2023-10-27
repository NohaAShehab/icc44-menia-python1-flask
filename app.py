from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)

# initialize db instance for this app
db = SQLAlchemy()
# # add db configuration to this app ?
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"
db.init_app(app)


# add new routes to the application
@app.route('/hello')
def hello():
    return "<h1 style='color:green'> Hello world </h1>"


@app.route('/hello/<user>')
def hello_user(user):
    return f"<h1 style='color:green'> Hello {user} </h1>"


users = [
    {"id": 1, "name": "omar", "email": "omar@gmail.com"},
    {"id": 2, "name": "Ahmed", "email": "ahmed@gmail.com"},
    {"id": 3, 'name': "Ali", "email": "ali@gmail.com"}
]


@app.route('/users')
def get_users():
    return users


@app.route("/users/<int:id>", endpoint='user_details')
def get_user(id):
    filtered_users = filter(lambda user: user['id'] == id, users)  # filter object
    filtered_users = list(filtered_users)
    if filtered_users:
        return filtered_users[0]

    return "<h1>  User not found </h1>"


# return with template
@app.route('/landing', endpoint='landingpage')
def land():
    return render_template("landing.html", users=users)


# create route for errors

@app.errorhandler(404)
def not_found(error):
    return render_template('notfound.html')


### assign function to usrl
from views import test_view

app.add_url_rule('/test', view_func=test_view, endpoint='testview')


# models
class Student(db.Model):
    __tablename__ = 'students'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    image= db.Column(db.String)




""" each route --> have endpoint if you didn't specify --> flask will use function name"""
if __name__ == '__main__':
    app.run(debug=True)
