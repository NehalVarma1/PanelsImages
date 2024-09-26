import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Path to your image folder
IMAGE_FOLDER = r'C:\Users\nehal\Documents\PanelsImages\downloads'

@app.route('/')
def index():
    # Get a list of all image files in the folder
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return render_template('index.html', images=images)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
