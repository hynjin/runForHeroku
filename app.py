from flask import Flask, render_template, request, Response
from werkzeug import secure_filename

import pandas as pd
import taxInvoice
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'this is test for heroku'

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['erp'])
        erp = request.files['erp']
        print(request.files['email'])
        email = request.files['email']
        result = taxInvoice.tax(erp,email)
        response = Response(
        result.getvalue(),
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        content_type='application/octet-stream')
        dt = datetime.datetime.now()
        fname = dt.strftime("%m월세금계산서").encode('utf-8').decode('iso-8859-1')
        response.headers["Content-Disposition"] = "attachment; filename=%s.xlsx" % fname
        return response
    return render_template('index.html')
