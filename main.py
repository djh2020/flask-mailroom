import os
import base64
import random

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        donation = Donation(donor=request.form['name'], value=int(request.form['donation']))
        donation.save()
        return redirect(url_for('all'))
    else:
        donors = Donor.select()
        return render_template('add.jinja2', donors=donors)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

