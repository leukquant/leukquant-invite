from PIL import Image, ImageFilter, ImageOps
import numpy as np
import base64
import json
import os

def remove_ivory_background(img_path, output_path, ivory_rgb=(246, 240, 228), tolerance=38, smoothness=1.5):
    img = Image.open(img_path).convert('RGBA')
    data = np.array(img, dtype=np.float32)
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
    
    # Distance from target ivory paper background
    ir, ig, ib = ivory_rgb
    dist = np.sqrt((r - ir)**2 + (g - ig)**2 + (b - ib)**2)
    
    # Create smooth alpha mask
    new_a = np.clip((dist - (tolerance - 15)) / 20.0, 0, 1) * 255.0
    
    # Where original alpha was low, keep it low
    new_a = np.minimum(new_a, a)
    
    # Defringe color towards foreground
    data[:, :, 3] = new_a
    result = Image.fromarray(np.uint8(data), 'RGBA')
    
    # Crop transparent borders
    bbox = result.getbbox()
    if bbox:
        result = result.crop(bbox)
        
    result.save(output_path, 'PNG', optimize=True)
    print(f"Saved clean logo: {output_path} (Size: {result.size})")
    return result

# Create clean versions directory
os.makedirs('clean_assets', exist_ok=True)

# 1. Leukquant Logo: Clean from logo_thumb and leukquant_logo
remove_ivory_background('extracted/leukquant_logo.png', 'clean_assets/leukquant_logo.png', tolerance=35)
if os.path.exists('inspect/logo_thumb.png'):
    thumb = Image.open('inspect/logo_thumb.png').convert('RGBA')
    thumb.save('clean_assets/leukquant_navbar_logo.png', 'PNG')

# 2. Top Crest
remove_ivory_background('extracted/top_crest.png', 'clean_assets/top_crest.png', tolerance=35)

# 3. JIT Crest
remove_ivory_background('extracted/jit_crest.png', 'clean_assets/jit_crest.png', tolerance=35)

# 4. NBA Logo
remove_ivory_background('extracted/nba_logo.png', 'clean_assets/nba_logo.png', tolerance=32)

# 5. NAAC Seal
remove_ivory_background('extracted/naac_seal.png', 'clean_assets/naac_seal.png', tolerance=32)

# 6. Mascot - use ultra-clean 952x1024 mascot_clean.png
mascot_clean = Image.open('extracted/mascot_clean.png').convert('RGBA')
# Resize with Lanczos to crisp 480px width
aspect = mascot_clean.height / mascot_clean.width
mascot_hd = mascot_clean.resize((480, int(480 * aspect)), Image.Resampling.LANCZOS)
mascot_hd.save('clean_assets/mascot.png', 'PNG', optimize=True)
print(f"Saved ultra-clean mascot: clean_assets/mascot.png (Size: {mascot_hd.size})")

# 7. Guest Photo
guest = Image.open('extracted/guest_photo.png')
guest.save('clean_assets/guest_photo.png', 'PNG')
print(f"Saved guest photo: clean_assets/guest_photo.png")
