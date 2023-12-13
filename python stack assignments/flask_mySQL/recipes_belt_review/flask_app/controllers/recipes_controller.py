from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.recipes_model import Recipe
from flask_app.models.user_model import User

@app.route("/recipes/new")
def create_recipe():
    if 'user_id' in session:
        return render_template("create_new_recipe.html")
    return redirect('/')

@app.route('/recipes/add',methods=["POST"])
def add_recipe():
    print(request.form)
    Recipe.create_recipy(request.form)
    return redirect("/recipes")
@app.route('/recipes/<int:id>/destroy/')
def delete_recipe(id):
    if 'user_id' in session:
        data={'id':id}
        Recipe.delete(data)
    return redirect('/recipes')
@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' in session:
        one_recipe=Recipe.get_by_id({'id':id})
        return render_template("edit_recipe.html", recipe=one_recipe)
    return redirect('/')
@app.route('/recipes/<int:id>/update' ,methods=['POST'])
def update_recipe(id):
    print(request.form)
    Recipe.edit_recipe(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def one_recipe(id):
    if 'user_id' in session:
        one_recipe=Recipe.get_by_id({'id':id})
        poster=User.get_by_id({'id':one_recipe.user_id})
        return render_template('one.html',recipe=one_recipe,user=poster)
    return redirect('/')