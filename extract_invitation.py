with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="invitation"')
end = text.find('</section>', start)

with open('scratch_html.txt', 'w', encoding='utf-8') as out:
    out.write(text[start-40:end+10])

print("Wrote scratch_html.txt, length:", end - start)
