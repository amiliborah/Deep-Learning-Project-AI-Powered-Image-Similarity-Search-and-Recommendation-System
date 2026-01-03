import os
import pickle
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# Load pretrained CNN
model = ResNet50(weights="imagenet", include_top=False, pooling="avg")

# Load feature database
with open("image_features.pkl", "rb") as f:
    features_db = pickle.load(f)

def extract_features(img_path):
    """
    Extract deep features from an image
    """
    img = Image.open(img_path).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)
    return model.predict(arr)[0]

def find_similar_images(query_img, top_k=5):
    """
    Find top-k similar images
    """
    query_feat = extract_features(query_img)
    scores = {}

    for name, feat in features_db.items():
        score = cosine_similarity([query_feat], [feat])[0][0]
        scores[name] = score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]