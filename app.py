from flask import Flask,render_template, request
from google import search
from bs4 import BeautifulSoup
import urllib3
import io
from collections import Counter
import namefinder


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
            
            ## SO FAR WE WILL ONLY DEAL WITH "who". When dealing with datefinder, make an if statement inside the loop.

            ##Top 10 results
            search_results10 = [str(url) for url in search(query,start=1,stop=10,pause=1.0)]             
            #search_results10 = search(query, stop=25)

##Dictionary of names and occurrences
            names = []
            #"real" names
            femaleNames = namefinder.makeList("namefinder/femalenames.txt")
            maleNames = namefinder.makeList("namefinder/malenames.txt")
            validlasts = namefinder.makeList("namefinder/surnames.txt")
            validfirsts = femaleNames + maleNames
            tagless_text = ""
            print search_results10
            

            #Process the text in each link
            for link in search_results10:
                #parse text
                
                raw_text = urllib3.connection_from_url(link).urlopen('GET',link).data #this bothers me

                soup = BeautifulSoup(raw_text)
                #tagless_text += " ".join([str(x) for x in soup.find_all('p')]) #Way too slow
                tagless_text = soup.get_text() #still really slow and doesn't always work
                names += namefinder.findNames(tagless_text, validfirsts, validlasts)

                #if (search contains who...)
                #else if (search contains when...)
                
            #name = tagless_text #testing...

            name = Counter(names)
            name = name.most_common(1)[0][0]
            # CHANGE name TO THE NAME TO BE DISPLAYED
            # if (search contains who...)
            return render_template("result.html",query=query,name=name)
            #else if (search contains when...) return render_template("results.html",query=query,name=date) where date is a variable set to be the date
        else:
            return render_template("/error.html")



if __name__=="__main__":
    app.debug=True
    app.run()
