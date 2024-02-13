import sys
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

farm_data = pd.read_csv('data/farm.csv')

# sort the crop in each row. because of no-relation with columns with cossim
farm_data = farm_data[['crop0', 'crop1', 'crop2', 'crop3']]
farm_data = farm_data.apply(lambda row: sorted(row), axis=1)
farm_data = pd.DataFrame(list(farm_data), columns=['crop0', 'crop1', 'crop2', 'crop3'])
farm_data.insert(0, 'userId', farm_data.index)

# userId == id == index (so its possible)
cosine_sim = cosine_similarity(farm_data)
sim_df = pd.DataFrame(data=cosine_sim, index=farm_data.index, columns=farm_data.index)

# its user-based CF, so we can upgrade it to pearson correlation matrix
userId = int(sys.argv[1])
sim_user_crop = []
sim_user_crop.extend(sim_df[userId].sort_values(ascending=False)[1:5].index)

# get the crop that the user haven't planted
target_crop_set = set(farm_data.loc[farm_data['userId'] == userId, ['crop0', 'crop1', 'crop2', 'crop3']].values.flatten())
crop_set = set(farm_data.loc[farm_data['userId'] == sim_user_crop[0], ['crop0', 'crop1', 'crop2', 'crop3']].values.flatten())
non_duplicated_crop = crop_set - target_crop_set

crop_list = ['nothing', 'potato', 'tomato', 'pepper', 'corn', 'grape']
# i need exception case with empty set, but i'll skip it
print('suggested crop:', crop_list[non_duplicated_crop.pop()])