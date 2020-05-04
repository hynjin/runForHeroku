from flask import Flask, render_template, request, Response
from werkzeug import secure_filename

import os
import taxInvoice
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return 'this is test for heroku'

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        erp = request.files['erp']
        email = request.files['email']

        result = taxInvoice.tax(erp,email)

        response = Response(
        result.getvalue(),
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        content_type='application/octet-stream')

        dt = datetime.datetime.now()
        month = (int(dt.strftime("%m")) + 11)%12
        month = str(month)+"월세금계산서"
        fname = month

        response.headers["Content-Disposition"] = "attachment; filename=%s.xlsx" % fname
        return response
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
