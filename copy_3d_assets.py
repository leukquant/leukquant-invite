import shutil
import os

os.makedirs('assets_3d', exist_ok=True)

brain_dir = r'C:\Users\rickj\.gemini\antigravity-ide\brain\00dc788f-ab58-4e1f-987c-b57ba155340b'

for f in os.listdir(brain_dir):
    if f.startswith('iso_launch_stage') and f.endswith('.jpg'):
        shutil.copy(os.path.join(brain_dir, f), 'assets_3d/iso_launch_stage.jpg')
    elif f.startswith('iso_cyber_shield') and f.endswith('.jpg'):
        shutil.copy(os.path.join(brain_dir, f), 'assets_3d/iso_cyber_shield.jpg')
    elif f.startswith('iso_calendar_3d') and f.endswith('.jpg'):
        shutil.copy(os.path.join(brain_dir, f), 'assets_3d/iso_calendar_3d.jpg')
    elif f.startswith('iso_location_auditorium') and f.endswith('.jpg'):
        shutil.copy(os.path.join(brain_dir, f), 'assets_3d/iso_location_auditorium.jpg')

print("Copied 3D isometric images to assets_3d folder successfully!")
