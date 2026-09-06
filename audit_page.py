import re
import os

with open('template.html', 'r', encoding='utf-8') as f:
    t = f.read()

print("--- PLACEHOLDERS IN TEMPLATE.HTML ---")
placeholders = set(re.findall(r'__[A-Z0-9_]+__', t))
print("Found placeholders:", sorted(list(placeholders)))

print("\n--- SECTIONS FOUND ---")
for m in re.finditer(r'<section[^>]*id="([^"]+)"', t):
    print("Section ID:", m.group(1))

print("\n--- TEXT AUDIT ---")
forbidden = [
    "INDUSTRY 5.0 MENTOR",
    "ACTIVE DEFENSE ADVISORY",
    "Official Inauguration Timetable",
    "schedule-fullscreen-section"
]
for text in forbidden:
    count = t.count(text)
    print(f"'{text}': {count} occurrences")

required = [
    "DR N.MARIE WILSON",
    "SOUNDARRAJ KANNAN",
    "LEUKQUANT 2026",
    "SEP 07, 2026",
    "Ground Floor Auditorium",
    "openRoyalBooklet",
    "openOfficialCardModal",
    "addToCalendar"
]
for text in required:
    count = t.count(text)
    print(f"'{text}': {count} occurrences")
