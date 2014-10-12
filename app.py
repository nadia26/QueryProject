from flask import Flask,render_template, request
#import google
from google import search
#HOW TO USE THE GOOGLE LIBRARY
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def page():
    #return google.search(query="hi",start=0,stop=10)
    #^ says generator object is not callable

    return render_template("home.html")

@app.route("/data")
def data():
    button = request.args.get("b",None)
    query = request.args.get("query",None)
    if button == "Search": #it will always be, if there's only one button
        #for url in search(query, num=10, stop=1): #default pause=2.0
           # print(url)
        if (len(query)>0):
            search_results10 = [url for url in search(query,num=10,stop=1)]
            #do more stuff
        
            return "this is the data page"
        else:
            return render_template("/error.html")



if __name__=="__main__":
    app.debug=True
    app.run()
