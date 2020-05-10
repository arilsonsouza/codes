import os
import requests
import shutil

def download_file(url, base_dir, fname=None):
	if fname == None:
		 fname = os.path.basename(url)
	dl_filename = os.path.join(base_dir, fname)
	with requests.get(url, stream=True) as r:
		with open(dl_filename, 'wb') as f:
			shutil.copyfileobj(r.raw, f)

	return dl_filename