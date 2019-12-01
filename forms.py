from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class createform(FlaskForm):
    vehiclenumber = StringField('Vehicle Number', validators=[DataRequired()])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    prikey = StringField('Private Key', validators=[DataRequired()])
    pubkey = StringField('Public Key', validators=[DataRequired()])
    submit = SubmitField('Create Asset')


class queryform(FlaskForm):
    search = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Send Query')


class transferform(FlaskForm):
    txid = StringField('Transaction ID', validators=[DataRequired()])
    opk = StringField('Owner Public Key', validators=[DataRequired()])
    rpk = StringField('Recepient Public Key', validators=[DataRequired()])
    oprk = StringField('Owner Private Key', validators=[DataRequired()])
    submit = SubmitField('Sign Transaction and Transfer')


class checkform(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Check for Asset')


"""class checkerpoform(FlaskForm):
    ID = StringField('id', validators=[DataRequired()])
    pk = StringField('public key', validators=[DataRequired()])
    submit = SubmitField('CHECK')"""


class initform(FlaskForm):
    submit = SubmitField('Generate Keypair')
