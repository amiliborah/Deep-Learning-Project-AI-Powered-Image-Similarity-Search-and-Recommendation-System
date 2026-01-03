import os
import pickle
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image

model = ResNet50(weights="imagenet", include_top=False, pooling="avg")

def extract_features(img_path):
    try:
        img = Image.open(img_path).convert("RGB")
        img = img.resize((224, 224))
        arr = np.array(img)
        arr = np.expand_dims(arr, axis=0)
        arr = preprocess_input(arr)
        return model.predict(arr)[0]
    except Exception as e:
        print(f"Skipping {img_path}: {e}")
        return None

features = {}

print("Starting feature extraction...")

for img_name in os.listdir("dataset_images"):
    if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
        print(f"Skipping non-image file: {img_name}")
        continue

    img_path = os.path.join("dataset_images", img_name)
    feat = extract_features(img_path)

    if feat is not None:
        features[img_name] = feat
        print("Processed:", img_name)

with open("image_features.pkl", "wb") as f:
    pickle.dump(features, f)

print("SUCCESS: image_features.pkl created with", len(features), "images")