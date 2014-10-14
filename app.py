from flask import Flask,render_template, request
from google import search
from bs4 import BeautifulSoup
import urllib3
import io

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def page():
    return render_template("home.html")

@app.route("/data")
def data():
    button = request.args.get("b",None)
    query = request.args.get("query",None)
    if button == "Search": #it will always be, if there's only one button
        if (len(query)>0): #as long as text is in box, len(query)>1
            
            ## SO FAR WE WILL ONLY DEAL WITH "who"

            ##Top 10 results
            search_results10 = [url for url in search(query,num=10,stop=1)]             
            ##Dictionary of names and occurrences
            names = {}

            #Process the text in each link
            for link in search_results10:
                #parse text
                raw_text = urllib3.connection_from_url(link).urlopen('GET',link).data
                soup = BeautifulSoup(raw_text)
                tagless_text = soup.get_text()
                print tagless_text
                
            #do more stuff?
            print search_results10
        
            return "this is the data page"
        else:
            return render_template("/error.html")



if __name__=="__main__":
    app.debug=True
    app.run()
