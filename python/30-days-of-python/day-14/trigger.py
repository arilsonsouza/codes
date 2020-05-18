import requests

ngrok_url = ''
endpoint f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.text)