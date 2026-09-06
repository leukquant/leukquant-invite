# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the inline official card container and modal from HTML
inline_card_pattern = r'<!-- Authentic Official Invitation Card Inline Container -->.*?<!-- Official Fullscreen Modal -->.*?</div>\s*</div>'
html = re.sub(inline_card_pattern, '', html, flags=re.DOTALL)

# Remove the '📜 Official Card (HD)' button from header hint & action bar
html = html.replace("""<button class="btn-envelope-action" onclick="openOfficialCardModal()" style="background: linear-gradient(135deg, #B45309 0%, #D4AF37 100%); color: #0F172A; font-weight: 800; border-color: #FEF3C7;">📜 View Full Official Card (HD)</button>""", "")

html = html.replace("""<button class="btn-material-primary" onclick="openOfficialCardModal()" style="background: linear-gradient(135deg, #B45309 0%, #D4AF37 100%); color: #0F172A; font-weight: 800;">
                    <span>📜 Official Card (HD)</span>
                  </button>""", "")

# 2. Update CSS for slow, majestic 3D book cover transitions
css_cover_pattern = r'\.book-gate-cover\s*\{[^}]*transition:[^;]*;[^}]*\}'
new_cover_css = """.book-gate-cover {
    position: absolute;
    top: 0;
    height: 100%;
    width: 50%;
    background: linear-gradient(145deg, #1B263B 0%, #0F172A 100%);
    border: 3px solid #D4AF37;
    z-index: 40;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 24px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
    transform-style: preserve-3d;
    backface-visibility: hidden;
    transition: transform 2.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.8s ease, visibility 1.8s;
    cursor: pointer;
    overflow: hidden;
  }"""

html = re.sub(css_cover_pattern, new_cover_css, html, flags=re.DOTALL)

# 3. Update JavaScript openRoyalBooklet for slow, smooth, graceful opening animation
js_open_pattern = r'function openRoyalBooklet\(autoTriggered = false\)\s*\{.*?function replayBookletAnimation\(\)'

new_js_open = """function openRoyalBooklet(autoTriggered = false) {
      if (isBookletOpened && !autoTriggered) return;
      isBookletOpened = true;

      const coverLeft = document.getElementById('gate-cover-left');
      const coverRight = document.getElementById('gate-cover-right');
      const centerSeal = document.getElementById('gate-center-seal');
      const pageLeft = document.getElementById('book-page-left');
      const pageRight = document.getElementById('book-page-right');
      const card = document.getElementById('invitation-card');
      const sheen = document.getElementById('card-sheen');

      if (card) {
        gsap.to(card, { opacity: 1, scale: 1, y: 0, duration: 0.8 });
      }

      // Step 1: Break & fade center seal slowly
      if (centerSeal) {
        gsap.to(centerSeal, {
          scale: 1.3,
          rotate: 20,
          opacity: 0,
          duration: 1.2,
          ease: 'power2.out',
          onComplete: () => {
            centerSeal.classList.add('opened');
          }
        });
      }

      // Step 2: Swing open Left and Right covers in majestic slow 3D motion (Double-Side Open!)
      if (coverLeft && coverRight) {
        coverLeft.classList.add('opened');
        coverRight.classList.add('opened');
        
        gsap.to(coverLeft, {
          rotateY: -140,
          opacity: 0,
          duration: 2.6,
          ease: 'power2.inOut',
          delay: 0.15
        });

        gsap.to(coverRight, {
          rotateY: 140,
          opacity: 0,
          duration: 2.6,
          ease: 'power2.inOut',
          delay: 0.15
        });
      }

      // Step 3: Inner pages unfold slowly from 3D angle into flat spread
      if (pageLeft && pageRight) {
        gsap.fromTo(pageLeft,
          { rotateY: 22, transformOrigin: 'right center' },
          { rotateY: 0, duration: 2.4, ease: 'power2.out', delay: 0.4 }
        );
        gsap.fromTo(pageRight,
          { rotateY: -22, transformOrigin: 'left center' },
          { rotateY: 0, duration: 2.4, ease: 'power2.out', delay: 0.4 }
        );
      }

      // Step 4: Gold sheen sweep across unfolded 2-page spread
      if (sheen) {
        gsap.fromTo(sheen,
          { left: '-150%' },
          { left: '150%', duration: 2.2, ease: 'power2.inOut', delay: 1.2 }
        );
      }

      if (!autoTriggered) {
        showToast('📖 Royal Double-Side Booklet Opened');
      }
    }

    function replayBookletAnimation()"""

html = re.sub(js_open_pattern, new_js_open, html, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html with slow booklet opening and removed official printed card container!")
