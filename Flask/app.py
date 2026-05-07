from flask import Flask
''' 
It creates an interface of flask class,act WSGI as web server gateway interface to interact with web server
'''
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course.This will be an amzing courses,I love it!" 

@app.route("/index")
def index():
    return "This is the Index page" 

if __name__ == "__main__":
    app.run(debug=True)
