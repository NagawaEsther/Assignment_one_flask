#Creating my first app
#importing Flask

from flask import Flask

#creating an instance from the Flask class
app=Flask(__name__) #creating app instance

#working with the app decorator.decorator starts with the @symbol
#it takes in two parameters that is the path/url and the methods parameter

@app.route("/") #() defines the path and methods to be used and "/" defines methods to be used

#creating a root page for the app
def home():
    return "<h1>Nagawa Esther Cohort 3 Python flask </h1>"\
'<p>i love code</p>'


@app.route("/about")
def about():
    return "<h2>flask basics </h2>"


#turning on the debug option
if __name__ =="_main_":
    app.run(debug=True)
