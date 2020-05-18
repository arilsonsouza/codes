from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()

@app.get('/')
def hello_world():
	return {'hello': 'world'}

@app.get('/box-office-mojo-scraper')
def box_office_scraper_view():
	trigger_log_save()
	scrape_runner()
	return { 'message': 'Done' }