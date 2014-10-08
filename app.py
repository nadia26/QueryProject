from flask import Flask,render_template
import google
#HOW TO USE THE GOOGLE LIBRARY
app = Flask(__name__)

@app.route("/")
def page():
    return google.search(query="hi",start=0,stop=10)
    #^ says generator object is not callable

    return render_template("home.html")

@app.route("/data")
def data():
    return "this is the data page"

if __name__=="__main__":
    app.debug=True
    app.run()
