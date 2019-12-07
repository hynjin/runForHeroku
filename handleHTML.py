#!/opt/anaconda3/bin/python3
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/data')
def render_file():
    return render_template('index.html')

@app.route('/fileUpload', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['email_file']
        f.save(secure_filename(f.filename))
        return 'upload 디렉토리 -> 파일 업로드 성공'

if __name__ == '__main__':
    app.run(debug = True)
# import cgi
# form = cgi.FieldStorage()
#
# erp = form["erp"].value
# email = form["email"].value
# title = form["title"].value
# description = form['description'].value
#
# opened_file = open('data/'+title, 'w')
# opened_file.write(description)
# opened_file.close()
#
# #Redirection
# print("Location: index.py?id="+title)
# print()
