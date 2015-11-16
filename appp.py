from flask import Flask, render_template, request
import urllib2, json, signal, time, thread, multiprocessing
from threading import Thread
import urllib2
import json
import xmltodict
import random

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/t")
def t():

    key="6qjbDDaQ4vUogvpFIZ2UoaHuo6ykn1vMpjRYOdYOPCQI6dBw4K"
    uri="https://api.tumblr.com/v2/tagged?tag=%s&api_key=%s"

    url1 = uri%("insect",key)
    request = urllib2.urlopen(url1)
    result = request.read()
    r = json.loads(result)

    url2 = uri%("animal",key)
    request2 = urllib2.urlopen(url2)
    result2 = request2.read()
    r2 = json.loads(result2)

    #r['response'][0]['photos'][0]['original_size']['url']

    photos1=[]
    for item in r['response']:
        try:
            newphoto1 = item['photos'][0]['original_size']['url']
            photos1.append(newphoto1)
        except:
            pass

    photos2=[]
    for item in r2['response']:
        try:
            newphoto2 = item['photos'][0]['original_size']['url']
            photos2.append(newphoto2)
        except:
            pass

    return render_template("tagged.html",urls1=photos1,urls2=photos2)



if __name__ == "__main__":
   app.debug = True
   app.secret_key = "secret"
   app.run(host="0.0.0.0", port=8000) 

