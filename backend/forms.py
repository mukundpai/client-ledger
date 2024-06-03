
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class ServiceForm(FlaskForm):
    service_title = StringField('Service Title', validators=[DataRequired()])
    client_id = StringField('Client ID', validators=[DataRequired()])
    category_id = StringField('Category ID', validators=[DataRequired()])
    service_type_id = StringField('Service Type ID', validators=[DataRequired()])
    end_date = DateField('End Date')
    create_date = DateField('Create Date')
    submit = SubmitField('Create Service')