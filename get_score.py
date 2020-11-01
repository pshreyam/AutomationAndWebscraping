from flask import Flask
import requests
from bs4 import BeautifulSoup

URL = "https://www.espncricinfo.com/series/8048/game/1216506"

app = Flask(__name__)

def get_score():
	r = requests.get(URL)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		return {
			"score": soup.find_all('div', class_="score-run font-weight-bold")[0].get_text()
		}
	return {
		"score": "Sorry! Score cannot be fetched!"
	}

@app.route('/')
def index():
	score = get_score()
	return "<meta http-equiv='refresh' content='5' /><h1>"+score['score']+"</h1>"
	
if __name__ == "__main__":
	app.run(debug=True)
