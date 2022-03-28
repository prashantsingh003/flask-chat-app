from dataclasses import dataclass
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class JoiningForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    room_id=StringField('RoomID',validators=[DataRequired()])
    submit=SubmitField('Submit')