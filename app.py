from flask import Flask, render_template, url_for
#import apache as url
import requests

def apache():
    url = ''
    try:
        r = requests.get(url)
        r.raise_for_status()
        return("Active")
    except requests.exceptions.HTTPError:
        return("URL not found")
    except requests.exception.ConnectionError:
        return("InActive")
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('homepage.html', res = apache())

if __name__ == "__main__" :
    app.run(debug = True)
