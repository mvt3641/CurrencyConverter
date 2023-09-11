# importinstall flask
from flask import Flask, render_template

app = Flask(__name__) # Folder Name

@app.route('/')
def index(): # App main page function
    return render_template('index.html')

@app.route('/sample',methods=["GET","POST"] )
def sample(): # App sample conversion form
    currencies = ['Dinar1', 'Dinar2', 'Dinar3', 'Dollar', 'Pound', 'etc']
    return render_template('sample.html',currencies=currencies)

@app.route('/about')
def about(): # App about or instructions form
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)

