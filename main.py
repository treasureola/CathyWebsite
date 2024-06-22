import sqlite3
from flask import Flask, session, render_template, redirect, request
from waitress import serve
from gevent.pywsgi import WSGIServer
from wsgiref.simple_server import make_server
app = Flask(__name__)
app.secret_key = "GODISGOOD"

####################################################
#                   Functions/Variables            #
####################################################
    
####################################################
#                   HOME                          #
####################################################
@app.route('/')
def home():
    connection = sqlite3.connect("Database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if not session.get("email"):
        return render_template('homeNotLoggedIn.html')
    return render_template('homeLoggedIn.html')

####################################################
#                   PRODUCT                        #
####################################################
@app.route('/products')
def products():
    connection = sqlite3.connect("Database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return render_template('product.html', products = data)

####################################################
#        ADD TO CART and PLACE ORDER               #
####################################################
@app.route('/addCart', methods = ['GET', 'POST'])
def addCart():
    if request.method == 'POST':
        connection = sqlite3.connect("Database.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        # if not session.get("email"):
        #     return render_template(email = session.get("email"))
        if not session.get("cart"):
            session['cart'] = {}
        id = request.form["id"]
        cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
        data = cursor.fetchone()
        if id not in session['cart'].keys(): 
            session['cart'][id] = 1
            print(session['cart'])
            cursor.execute("INSERT INTO cart(cp_email, cp_name, cp_price, cp_id, cp_quantity) VALUES (?, ?, ?, ?, ?)", (session.get("email"), data["p_name"], data["price"], id, 1, ))
            print(11111111111111)
            connection.commit()
            print(333333333)
        else:
            print(2222222222222)
            session['cart'][id] += 1 
            cursor.execute("UPDATE cart SET cp_quantity = ? WHERE cp_email = ? AND cp_id = ?", (session['cart'][id], session.get("email"), id, ))
            connection.commit()
    return redirect(request.referrer, email=session.get("email"))

@app.route('/viewCart')
def viewCart():
    connection = sqlite3.connect("Database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if not session.get("email"):
        redirect('/')
    cursor.execute("SELECT * FROM cart WHERE cp_email = ?", (session.get("email"), ))
    data = cursor.fetchall()
    return render_template("viewCart.html", result = data)

@app.route('/clearCart')
def clearCart():
    connection = sqlite3.connect("Database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if not session.get("email"):
        return redirect('/')
    cursor.execute("DELETE FROM cart WHERE cp_email = ?", (session.get("email"), ))
    session['cart'] = {}
    print(session['cart'])
    connection.commit()
    return redirect(request.referrer)

@app.route('/deleteCart', methods=['GET', 'POST'])
def deleteCart():
    if request.method == 'POST':
        connection = sqlite3.connect("Database.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        if not session.get("email"):
            return redirect('/')
        id = request.form["id"]
        # print(session['cart'])
        session['cart'].pop(id)
        # try:
        #     session['cart'].pop(id)
        # except:
        #     print("key no in dict")
        cursor.execute("DELETE FROM cart where cp_id = ? AND cp_email = ?", (id, session.get("email")))
        connection.commit()
        # connection.close()
    return redirect(request.referrer)
    
####################################################
#                   LOGIN/LOGOUT                   #
####################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connection = sqlite3.connect("Database.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        email = request.form["email"]
        password = request.form['password']
        cursor.execute("SELECT email, password FROM users WHERE email = ? AND password = ?", (email,password,))
        data = cursor.fetchone()
        if data != None:
            session['email'] = email
            return redirect ('/loggedin')
        else: 
            return render_template('script.html')
    return render_template('login.html')

#AFTER SUCCESSFUL LOG IN
@app.route('/loggedin')
def loggedin():
    connection = sqlite3.connect("Database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT fname FROM users where email = ?", (session.get('email'),))
    data = cursor.fetchone()
    return render_template('loggedin.html', name = data)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
        
app.run(host='0.0.0.0', port=8080)
