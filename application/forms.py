from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField,TextAreaField
from wtforms.validators import DataRequired

class GenerateForm(FlaskForm):
    name    =   StringField("Name", validators=[DataRequired()])
    course  =   StringField("Course Name", validators=[DataRequired()])
    date    =   DateField('Date', format='%D-%M-%Y', validators=[DataRequired()])
    generate=   SubmitField()