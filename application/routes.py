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
    val         =   (name,course, date)

    code        =   pyqrcode.create(val)
    code_png    =   code.png_as_base64_str(scale=5)
    html_img = '<img src="data:image/png;base64,{}">'.format(code_png)

    return redirect('index.html', code_png=html_img)