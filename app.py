from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def page():
    #return "hi"
    return render_template("home.html")

@app.route("/data")
def data():
    return "this is the data page"

if __name__=="__main__":
    app.debug=True
    app.run()
