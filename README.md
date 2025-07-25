
# 🖼️ Image Resizer Tool

A simple Python script to **automate image resizing and format conversion** in bulk using the `Pillow` library. Ideal for preparing images for web, social media, or batch processing.

---

## 🚀 Features

- ✅ Resize all images in a folder to a fixed width and height
- ✅ Convert images to a specified format (e.g., `.jpg`, `.png`)
- ✅ Supports JPG, PNG, BMP, TIFF, and more
- ✅ Automatically creates output folder
- ✅ Fast and easy automation with Python

---

## 📦 Requirements

- Python 3.x
- Pillow (Python Imaging Library)

Install dependencies:
```bash
pip install pillow

🛠️ How to Use
Place all input images in the input_images/ folder.

Run the script:
python image_resizer.py

Processed images will be saved to the output_images/ folder.

⚙️ Configuration
Edit the script to adjust:

resize_to = (800, 600)           
output_format = "JPEG"           
output_extension = ".jpg"        


📁 Folder Structure
image-resizer-tool/
├── batch_image_automation.py
├── input_images/
│   ├── img1.png
│   ├── photo2.jpg
├── output_images/
├── README.md


🔧 Future Enhancements
CLI support with argparse

Aspect ratio preserving option

Compression and watermarking

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Reddy Ramanjaneyulu

