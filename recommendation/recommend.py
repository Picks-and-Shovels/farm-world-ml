import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics.pairwise import cosine_similarity

board_data = pd.read_csv("data/data.csv")

df_user_board = board_data.pivot_table(
	values='views',
	index='userId',
	columns='title',
	aggfunc='sum').fillna(0)

df_user_board = df_user_board.transpose()

sim = cosine_similarity(df_user_board, df_user_board)
sim_df = pd.DataFrame(data=sim, index=df_user_board.index, columns=df_user_board.index)

print(sim_df["09DP70A8"].sort_values(ascending=False)[1:10])