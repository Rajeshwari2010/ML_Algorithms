from flask import Flask,render_template,request
''' 
It creates an interface of flask class,act WSGI as web server gateway interface to interact with web server
'''
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask Course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
