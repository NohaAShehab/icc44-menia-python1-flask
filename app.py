from flask import  Flask
# create the app
app = Flask(__name__)

# add new routes to the application
@app.route('/hello')
def hello():
    return  "<h1 style='color:green'> Hello world </h1>"


@app.route('/hello/<user>')
def hello_user(user):
    return f"<h1 style='color:green'> Hello {user} </h1>"



users = [
    {"id":1, "name":"omar", "email":"omar@gmail.com"},
    {"id":2 , "name":"Ahmed", "email": "ahmed@gmail.com"},
    {"id":3, 'name':"Ali", "email":"ali@gmail.com"}
]


@app.route('/users')
def get_users():
    return users


@app.route("/users/<int:id>")
def get_user(id):
    filtered_users = filter(lambda user: user['id']==id, users) # filter object
    filtered_users= list(filtered_users)
    if filtered_users:
        return  filtered_users[0]

    return  "<h1>  User not found </h1>"



if __name__=='__main__':
    app.run(debug=True)