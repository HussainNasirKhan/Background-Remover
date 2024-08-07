from flask import Flask, render_template, request, send_file, redirect, url_for
from PIL import Image
from rembg import remove
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(input_path)
        
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
        output_image.save(output_path)
        
        return render_template('index.html', original_image=url_for('static', filename=f'img/{file.filename}'), output_image=url_for('static', filename='img/output.png'))

@app.route('/download')
def download_image():
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
