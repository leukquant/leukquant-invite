import json
import os
import base64

with open(r'extracted\assets.json', 'r', encoding='utf-8') as f:
    assets = json.load(f)

print("Current assets in assets.json:")
for k, v in assets.items():
    print(f"  {k}: length {len(v)}, prefix: {v[:50]}")

print("\nFiles in extracted:")
for f in os.listdir('extracted'):
    if f.endswith(('.png', '.jpg')):
        size = os.path.getsize(os.path.join('extracted', f))
        print(f"  {f}: {size} bytes")

print("\nFiles in inspect:")
for f in os.listdir('inspect'):
    if f.endswith(('.png', '.jpg')):
        size = os.path.getsize(os.path.join('inspect', f))
        print(f"  {f}: {size} bytes")
