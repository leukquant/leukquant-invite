import json
import sys

print("Loading fonts and assets...")
with open(r'extracted\fonts.json', 'r', encoding='utf-8') as f:
    fonts = json.load(f)

with open(r'extracted\assets.json', 'r', encoding='utf-8') as f:
    assets = json.load(f)

with open(r'generate_website.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("Files read successfully. Total length:", len(content))
