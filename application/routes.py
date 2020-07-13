from flask import Flask, render_template, url_for, request, redirect
from application import app
from application.forms import GenerateForm
import pyqrcode
import png

@app.route('/')
@app.route('/home')
def index():
    gForm   =   GenerateForm()
    return render_template('index.html', form=gForm)

@app.route('/qrcode', methods=['GET','POST'])
def generation():
    name        =   request.form.get('name')
    course      =   request.form.get('course')
    date        =   request.form.get('date')
    str         =   (name+" | "+course+" | "+date)

    code        =   pyqrcode.create(str)
    code.png('qrcode.png', scale=4)

    return render_template('qrcode.html')
