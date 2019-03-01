from flask import Flask,jsonify
import requests
#import simplejson
import json

app = Flask(__name__)

@app.route("/")
def request():
    uri = "https://cve.circl.lu/api/search/servicenow"
    #connection test
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"
    #json response
    Jresponse = uResponse.text
    data = json.dumps(Jresponse)
    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)
