# Background Remover

**Description:**
The Background Remover is a Flask-based web application that allows users to remove the background from images effortlessly. Users can upload an image, and the application will process it to remove the background, providing an option to download the resulting image.

https://github.com/user-attachments/assets/dc35ff71-1d82-42b2-9f5d-358861e294ba

**Features:**
- **Upload Image:** Users can upload images in various formats.
- **Background Removal:** Utilizes the `rembg` library to remove the background from the uploaded image.
- **Preview Original and Processed Images:** Displays both the original and processed images side by side for easy comparison.
- **Download Processed Image:** Users can download the processed image with the background removed.
- **User-Friendly Interface:** Clean and simple UI with navigation options.

**Tech Stack:**
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Image Processing:** PIL (Python Imaging Library), rembg

**Getting Started:**
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/HussainNasirKhan/Background-Remover.git
    cd Background-Remover
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```sh
    python app.py
    ```

4. **Open in Browser:**
    Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

**Requirements:**
- Python 3.9 or higher
- Flask
- rembg
- Pillow

**Usage:**
- Upload an image using the upload form.
- The application will process the image and remove the background.
- View and compare the original and processed images.
- Download the processed image if desired.
- Upload another image or restart the process as needed.

**Contribution:**
Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!

