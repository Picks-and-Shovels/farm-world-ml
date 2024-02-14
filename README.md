# farm-world-ml
Picks-and-Shovels FarmWorld ML Part Repository
## Stacks
- Python 3.11
- Tensorflow 2.13.0
## Functions
- Plant Disease Detection
	- Plant disease detection determines pests and diseases through photos of the user's plant leaves and even suggests solutions for the pests.
	- Open Dataset and API
		- Using Kaggle Plant Village Dataset (https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
		- Generate plant disease solutions answers using Google Gemini (https://gemini.google.com/app)
- Post and crop recommendations for users
	- "recommendation" recommends crops for the user and articles that may be helpful for urban agriculture.
	- Reference
		- https://github.com/lsjsj92/recommender_system_with_Python
## How to use
### general
1. clone this repository
2. run setup.sh to install requirements.txt
### disease_detection
1. download pre-trained model in disease_detection directory
 - download at https://drive.google.com/file/d/1SSs4ZLdTdUOOYDp5Fjpql7AlISgTm_0B/view?usp=drive_link
2. unzip archive.zip in this directory
3. run disease_detection/pred.py with img_url to argv[1] 
	- python3.11 disease_detection/pred.py "your_img_url"
4. then result will print in console (sentences)
### recommendation
**recommend_crop**
1. run recommendation/recommend_crop.py with userId to argv[1]
	- python3.11 recommendation/recommend_crop.py 0
2. then result will print in console (crop_name or cropId)

**recommend_post**
1. run recommendation/recommend_post.py with userId to argv[1]
	- python3.11 recommendation/recommend_post.py 0
2. then result will print in console (boardId)