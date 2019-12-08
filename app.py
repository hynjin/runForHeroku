from flask import Flask, render_template, request, Response
from werkzeug import secure_filename

import pandas as pd
import taxInvoice
import openpyxl
# import flask_excel as excel
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'this is test for heroku'

# @app.route('/upload', methods = ['GET','POST'])
# def load_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             a = 'file uploaded'
#    return render_template('upload.html', data = a)

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        test = taxInvoice.tax(f)
        response = Response(
        test.getvalue(),
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        content_type='application/octet-stream')
        response.headers["Content-Disposition"] = "attachment; filename=boom.xlsx"
        return response
    return render_template('index.html')

@app.route("/export", methods=['GET'])
def export_records():
    return

@app.route('/test.csv')
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield ','.join(row) + '\n'
    return Response(generate(), mimetype='text/csv')
