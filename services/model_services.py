from keras.applications import imagenet_utils
from keras.utils.image_utils import img_to_array
import cv2
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import numpy as np
from config import MODEL_PATH

IMAGEDIR="./img/"

model = load_model(MODEL_PATH)
labels = ['G&M', 'Organic', 'Other', 'Paper', 'Plastic']
le = LabelEncoder()
labels = le.fit_transform(labels)

def pre(img_path):
    img = cv2.resize(img_path, (224, 224))
    img = imagenet_utils.preprocess_input(img)
    img = img_to_array(img)
    img = np.expand_dims(img / 255, 0)
    return img

def predict(img):
    img = cv2.imread(img, 1)
    img1 = pre(img)
    p = model.predict(img1)
    predicted_class = le.classes_[np.argmax(p[0], axis=-1)]
    score = p.max()
    return predicted_class,score