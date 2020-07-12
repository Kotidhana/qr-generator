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
    name        =   str(request.form.get('name'))
    course      =   str(request.form.get('course'))
    date        =   str(request.form.get('date'))

    code        =   pyqrcode.create(name)
    code.svg('uca.svg', scale=4)
    code.eps('uca.svg', scale=2)
    html_img    =   code.terminal(quiet_zone=1)

    return render_template('qrcode.html', code_png=html_img)

    # https://www.youtube.com/watch?v=zfodARFn25s