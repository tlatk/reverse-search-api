from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://serpapi.com/search.json?engine=google_reverse_image&image_url=https://m.media-amazon.com/images/M/MV5BMTM0ODU5Nzk2OV5BMl5BanBnXkFtZTcwMzI2ODgyNQ@@._V1_UY317_CR4,0,214,317_AL_.jpg&api_key=bd55b12ad4e00a609ea7a279ec31726dded49ca2f3cfb6fe422032c7fd6954db"
    #url = "https://serpapi.com/search.json?engine=google_reverse_image&image_url=https://127.0.0.1:5000/static/image.jpg&api_key=bd55b12ad4e00a609ea7a279ec31726dded49ca2f3cfb6fe422032c7fd6954db"

    results = requests.get(url)

    data = json.loads(results.text)

    #print(json.dumps(data['inline_images'][0]['source'], indent=4, sort_keys=True))



    return render_template('index.html', data=data['inline_images'])