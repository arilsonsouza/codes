import requests
import pprint
import os
import pandas as pd

api_key = '<API KEY>'

# movie_id = 500
# api_version = 3
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# endpoint_path = f'/movie/{movie_id}'

# endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
# r = requests.get(endpoint)

# print(r.text)

# Using v4
# movie_id = 501
# api_version = 4
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# endpoint_path = f'/movie/{movie_id}'

# headers = {
# 	'Authorization': f'Bearer {api_key_v4}',
# 	'Content-Type': 'application/json;charset=utf-8'
# }

# endpoint = f'{api_base_url}{endpoint_path}'
# r = requests.get(endpoint, headers=headers)

# print(r.text)

api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'

search_query = 'The Matrix'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}'
r = requests.get(endpoint)

if r.status_code in range(200, 299):
	data = r.json()
	# pprint.pprint(data)
	
	results = data['results']	
	movie_ids = set()
	for result in results:
		_id = result['id']
		movie_ids.add(_id)
	
	output = 'movies.csv'
	movies_data = []

	for movie_id in movie_ids:
		api_base_url = f'https://api.themoviedb.org/{api_version}'
		endpoint_path = f'/movie/{movie_id}'
		
		endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
		r = requests.get(endpoint)
		if r.status_code in range(200, 299):
			data = r.json()
			movies_data.append(data)
		
	df = pd.DataFrame(movies_data)

	this_file_path = os.path.abspath(__file__)
	BASE_DIR = os.path.dirname(this_file_path)	
	path = os.path.join(BASE_DIR, 'data')
	os.makedirs(path, exist_ok=True)

	csv_file_path = os.path.join(path, output)
	df.to_csv(csv_file_path, index=False)