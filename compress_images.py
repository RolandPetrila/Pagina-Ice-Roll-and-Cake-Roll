from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                img = img.convert("RGB")  # Ensure compatibility
                output_file = output_path.rsplit('.', 1)[0] + ".webp"
                img.save(output_file, "WEBP", optimize=True, quality=quality)
                print(f"Compressed: {filename} -> {output_file}")

if __name__ == "__main__":
    input_folder = "assets/images"
    output_folder = "assets/images/compressed"
    compress_images(input_folder, output_folder)