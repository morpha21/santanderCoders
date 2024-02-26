import pandas as pd
import numpy as np

from datetime import datetime




def format_columns(columns: pd.core.indexes.base.Index) -> list:
	"""receives thecolumns of a DataFrame and returns a list with more suitable
	column names"""
	return [col.replace(".","_").replace("@","").replace("games_","") for col in columns]




def adequate(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
	disposable_columns = ['initial_setup', 'white_id', 'black_id',
				   'start_time', 'pgn', 'tcn', 'uuid', 'fen', 'rules',
				   'end_time', 'tournament']
	if df.empty:
		return df
	df.columns = format_columns(df.columns)
	df = df[df['rules'] == 'chess']
	df = df[df['time_class'] != 'daily']
	first_cols   = [col for col in
			['white_username', 'white_uuid', 'white_result', 'white_rating',
			'black_username', 'black_uuid', 'black_result', 'black_rating']
			if col in df.columns]
	last_cols    = [col for col in
			['accuracies_white', 'accuracies_black', 'url']
			if col in df.columns]
	ordered_cols = first_cols + [col for col in df.columns if (col not in first_cols) and (col not in last_cols)] + last_cols
	df = df[ordered_cols]
	df.index = df['end_time'].apply(datetime.fromtimestamp)
	return df.drop([col for col in disposable_columns if col in df.columns], axis=1)



def personalize(df: pd.core.frame.DataFrame, user: str) -> pd.core.frame.DataFrame:
	personalizable = df.apply(lambda row: user in row['white_username'] or user in row['black_username'], axis=1).all()

	if not personalizable:
		print(f'Not all games are from {user}')
		return df
	df['played_as']       = np.where(df['white_username'] == user, 'white', 'black')
	df['against']         = np.where(df['white_username'] == user, 'black', 'white')
	df['opponent']        = np.where(df['played_as'] == 'white', df['black_username'], df['white_username'])
	df['opponent_uuid']   = np.where(df['played_as'] == 'white', df['black_uuid'], df['white_uuid'])
	df['rating']          = np.where(df['played_as'] == 'white', df['white_rating'], df['black_rating'])
	df['opponent_rating'] = np.where(df['played_as'] == 'black', df['white_rating'], df['black_rating'])
	df['result']          = np.where(df['played_as'] == 'white', df['white_result'], df['black_result'])
	df['opponent_result'] = np.where(df['played_as'] == 'black', df['white_result'], df['black_result'])
	df['draw']            = (df['result'] == df['opponent_result'])
	if ('white_accuracies' in df.columns):
		df['accuracies']          = np.where(df['played_as'] == 'white', df['white_accuracies'], df['black_accuracies'])
		df['opponent_accuracies'] = np.where(df['played_as'] == 'black', df['white_accuracies'], df['black_accuracies'])

	disposable_columns = ['white_username','white_uuid','white_result','white_rating',
			      'black_username','black_uuid', 'black_result', 'black_rating',
                              'accuracies_white','accuracies_black']

	first_columns = ['time_control', 'time_class', 'rating', 'played_as', 'result',
                         'against', 'opponent_rating', 'opponent', 'opponent_result']
	last_columns  = ['opponent_uuid']

	ordered_columns = first_columns + last_columns + [c for c in df.columns if c not in (first_columns+last_columns)]
	df = df[ordered_columns]
	return df.drop(disposable_columns, axis=1)

