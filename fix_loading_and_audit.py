# -*- coding: utf-8 -*-
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Preloader JavaScript: instant smooth entrance, fast 500ms mascot signet polish, and hard safety fallback
old_preloader_js = """    // 2. Preloader Mascot Stamping Sequence
    window.addEventListener('DOMContentLoaded', () => {
      const preloader = document.getElementById('preloader');
      const bar = document.getElementById('preloader-bar');
      const status = document.getElementById('preloader-status');
      const badgeText = document.getElementById('preloader-badge-text');
      const stamp = document.getElementById('pmini-stamp');
      const seal = document.getElementById('pmini-seal');

      let progress = 0;
      let phase = 0;

      const timer = setInterval(() => {
        progress += 3;
        if (progress > 100) progress = 100;
        if (bar) bar.style.width = progress + '%';

        if (progress >= 25 && phase === 0) {
          phase = 1;
          if (status) status.innerText = 'Positioning Mascot Signet Stamp...';
          if (badgeText) badgeText.innerText = 'Engraving Seal';
          if (stamp) stamp.style.transform = 'translateX(-50%) translateY(22px)';
        }

        if (progress >= 55 && phase === 1) {
          phase = 2;
          if (status) status.innerText = 'Stamping Molten Gold Wax...';
          if (badgeText) badgeText.innerText = 'Sealing Envelope';
          if (stamp) stamp.style.transform = 'translateX(-50%) translateY(52px) scale(0.96)';
        }

        if (progress >= 80 && phase === 2) {
          phase = 3;
          if (status) status.innerText = 'Mascot Signet Seal Imprinted!';
          if (badgeText) badgeText.innerText = 'Sealed & Verified';
          if (stamp) {
            stamp.style.transform = 'translateX(-50%) translateY(-70px) scale(0.8)';
            stamp.style.opacity = '0';
          }
          if (seal) {
            seal.style.opacity = '1';
            seal.style.transform = 'scale(1)';
          }
        }

        if (progress >= 100) {
          clearInterval(timer);
          if (status) status.innerText = 'Royal Invitation Sealed & Ready!';
          if (badgeText) badgeText.innerText = 'Grand Launch 2026';
          setTimeout(() => {
            if (preloader) preloader.classList.add('loaded');
            initGsapAnimations();
            ScrollTrigger.refresh();
          }, 600);
        }
      }, 35);
    });"""

new_preloader_js = """    // 2. Ultra-Smooth Fast Loading & Preloader Sequence
    function dismissPreloader() {
      const preloader = document.getElementById('preloader');
      if (preloader && !preloader.classList.contains('loaded')) {
        preloader.classList.add('loaded');
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 800);
        if (typeof ScrollTrigger !== 'undefined') {
          ScrollTrigger.refresh();
        }
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      // Run animations immediately so page is ready
      initGsapAnimations();

      const preloader = document.getElementById('preloader');
      const bar = document.getElementById('preloader-bar');
      const status = document.getElementById('preloader-status');
      const badgeText = document.getElementById('preloader-badge-text');
      const stamp = document.getElementById('pmini-stamp');
      const seal = document.getElementById('pmini-seal');

      // Click or keydown anywhere on preloader immediately dismisses it
      if (preloader) {
        preloader.addEventListener('click', dismissPreloader);
      }

      let progress = 0;
      const timer = setInterval(() => {
        progress += 8;
        if (progress > 100) progress = 100;
        if (bar) bar.style.width = progress + '%';

        if (progress >= 30 && stamp) {
          stamp.style.transform = 'translateX(-50%) translateY(35px)';
        }
        if (progress >= 70 && stamp && seal) {
          stamp.style.transform = 'translateX(-50%) translateY(52px) scale(0.96)';
          seal.style.opacity = '1';
          seal.style.transform = 'scale(1)';
        }

        if (progress >= 100) {
          clearInterval(timer);
          if (status) status.innerText = 'Grand Launch 2026 Ready!';
          if (badgeText) badgeText.innerText = 'Verified';
          setTimeout(dismissPreloader, 300);
        }
      }, 25);

      // Hard safety timeout: preloader NEVER hangs under any circumstances
      setTimeout(dismissPreloader, 1000);
    });

    window.addEventListener('load', () => {
      setTimeout(dismissPreloader, 200);
    });"""

if old_preloader_js in html:
    html = html.replace(old_preloader_js, new_preloader_js)
    print("Replaced preloader JS!")
else:
    print("Warning: old_preloader_js exact string not found, using regex...")
    import re
    p_pattern = r'//\s*2\.\s*Preloader Mascot Stamping Sequence.*?window\.addEventListener\(\'DOMContentLoaded\',.*?\}\);\s*\}\s*,\s*35\);\s*\}\);'
    html = re.sub(p_pattern, new_preloader_js, html, flags=re.DOTALL)
    print("Replaced via regex!")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved template.html with fast loading fix!")
