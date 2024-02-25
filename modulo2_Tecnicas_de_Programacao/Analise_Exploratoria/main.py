import concurrent.futures
from datetime import datetime

import pandas as pd

import transform.chess_transform as ct
from extract.chess_request import request_games
from extract.chess_request import get_user


def worker(year_,user_,email_):
	df_list = []
	current_month = datetime.now().month
	global current_year

	for month in range(1, 13):
		df = request_games(year_, month, user_, email_)
		df_list += [df]
		if (year_ == current_year) and (month == current_month):
			break
	return pd.concat(df_list)



current_year = datetime.now().year
user         = "morpha_21"
email        = ""

with open("extract/.email", 'r') as email_file:
	email = email_file.read().strip()

with concurrent.futures.ThreadPoolExecutor() as executor:
	futures = []
	for year in range(2020, current_year+1):
			futures += [executor.submit(worker, year, user, email)]
	df_list = [f.result() for f in futures]

df = pd.concat(df_list)
df = ct.adequate(df)
df.sort_index(inplace=True)

uuid = df[df['white_username'] == user]['white_uuid'].unique()[0]

df   = ct.personalize(df, user)

print()
print(df)

l = 1 + len(df['opponents'])//6

opponents = [df['opponent'][l*i:l*(i+1)] for i in range(0,7)]

print()
print(opponents)
print()








df.to_csv(f"{user}_chess_games.csv")


