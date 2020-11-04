# No APIs used
# Web Scraping implemented

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
			"team1": soup.find_all('div', class_="score-run font-weight-bold")[0].get_text(),
			"team2": soup.find_all('div', class_="score-run font-weight-bold")[1].get_text()
		}
	return None

@app.route('/')
def index():
	score = get_score()
	if score:
		return "<meta http-equiv='refresh' content='5' /><h1>"+\
		score['team1']+"</h1><h1>"+score['team2']+"</h1>"
	return "<meta http-equiv='refresh' content='5' /><h1>No score available!</h1>"
	
if __name__ == "__main__":
	app.run(debug=True)
