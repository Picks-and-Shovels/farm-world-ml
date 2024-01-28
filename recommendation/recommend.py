import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics.pairwise import cosine_similarity

user_data = pd.read_csv("data/user.csv")
farm_data = pd.read_csv("data/farm.csv")
tag_data = pd.read_csv("data/tag.csv")
board_data = pd.read_csv("data/board.csv")

df_user_board = board_data.pivot(
    index='writerId',
    columns='title',
    values='views'
).fillna(0)

df_user_board = df_user_board.transpose()

sim = cosine_similarity(df_user_board, df_user_board)
sim_df = pd.DataFrame(data=sim, index=df_user_board.index, columns=df_user_board.index)

print(sim_df["girl"].sort_values(ascending=False)[0:3])