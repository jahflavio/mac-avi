import os
from PIL import Image

def optimize_catalog_images(source_base, target_base):
    """
    Optimizes images from imagenes_cat and moves them to Fotos_Optimized with categorization.
    """
    # Define mapping: (source_subfolder, target_category)
    mapping = [
        ('equipo', 'Catalogo'),
        ('espectaculos', 'Show')
    ]
    
    # Files to explicitly skip
    skip_files = ['img116.jpg']
    
    # Quality and resizing settings
    quality = 75
    max_size = (1920, 1080)

    for source_fold, target_cat in mapping:
        source_path = os.path.join(source_base, source_fold)
        target_path = os.path.join(target_base, target_cat)
        
        if not os.path.exists(source_path):
            print(f"Skipping {source_path}: Source folder not found.")
            continue
            
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print(f"Created target folder: {target_path}")

        for filename in os.listdir(source_path):
            if filename in skip_files:
                print(f"Explicitly skipping: {filename}")
                continue
                
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    img_path = os.path.join(source_path, filename)
                    with Image.open(img_path) as img:
                        # Convert to RGB if necessary
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                            
                        # Resize
                        img.thumbnail(max_size, Image.Resampling.LANCZOS)
                        
                        # Save path
                        name_no_ext = os.path.splitext(filename)[0]
                        save_name = f"cat_{name_no_ext}.webp" # Add prefix to avoid name collisions
                        save_path = os.path.join(target_path, save_name)
                        
                        img.save(save_path, "WEBP", quality=quality)
                        print(f"Processed: {filename} -> {save_name} in {target_cat}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    src_dir = "images/imagenes_cat"
    dst_dir = "images/Fotos_Optimized"
    
    optimize_catalog_images(src_dir, dst_dir)
