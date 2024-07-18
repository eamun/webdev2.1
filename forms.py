from flask_wtf import FlaskForm
from wtforms import SubmitField,TimeField,DateField,StringField,PasswordField
from wtforms.validators import InputRequired,EqualTo

class registrationform(FlaskForm):
    userid=StringField('Username:',validators=[InputRequired()])
    password1=PasswordField('Password:',validators=[InputRequired()])
    password2=PasswordField('Password again:',validators=[InputRequired(),EqualTo('password1')])
    submit=SubmitField('Confirm')

class loginform(FlaskForm):
    userid=StringField('Username:',validators=[InputRequired()])
    password=PasswordField('Password:',validators=[InputRequired()])
    submit=SubmitField('Confirm')

class adminloginform(FlaskForm):
    userid=StringField('Admin Username:',validators=[InputRequired()])
    password=PasswordField('Admin Password:',validators=[InputRequired()])
    submit=SubmitField('Confirm')

class bookingform(FlaskForm):
    appttime=TimeField('Appointment time:',validators=[InputRequired()])
    apptdate=DateField('Appointment Date:', validators=[InputRequired()])
    userid=StringField('Username:')
    haircut=StringField('Haircut:')
    submit=SubmitField('Book')

class reviewform(FlaskForm):
    review=StringField('Write a review:',validators=[InputRequired()])
    submit=SubmitField('Send')

    