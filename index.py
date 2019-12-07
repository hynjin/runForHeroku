# #!/opt/anaconda3/bin/python3
# print("Content-Type: text/html")
# print()

#!/opt/anaconda3/bin/python3

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()
