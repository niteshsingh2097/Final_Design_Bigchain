from flask_wtf import FlaskForm
from flask import Flask, render_template, url_for, redirect, flash
from forms import createform, checkform, queryform, transferform, initform
from backend import back


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = initform()
    if form.validate_on_submit():

        msg, msg1 = back.init()
        msg = 'Public Key: ' + msg + ' Private Key: ' + msg1
        flash(msg)

    return render_template('home.html', form=form)


@app.route("/create", methods=['GET', 'POST'])
def create():
    form = createform()
    if form.validate_on_submit():
        vehicle_number = form.vehiclenumber.data
        manufacturer1 = form.manufacturer.data
        prikey = form.prikey.data
        pubkey = form.pubkey.data

        signed_tx = back.docreate(
            vehicle_number, manufacturer1, pubkey, prikey)
        flash(signed_tx)

    return render_template('create.html', form=form)


@app.route("/check", methods=['GET', 'POST'])
def check():
    form = checkform()
    if form.validate_on_submit():
        ID = form.id.data
        msg = back.checker(ID)
        flash(msg)

    return render_template('check.html', form=form)


@app.route("/transfer", methods=['GET', 'POST'])
def transfer():
    form = transferform()
    if form.validate_on_submit():
        txid = form.txid.data
        opk = form.opk.data
        rpk = form.rpk.data
        oprk = form.oprk.data
        msg, privateKey = back.asset_transfer(txid, opk, rpk, oprk)
        flash(msg)

    return render_template('transfer.html', form=form)


@app.route("/query", methods=['GET', 'POST'])
def query():
    form = queryform()
    if form.validate_on_submit():
        srch = form.search.data
        msg = back.queryer(srch)
        flash(msg)
    return render_template('query.html', form=form)


"""@app.route("/checker_po", methods=['GET', 'POST'])
def checkerpo():
    form = checkerpoform()
    if form.validate_on_submit():
        ID = form.ID.data
        pk = form.pk.data
        msg = back.checkerpoform(ID, pk)

        flash(msg)
    return render_template('checker_po.html', form=form)"""


if __name__ == '__main__':
    app.run(debug=True)
