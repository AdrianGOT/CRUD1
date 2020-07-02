from app import app, db
from .schemas import Users, Info
from flask import render_template, request, redirect, url_for,session,escape
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
from sqlalchemy import exc

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods = ["GET","POST"])
def home():
    if "username" in session:
        n = session["username"]
        if request.method == "POST":
            x = datetime.datetime.now()
            time = x.strftime("%X")
            new_data = Info(name = request.form["name"],usuario = n ,lastName = request.form["lastName"], email = request.form["email"], time = time )
            db.session.add(new_data)
            
            try:
                db.session.commit()
            except exc.IntegrityError:
                db.session.rollback()
            
        inf = Info.query.all()
        return render_template('home.html', title = "Home", datos = inf, name = n)

    else:
        return render_template('first.html', title = "...")

def igualdad(pas1,pas2):
    if pas1 == pas2:
        return True
    else:
        return False

@app.route('/signIn', methods = ["GET","POST"])
def signIn():
    if request.method == "POST":
        username1 = request.form["username"]
        password1 = request.form["password"]
        password2 = request.form["password1"]

        if igualdad(password2,password1):
            hashed_pw = generate_password_hash(password1,method="sha256")
            new_user = Users(username = username1 , password = hashed_pw)
            db.session.add(new_user)
            try:
                db.session.commit()
            except exc.IntegrityError:
                db.session.rollback()
            
            session["username"] = username1

            return redirect(url_for('home'))
        else:
            #incluir el mensaje flash
            return render_template("sign.html",title = "aml" ) 


    return render_template("sign.html",title = "Registro" )

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        usuario = Users.query.filter_by(username = request.form["username"]).first()
        if usuario and check_password_hash(usuario.password , request.form["password"]):
            session["username"] = usuario.username

            return redirect(url_for('home')) 

        else:
            return redirect(url_for('login'))

    return render_template("login.html", title = "Iniciar sesión")

@app.route('/logout')
def logout():
    session.pop("username",None)
    return redirect(url_for('home'))


@app.route('/delete/<string:name>')
def delete(name):
    user = Info.query.filter_by(name = name).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/editar/<string:name>', methods = ["GET","POST"])
def editar(name):
    user = Info.query.filter_by(name = name).first()
    n = session["username"]

    if request.method == "POST":
        if request.form["name"] != "" and request.form["lastName"] !="" and request.form["correo"] != "": 
            
            user.name = request.form["name"]
            user.lastName = request.form["lastName"]    
            user.email = request.form["correo"]

            x = datetime.datetime.now()
            time = x.strftime("%X")
            user.time = time
            db.session.commit()
            return redirect(url_for('home'))


    return render_template('edit.html', person = user,name =n )     
    