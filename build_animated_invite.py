import json
import base64
import os

def file_to_data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = 'image/png' if ext == '.png' else 'image/jpeg'
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

print("Encoding assets...")

# Specific requirement: Use C:\Users\rickj\.cache\LEUKQUANT_INVITE\extracted\mascot_trans.png as mascot
mascot_path = r'extracted/mascot_trans.png'
if not os.path.exists(mascot_path):
    mascot_path = r'C:\Users\rickj\.cache\LEUKQUANT_INVITE\extracted\mascot_trans.png'

assets = {
    "top_crest": file_to_data_uri('clean_assets/top_crest.png'),
    "guest_photo": file_to_data_uri('clean_assets/guest_photo.png'),
    "mascot": file_to_data_uri(mascot_path),
    "leukquant_logo": file_to_data_uri('clean_assets/leukquant_logo.png'),
    "leukquant_navbar_logo": file_to_data_uri('clean_assets/leukquant_navbar_logo.png'),
    "jit_crest": file_to_data_uri('clean_assets/jit_crest.png'),
    "nba_logo": file_to_data_uri('clean_assets/nba_logo.png'),
    "naac_seal": file_to_data_uri('clean_assets/naac_seal.png'),
}

with open(r'extracted/assets.json', 'w', encoding='utf-8') as f:
    json.dump(assets, f, indent=2)

print(f"Updated extracted/assets.json successfully! Mascot size in base64: {len(assets['mascot'])} chars")
