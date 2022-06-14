from flask import render_template, redirect, request
from dojo_survey import app
from dojo_survey.models.dojo import Dojo


@app.route('/')
def first():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if Dojo.validate_dojo(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    return render_template('index2.html', dojo = Dojo.get_last_survey())


@app.route('/goback', methods =['POST'])
def goback():
    return redirect('/')