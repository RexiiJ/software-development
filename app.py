from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "welcome guests"

@app.route('/reg')
def reg():
    return "welcome to registration page"    

@app.route('/task')
def task():
    a=21
    b=52
    c=61
    d=a+b+c-50
    f=d*3
    return "this is the result of the addition " + str(f)


@app.route('/multiply')
def multiply():
    a=6
    b=9
    c=2
    d=a*b*c
    return "this is the result of the multiplication " + str(d)


@app.route('/aboutus')
def aboutus():
    email="joooh@yahoo.com"
    name="joooh"
    return render_template('aboutus.html', name=name, email=email)

@app.route('/homepage')
def homepage():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    return render_template('homepage.html', name=name,email=email)

    
    
    
    
    
    
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)