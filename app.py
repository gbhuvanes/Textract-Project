import os
import urllib.request
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template
import textractor
from document import Document
import json

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

UPLOAD_FOLDER = "static/uploads/"

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        result = textractor.analyze_image( filename=UPLOAD_FOLDER + filename)
        writeToFile("C:\AWS\Extract.txt",result)
        # flash("Text extracted successfully. Please find the extracted content in C:\AWS\Extract.txt")
        return redirect(request.url)
    else:
        flash("Allowed image types are -> png, jpg, jpeg")
        return redirect(request.url)

def writeToFile(fileName, content):
    with open(fileName, 'a', encoding='utf-8') as doc:
        for item in content:
            doc.write(str(item))
            doc.write("\n")
    

@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for("static", filename="uploads/" + filename), code=301)

if __name__ == '__main__':
    app.run()
  