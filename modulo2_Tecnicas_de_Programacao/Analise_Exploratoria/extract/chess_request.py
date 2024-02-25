from time import sleep

import pandas as pd
import requests as rq

def request_json(url: str, email: str) -> dict:
	headers={'User-Agent': email}
	response = rq.get(url, headers=headers)
	while response.status_code == 429:
		sleep(0.618)
		response = rq.get(url, headers=headers)
	if response.status_code == 200:
		return response.json()
	print(f'Error: {response.status_code}')
	return None

def request_games(year: int, month: int, user: str, email: str) -> pd.core.frame.DataFrame:
	"""gets chess data from chess.com"""
	year  = str(year)
	month = ("0"+str(month))[-2:]
	print(f"\rrequesting game data from {month}/{year}... ", end=' ')

	url   = f"https://api.chess.com/pub/player/{user}/games/{year}/{month}"
	
	return pd.json_normalize(request_json(url, email)['games'])




def get_user(user: str, email:str) -> pd.core.frame.DataFrame:
	"""gets data from a given chess.com user"""
	url= f"https://api.chess.com/pub/player/{user}/"
	user_json = request_json(url, email)
	disposable_keys = [el for el in ['tactics', 'puzzle_rush'] if el in  user_json.keys()]
	for key in disposable_keys:
		del user_json[key]
	return pd.json_normalize(user_json)
	

def get_user_country(user: str, email:str) -> str:
	"""Gets the country of a user"""
	url= f"https://api.chess.com/pub/player/{user}/"
	return request_json(url, email)['country'].split("/")[-1]
	