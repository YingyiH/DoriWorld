# Import Flask,template to python run file
from flask import Flask, render_template, url_for,request, jsonify
from models.score import Score
from models.user import User

# __name__ is the name of the current Python module 
# The app needs to know where it's lacated to set up some paths
app = Flask(__name__)

@app.route('/')
def home():
    score = Score("user.json")
    return render_template('home.html',score=score)
    
@app.route('/user/<string:username>') ## to add an argument to the function
def user(username):
    score = Score("user.json")
    user = score.get_users(username)
    return render_template('user.html',user = user)

@app.route('/user/add', endpoint='create a user', methods = ["POST"])
def add_user():
    # if request.method == 'Post':
        score = Score("user.json")
        user = request.json

        # ERROR CONDITION:
        if ("username" not in user.keys()) or ("user" not in user.keys()):
            return render_template('error.html',error=400),400
        if (score.get_users(user['username'])):
            return render_template('error.html',error=409),409
            
        # OUTPUT
        try:
            username = user['username']
            grades = user["grades"]
            score.add_user(username,grades)
            score.save()
            
            return 'Saved', 200
        except ValueError:
            return render_template('error.html',error=400),400

@app.route('/user/<string:username>/grades/add', endpoint='add a grade', methods = ["POST"])
def add_grade(username):
    if request.method == "POST":
        score = Score("user.json")
        user = score.get_users(username)
        grade = request.json

        # ERROR CONDITION:
        if not user:
            return render_template('error.html',error=404),404
        # OUTPUT:
        try:
            user.add_grade(grade['grade'])
            score.save()
            return 'Saved'
        except ValueError:
            return render_template('error.html',error=400),400

@app.route("/error",methods = ["POST"])
def reror():
    data = request.json
    if("name" not in data.keys()):
        raise ValueError
    else:
        return render_template('error.html',error=data['username'])

# Run the python file
if __name__ == "__main__":
    app.run(debug = True)