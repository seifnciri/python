from flask import Flask,render_template,request,redirect
from users import USER
app = Flask(__name__)

@app.route('/users')
def show_users():
    USER.show_users()
    return render_template("all_users.html",u=USER.show_users())

@app.route('/process',methods=['POST'])
def create_users():
    USER.creat(request.form)
    print('++++++++',request.form)
    return redirect('/users')
@app.route('/users/new')
def rend():
    return render_template("add_a_new_user.html")

@app.route('/users/<int:id>')
def user_info(id):
    data={'id':id}
    return render_template("show_one.html",y=USER.show_one(data))



if __name__ == '__main__':
    app.run(debug=True)