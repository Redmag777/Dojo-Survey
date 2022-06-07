from crypt import methods
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def first():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['location'] = request.form['location']
    session['comment'] =  request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('index2.html')


@app.route('/goback', methods =['POST'])
def goback():
    session.clear()
    return redirect('/')

if __name__==('__main__'):
    app.run(debug=True)