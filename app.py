from flask import Flask, render_template, request
import os, time
from model import find_similar_images

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SEARCH_COUNT = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global SEARCH_COUNT
    results = None
    query_image = None
    top_k = 5
    latency = None

    if request.method == "POST":
        SEARCH_COUNT += 1
        start = time.time()

        file = request.files["image"]
        top_k = int(request.form.get("top_k", 5))

        query_image = file.filename
        path = os.path.join(UPLOAD_FOLDER, query_image)
        file.save(path)

        results = find_similar_images(path, top_k=top_k)

        latency = round((time.time() - start) * 1000, 2)

    return render_template(
        "index.html",
        results=results,
        query_image=query_image,
        top_k=top_k,
        latency=latency,
        searches=SEARCH_COUNT
    )

if __name__ == "__main__":
    app.run(debug=True)