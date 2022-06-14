from flask import render_template, redirect, request, session
from dojo_survey import app


@app.route('/')
def first():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('index2.html')


@app.route('/goback', methods =['POST'])
def goback():
    session.clear()
    return redirect('/')