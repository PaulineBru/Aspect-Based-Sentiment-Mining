from flask import Flask
import recommender as sr
from  flask import render_template
from flask import request

app = Flask(__name__)




@app.route('/',
methods=['POST','GET']
)
def recommender():
    if request.method=='POST':
               print(request.form.keys())

               var1= request.form['condition']
               top =sr.test(var1)
               return render_template('web.html',
                drugs= top)
    else:

               return render_template('web.html',
                drugs= []




                    )

# Wie soll die Recommendationa aussehen und wie kann dieses auf einer Seite bkeiben
