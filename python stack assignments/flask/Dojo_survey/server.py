from flask import Flask,render_template, request, redirect,session 
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/process', methods=["POST"])
def process():
    session['name_proccess']=request.form['Name']
    session['location_process']=request.form['Location']
    session['Language_process']=request.form['Language']
    session['comment_process']=request.form['comment']
    return redirect("/")

@app.route('/result')
def create_user():
    return render_template("display.html",name=session['name_proccess'],location=session['Language_process']
    ,Language=session['Language_process'],comment=session['comment_process'])


if __name__ == '__main__':
    app.run(debug=True)