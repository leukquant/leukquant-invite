import json
import base64
import os

print("Compiling template.html into index.html and invitation.html...")

# 1. Read template.html
with open('template.html', 'r', encoding='utf-8') as f:
    tpl = f.read()

# 2. Encode helper
def get_data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = 'image/png' if ext == '.png' else 'image/jpeg'
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

# Specific mascot as required by user
mascot_path = r'extracted\mascot_trans.png'
if not os.path.exists(mascot_path):
    mascot_path = r'extracted/mascot_trans.png'

mascot_uri = get_data_uri(mascot_path)
jit_crest_uri = get_data_uri('clean_assets/jit_crest.png')
naac_uri = get_data_uri('clean_assets/naac_seal.png')
nba_uri = get_data_uri('clean_assets/nba_logo.png')
logo_uri = get_data_uri('clean_assets/leukquant_logo.png')
guest_uri = get_data_uri('clean_assets/guest_photo.png')
guest_soundarraj_uri = get_data_uri('clean_assets/guest_soundarraj.png')
authentic_card_uri = get_data_uri('clean_assets/authentic_invitation_card.jpg')

iso_launch_stage_uri = get_data_uri('assets_3d/iso_launch_stage.jpg')
iso_cyber_shield_uri = get_data_uri('assets_3d/iso_cyber_shield.jpg')
iso_calendar_3d_uri = get_data_uri('assets_3d/iso_calendar_3d.jpg')
iso_location_auditorium_uri = get_data_uri('assets_3d/iso_location_auditorium.jpg')

# 3. Perform replacements
rendered = tpl.replace('__JIT_CREST__', jit_crest_uri)
rendered = rendered.replace('__NAAC_SEAL__', naac_uri)
rendered = rendered.replace('__NBA_LOGO__', nba_uri)
rendered = rendered.replace('__MASCOT__', mascot_uri)
rendered = rendered.replace('__LEUKQUANT_LOGO__', logo_uri)
rendered = rendered.replace('__GUEST_PHOTO__', guest_uri)
rendered = rendered.replace('__GUEST_SOUNDARRAJ__', guest_soundarraj_uri)
rendered = rendered.replace('__AUTHENTIC_CARD__', authentic_card_uri)

rendered = rendered.replace('__ISO_LAUNCH_STAGE__', iso_launch_stage_uri)
rendered = rendered.replace('__ISO_CYBER_SHIELD__', iso_cyber_shield_uri)
rendered = rendered.replace('__ISO_CALENDAR_3D__', iso_calendar_3d_uri)
rendered = rendered.replace('__ISO_LOCATION_AUDITORIUM__', iso_location_auditorium_uri)
rendered = rendered.replace('__SHARE_IMAGE__', mascot_uri)

# 4. Write output files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered)

with open('invitation.html', 'w', encoding='utf-8') as f:
    f.write(rendered)

print(f"DONE! Written {len(rendered)} bytes to index.html & invitation.html")

