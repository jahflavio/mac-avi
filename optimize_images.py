import os
from PIL import Image

def optimize_images(input_folder, output_folder, max_size=(1920, 1080), quality=75):
    """
    Optimizes images by resizing them and converting to WebP format with compression.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    for root, dirs, files in os.walk(input_folder):
        # Create corresponding subdirectories in output_folder
        relative_path = os.path.relpath(root, input_folder)
        dest_dir = os.path.join(output_folder, relative_path)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for filename in files:
            if filename.lower().endswith(supported_formats):
                img_path = os.path.join(root, filename)
                
                # Create output filename with .webp extension
                name_without_ext = os.path.splitext(filename)[0]
                output_path = os.path.join(dest_dir, f"{name_without_ext}.webp")

                try:
                    with Image.open(img_path) as img:
                        # Convert to RGB if necessary (e.g., for PNG with transparency if saving as JPG, 
                        # but WebP supports transparency. However, some PNGs might behave better if converted)
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGBA")
                        else:
                            img = img.convert("RGB")

                        # Resize if image is larger than max_size
                        img.thumbnail(max_size, Image.Resampling.LANCZOS)

                        # Save as WebP with compression
                        img.save(output_path, "WEBP", quality=quality, optimize=True)
                        print(f"Optimized: {img_path} -> {output_path}")
                
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    # Define paths - relative to the project root where the script will run
    input_dir = os.path.join("images", "Fotos")
    output_dir = os.path.join("images", "Fotos_Optimized")
    
    # Run optimization
    print("Starting image optimization...")
    optimize_images(input_dir, output_dir)
    print("Image optimization complete.")
