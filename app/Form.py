from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired
from app.models import User

class LoginForm(FlaskForm):
    handle = StringField('Handle',validators=[DataRequired()])
    remember_me  = BooleanField('Remember me')
    submit = SubmitField('Register')
    def validate_username(self,handle):
        ## here we can keep the check of the handle
        check = False
        if not check:
            raise ValidationError('No such handle could be found')
        
