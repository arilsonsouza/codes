import datetime
import requests
import pandas as pd
from requests_html import HTML
import os
import sys

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)

def url_to_txt(url, filename='world.html', save=False):
	r = requests.get(url)

	if r.status_code == 200:
		html_text = r.text
		file_path = os.path.join(BASE_DIR, filename)			
		
		if save:
			with open(file_path, 'w') as f:
				f.write(html_text)

		return html_text
	return None

def parse_and_extract(url, name='2020'):
	html_text = url_to_txt(url)
	if html_text == None:
		return False

	r_html = HTML(html=html_text)
	table_class = '.imdb-scroll-table'
	
	r_table = r_html.find(table_class)
	
	table_data = []
	header_names = []

	if len(r_table) != 1:
		return False

	parsed_table = r_table[0]
	rows = parsed_table.find('tr')
	header_row = rows[0]
	header_cols = header_row.find('th')
	header_names = [x.text for x in header_cols]
	for row in rows[1:]:
		cols = row.find('td')
		row_data = []
		for i, col in enumerate(cols):
			row_data.append(col.text)
		table_data.append(row_data)

	df = pd.DataFrame(table_data, columns=header_names)
	path = os.path.join(BASE_DIR, 'data')
	os.makedirs(path, exist_ok=True)
	csv_file_path = os.path.join(path, f"{name}.csv")
	df.to_csv(csv_file_path, index=False)
	return True


def run(start_year=None, years_ago=1):
	if start_year == None:
		now = datetime.datetime.now()
		start_year = now.year
	assert isinstance(start_year, int)
	assert len(f'{start_year}') == 4
	
	for i in range(0, years_ago + 1):
		url = f'https://www.boxofficemojo.com/year/world/{start_year}'
		finished = parse_and_extract(url, name=start_year)
		if finished:
			print(f'Finished {start_year}')
		else:
			print(f'{start_year} not finished')
		start_year -= 1
