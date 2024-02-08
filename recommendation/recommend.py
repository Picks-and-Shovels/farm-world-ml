import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

board_data = pd.read_csv("data/board_read_like.csv")

# values : viewed
sim_view = []

df_user_board = board_data.pivot_table(
	values='viewed',
	index='userId',
	columns='boardId',
	aggfunc='sum').fillna(0)

df_user_board = df_user_board.transpose()

sim = cosine_similarity(df_user_board, df_user_board)
sim_df = pd.DataFrame(data=sim, index=df_user_board.index, columns=df_user_board.index)

sim_view.extend(sim_df[0].sort_values(ascending=False)[1:11].index)
print(sim_view)

# values : liked
sim_liked = []

df_user_board = board_data.pivot_table(
	values='liked',
	index='userId',
	columns='boardId',
	aggfunc='sum').fillna(0)

df_user_board = df_user_board.transpose()

sim = cosine_similarity(df_user_board, df_user_board)
sim_df = pd.DataFrame(data=sim, index=df_user_board.index, columns=df_user_board.index)

sim_liked.extend(sim_df[0].sort_values(ascending=False)[1:11].index)
print(sim_liked)

# values : farm