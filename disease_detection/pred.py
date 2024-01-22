import tensorflow as tf
import numpy as np

from bardapi import Bard

model = tf.keras.models.load_model('test_model.h5')
model.load_weights('test_weights.h5')

img1 = 'image/apple_cedar_apple_rust.jpg'
img2 = 'image/apple_healthy.jpg'

label = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

image = tf.keras.preprocessing.image.load_img(img1, target_size=(224, 224))
image = tf.keras.preprocessing.image.img_to_array(image)
image = np.expand_dims(image, axis=0)

image = tf.keras.applications.efficientnet.preprocess_input(image)

prediction = model.predict(image)
predicted_class = np.argmax(prediction)

index = label[predicted_class].find('___')
if index == -1:
	req_s = "Python find() method didn't work."
else:
	crop = label[predicted_class][:index]
	disease = label[predicted_class][index+3:]
	if disease == 'healthy':
		req_s = "나는 도심에서 " + crop + "을 키우고 있는데, 다행이 병에 걸리지 않았어. 더 잘 키우는 팁 좀 줄래 ?"
	else:
		req_s = "나는 도심에서 " + crop + "을 키우고 있는데, " + disease + "에 걸렸어. 어떻게 치료해야 할까?"

print(req_s)

token = 'your_token'
bard = Bard(token=token)

print(bard.get_answer(req_s)['content'])