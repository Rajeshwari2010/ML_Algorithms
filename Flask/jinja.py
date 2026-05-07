from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcom to this page"

    # @app.route("/submit",methods=['GET','POST'])
    # def submit():
    #     if request.method =='POST':
    #         name=request.form['name']
    #         return f"Hello {name}!"
    #     return render_template("form.html")

##variable rule
@app.route("/success/<int:score>")
def success(score):
    result=""
    if score>50 :
        result='PASS'
    else:
        result="FAIL"  

    return render_template('result.html',results=result)    

@app.route("/successor/<int:score>")
def successor(score):
    result=""
    if score>50 :
        result='PASS'
    else:
        result="FAIL"  

    exp={'score':score,'result':result}   

    return render_template('result1.html',results=exp)   


@app.route("/successif/<int:score>")
def successif(score):  
    return render_template('result2.html',results=score)  


## redirecting to different page

@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+c+maths+data_science)/4

    else:
        return render_template('getresult.html')    

    return redirect(url_for('successor',score=total_score))   



if __name__ == "__main__":
    app.run(debug=True)

        