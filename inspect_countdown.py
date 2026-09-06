with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="countdown"')
end = text.find('</section>', start)

out_text = "--- COUNTDOWN HTML ---\n" + text[start-40:end+10]

css_start = text.find('.countdown-enhanced-section')
if css_start != -1:
    css_end = text.find('/* =========================================================\n     7.', css_start)
    if css_end == -1:
        css_end = text.find('/* =========================================================\n     8.', css_start)
    if css_end == -1:
        css_end = css_start + 2500
    out_text += "\n\n--- COUNTDOWN CSS ---\n" + text[css_start:css_end]

js_start = text.find('// (F) COUNTDOWN')
if js_start == -1:
    js_start = text.find('COUNTDOWN')
if js_start != -1:
    out_text += "\n\n--- COUNTDOWN JS ---\n" + text[js_start:js_start+1500]

with open('scratch_countdown.txt', 'w', encoding='utf-8') as f:
    f.write(out_text)

print("Saved to scratch_countdown.txt")
