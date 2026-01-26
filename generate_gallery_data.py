import os
import json

def generate_gallery_data(optimized_dir, output_js_file):
    """
    Scans the optimized images directory and generates a JS file with a variable 
    containing the image data organized by category.
    """
    categories = ['Corporativo', 'Generales', 'Show', 'Sociales', 'Catalogo']
    gallery_data = []

    for cat in categories:
        cat_path = os.path.join(optimized_dir, cat)
        if not os.path.exists(cat_path):
            print(f"Warning: Category folder not found: {cat_path}")
            continue

        images = []
        for root, dirs, files in os.walk(cat_path):
            for filename in files:
                if filename.lower().endswith('.webp'):
                    # Create a relative path from the project root
                    # The optimized_dir is likely 'images/Fotos_Optimized'
                    rel_dir = os.path.relpath(root, os.path.dirname(os.path.dirname(optimized_dir)))
                    img_src = os.path.join(rel_dir, filename).replace('\\', '/')
                    images.append({
                        'src': img_src,
                        'alt': filename.replace('.webp', '').replace('_', ' ').capitalize()
                    })
        
        if images:
            gallery_data.append({
                'category': cat,
                'images': images
            })

    # Generate the JS file content
    js_content = f"const galleryData = {json.dumps(gallery_data, indent=2)};"
    
    with open(output_js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Gallery data generated successfully at: {output_js_file}")

if __name__ == "__main__":
    base_dir = "images/Fotos_Optimized"
    output_file = "js/gallery_data.js"
    
    # Ensure js directory exists
    if not os.path.exists("js"):
        os.makedirs("js")
        
    generate_gallery_data(base_dir, output_file)
