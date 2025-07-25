import os
from PIL import Image

# === CONFIG ===
input_folder = "input_images"         # Folder with source images
output_folder = "output_images"       # Folder to save processed images
resize_to = (800, 600)                # Target size: (width, height)
output_format = "JPEG"                # Target format: "JPEG", "PNG", etc.
output_extension = ".jpg"             # Extension matching format

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image types
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")

# === AUTOMATED TASK ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + output_extension)

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")            # Ensures compatibility with JPEG
                img = img.resize(resize_to)         # Resize image
                img.save(output_path, output_format)
                print(f"✅ Processed: {filename}")
        except Exception as e:
            print(f"❌ Failed: {filename} | Error: {e}")

print("\n🎯 Automation Complete: All images processed.")
