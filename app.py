from flask import Flask, render_template, request
import urllib2, json, signal, time, thread, multiprocessing

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

def read():
    with open ("data.txt", "r") as tags:
    data=tags.read().replace('\n', '') #should separate each entry into a new array entry


def apiCall(n): #n=url
    request = urllib2.urlopen(n)
    result = request.read()
    return json.loads(result)

@app.route("/t")   
@app.route("/t/<tag>")
def main(): #defaulted to tebow for now
    tag="Tebow"
    if request.method == "POST":
        tag = request.form["player"]
    for space in [' ']:
        tag = tag.replace(space, "%20")
    basic = """ """ + tag + """&results=1"""
    tag = apiCall(basic)

    if tag["response"]["players"]:
        tag = tag["response"]["players"][0]["name"]
    else:
    tag = "Tebow"
    player = tag
    
    for space in [' ']:
        tag = tag.replace(space, "%20")
    print tag

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