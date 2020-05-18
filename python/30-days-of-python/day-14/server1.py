from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	return 'Hello, world. This is Falsk'


@app.route('/box-office-mojo-scraper', methods=['GET'])
def box_office_scraper_view():
	trigger_log_save()
	scrape_runner()
	return 'Done'

