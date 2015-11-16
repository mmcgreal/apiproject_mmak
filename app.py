#tumblr.py
from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

def read():
    with open ("data.txt", "r") as tags:
    data=tags.read().replace('\n', '') #should separate each entry into a new array entry


def apiCall(n):
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)

@app.route("/t")   
@app.route("/t/<tag>")
def main(tag=data): 
    key="6qjbDDaQ4vUogvpFIZ2UoaHuo6ykn1vMpjRYOdYOPCQI6dBw4K"
    uri="https://api.tumblr.com/v2/tagged?tag=%s&api_key=%s"
    url = uri%(tag,key)

   
    #r['response'][1]['photos'][0]['original_size']['url']
    photos = []
    for item in r['response']:
        try:
            photos.append(item['photos'][0]['original_size']['url'])
        except:
            pass

    return render_template("photos.html",urls=photos)

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "secret"
   app.run(host="0.0.0.0", port=8000)