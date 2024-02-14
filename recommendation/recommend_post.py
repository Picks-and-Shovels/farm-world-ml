import sys
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

board_data = pd.read_csv("data/board_read_like.csv")
farm_data = pd.read_csv("data/farm.csv")
board_tag_data = pd.read_csv("data/board_tag.csv")

userId = int(sys.argv[1])

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

sim_view.extend(sim_df[userId].sort_values(ascending=False)[1:21].index)
#print(sim_view)

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

sim_liked.extend(sim_df[userId].sort_values(ascending=False)[1:21].index)
#print(sim_liked)

# values : farm
farm_data = farm_data[['userId', 'crop0', 'crop1', 'crop2', 'crop3']]
crop_set = set(farm_data.loc[farm_data['userId'] == userId, ['crop0', 'crop1', 'crop2', 'crop3']].values.flatten())
crop_list = list(crop_set)

board_like = board_data[['boardId', 'liked']]
board_like_count = board_like.groupby('boardId')['liked'].sum().reset_index()
df_tag_like = pd.merge(board_tag_data, board_like_count, on='boardId')
df_tag_like.sort_values(by='liked', ascending=False, inplace=True)

crop_tag_rank = []

for i in crop_list:
	crop_tag_rank.extend(df_tag_like.loc[df_tag_like['tagId'] == i, 'boardId'].values[:5])
#print(crop_tag_rank)

same_numbers = list(set(sim_view) & set(sim_liked) & set(crop_tag_rank))
for i in same_numbers:
	print(i, end=' ')
print()