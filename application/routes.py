from flask import Flask, render_template, url_for, request, redirect, send_file, session
from application import app
from application.forms import GenerateForm
import pyqrcode
import png
import os

@app.route('/')
@app.route('/home')
def index():
    session['name']=False
    gForm   =   GenerateForm()
    return render_template('index.html', form=gForm)

@app.route('/qrcode', methods=['GET','POST'])
def generation():
    name        =   request.form.get('name')
    course      =   request.form.get('course')
    date        =   request.form.get('date')
    str         =   (name+" | "+course+" | "+date)

    code        =   pyqrcode.create(str)
    nFile       =   'qrcode'+name+'.png'
    session['file']=nFile
    code.png(nFile, scale=5)
    os.system('cmd /c "move "'+nFile+'" application\qr"') 
    return render_template('qrcode.html', name=name)

@app.route('/download')
def download():
    nFile=session.get('file')
    filename = "qr/"+nFile
    return send_file(filename,as_attachment=True)
