# 🔍 AI-Powered Image Similarity Search & Recommendation System

A production-style AI web application that finds **visually similar images** using deep learning.  
The system extracts visual embeddings from images using a CNN model and performs similarity search, presenting results through a **modern, professional web interface**.

---

## 📌 Project Overview

In today’s digital world, platforms like **e-commerce, social media, and image libraries** require intelligent systems to recommend visually similar images.  
Traditional text-based search fails to capture **visual semantics**.

This project solves that problem by using **deep learning–based image embeddings** and **cosine similarity** to identify visually similar images **without relying on manual tags or descriptions**.

---

## 🧠 Problem Statement

> How can we automatically identify and recommend visually similar images from a large dataset using only image content?

---

## 🚧 Key Challenges Faced (and Solved)

### 1️⃣ Image Feature Extraction  
- **Challenge:** Extract meaningful visual representations  
- **Solution:** Used **ResNet50 (pretrained on ImageNet)** to generate deep embeddings

### 2️⃣ Similarity Computation  
- **Challenge:** Efficient comparison between images  
- **Solution:** Applied **cosine similarity** on feature vectors

### 3️⃣ Dataset Issues  
- **Challenge:** Solid-color images produced weak similarity results  
- **Solution:** Replaced dataset with **real-world images** (shoes, bags, cars)

### 4️⃣ Image Serving in Web App  
- **Challenge:** Images not displaying correctly  
- **Solution:** Proper use of Flask’s `static/` directory for dataset images and `uploads/` for query images

### 5️⃣ User Experience  
- **Challenge:** Initial UI looked too simple  
- **Solution:** Designed a **professional SaaS-style UI** with:
  - Dark mode
  - Drag & drop upload
  - Image zoom modal
  - Similarity bars
  - Category badges
  - Analytics (latency & search count)

### 6️⃣ Deployment  
- **Challenge:** Exposing a local ML app securely  
- **Solution:** Used **Cloudflare Tunnel** for secure public access without cloud servers
---

## ⚙️ Tech Stack

### 🔹 Backend
- Python
- Flask
- TensorFlow / Keras
- NumPy
- Scikit-learn

### 🔹 Model
- ResNet50 (Pretrained, feature extraction)

### 🔹 Frontend
- HTML5
- CSS3
- JavaScript
- Responsive card-based UI

### 🔹 Deployment
- Cloudflare Tunnel
- Local Flask server

---

Each image is embedded and stored in `image_features.pkl`.

---

## ✨ Key Features

- 🔍 AI-based visual similarity search
- 🧠 Deep learning feature extraction (ResNet50)
- 🏷️ Category-aware results (Shoes / Bags / Cars)
- 📊 Similarity confidence visualization
- 🌙 Dark / Light mode toggle
- 🖱️ Drag & drop image upload
- 🔎 Image zoom modal
- 📈 Analytics (search count & latency)
- 🌐 Cloudflare public deployment

---

## ▶️ How to Run Locally
pip install -r requirements.txt
python create_features.py
python app.py
http://127.0.0.1:5000

---

## 🏗️ System Architecture
