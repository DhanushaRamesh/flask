from flask import Flask, render_template, url_for
import apache as url
import requests
import json

def apache():
    url = 'Give the url u need'
    try:
        r = requests.get(url)
        r.raise_for_status()
        get_response = r.text
        get_res_json = r.json()
        return(get_res_json)
    except requests.exceptions.HTTPError:
        return("URL not found")
    except requests.exception.ConnectionError:
        return("InActive")
app = Flask(__name__)
@app.route("/")
def home(): 
    return render_template('homepage.html', res = apache())   # Rendering HTML page and sending response to the html file

if __name__ == "__main__" :
    app.run(debug = True)








