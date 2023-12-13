from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def display_8():
    return render_template("index.html")
@app.route('/<int:numb>')
def display_one_param(numb):
    return render_template("index_2.html",x=numb)
@app.route('/<int:numb_line>/<int:numb_row>')
def display_two_param(numb_line,numb_row):
    return render_template("index_3.html",y=numb_line,x=numb_row)
@app.route('/<int:numb_line>/<int:numb_row>/<string:color1>/<string:color2>')
def display_four_param(numb_line,numb_row,color1,color2):
    return render_template("index_4.html",y=numb_line,x=numb_row,color1=color1,color2=color2)

if __name__ == '__main__':
    app.run(debug=True)