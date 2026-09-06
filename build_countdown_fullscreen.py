# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Countdown CSS to be Fullscreen Pinned Diorama
css_pattern = r'/\*\s*=========================================================\s*6\.\s*LIVE COUNTDOWN.*?(?=/\*\s*=========================================================\s*7\.|\.footer-classic)'

new_countdown_css = """/* =========================================================
     6. FULLSCREEN PINNED LIVE COUNTDOWN DIORAMA
     ========================================================= */
  .countdown-enhanced-section {
    position: relative;
    width: 100%;
    min-height: 100vh;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: radial-gradient(ellipse at center, #131F37 0%, #090E1A 75%, #050810 100%);
    overflow: hidden;
    padding: 24px 20px;
    z-index: 10;
    box-sizing: border-box;
  }

  .countdown-ambient-aura {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(900px, 95vw);
    height: min(700px, 85vh);
    background: radial-gradient(circle at center, rgba(0, 102, 255, 0.25) 0%, rgba(212, 175, 55, 0.18) 40%, transparent 70%);
    filter: blur(80px);
    pointer-events: none;
    z-index: 0;
  }

  .countdown-orbital-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(680px, 92vw);
    height: min(680px, 92vw);
    border: 1.5px dashed rgba(212, 175, 55, 0.35);
    border-radius: 50%;
    pointer-events: none;
    z-index: 1;
    animation: ringRotate 30s linear infinite;
  }
  .countdown-orbital-ring::after {
    content: '';
    position: absolute;
    top: 10px;
    left: 50%;
    width: 12px;
    height: 12px;
    background: #D4AF37;
    border-radius: 50%;
    box-shadow: 0 0 16px #D4AF37;
  }

  @keyframes ringRotate {
    0% { transform: translate(-50%, -50%) rotate(0deg); }
    100% { transform: translate(-50%, -50%) rotate(360deg); }
  }

  .countdown-container-stage {
    position: relative;
    z-index: 2;
    max-width: 960px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 2px solid rgba(212, 175, 55, 0.4);
    border-radius: 32px;
    padding: clamp(24px, 4vw, 44px) clamp(16px, 3vw, 36px);
    box-shadow: 0 35px 90px rgba(0, 0, 0, 0.7), inset 0 1px 1px rgba(255, 255, 255, 0.15), 0 0 40px rgba(0, 102, 255, 0.2);
    margin: 0 auto;
  }

  .countdown-eyebrow-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(212, 175, 55, 0.15);
    border: 1.5px solid #D4AF37;
    color: #FEF3C7;
    padding: 6px 20px;
    border-radius: var(--radius-full);
    font-family: var(--font-royal);
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    box-shadow: 0 4px 16px rgba(212, 175, 55, 0.25);
    margin-bottom: 12px;
  }

  .countdown-date-display {
    font-family: var(--font-royal);
    font-size: clamp(28px, 5.5vw, 54px);
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
    background: linear-gradient(135deg, #FFFFFF 0%, #FEF3C7 50%, #D4AF37 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 20px rgba(212, 175, 55, 0.3);
  }

  .date-sub-text {
    font-family: var(--font-mono);
    font-size: clamp(11px, 2vw, 13.5px);
    color: #93C5FD;
    font-weight: 700;
    letter-spacing: 0.1em;
    margin-bottom: 24px;
    text-transform: uppercase;
  }

  .countdown-flip-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: clamp(10px, 2vw, 20px);
    width: 100%;
    max-width: 680px;
    margin: 12px 0 24px 0;
  }

  .countdown-flip-card {
    background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
    border: 2px solid rgba(212, 175, 55, 0.55);
    border-radius: 20px;
    padding: clamp(14px, 2.5vw, 24px) clamp(8px, 1.5vw, 16px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.15), 0 0 20px rgba(212, 175, 55, 0.15);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease;
  }
  .countdown-flip-card:hover {
    transform: translateY(-4px) scale(1.03);
    border-color: #FEF3C7;
    box-shadow: 0 20px 45px rgba(0, 102, 255, 0.35), 0 0 30px rgba(212, 175, 55, 0.4);
  }

  .countdown-flip-card::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 1px;
    background: rgba(0, 0, 0, 0.4);
    box-shadow: 0 1px 0 rgba(255, 255, 255, 0.08);
  }

  .countdown-flip-num {
    font-family: var(--font-mono);
    font-size: clamp(30px, 5.5vw, 56px);
    font-weight: 900;
    color: #FEF3C7;
    line-height: 1;
    text-shadow: 0 2px 14px rgba(212, 175, 55, 0.5);
    margin-bottom: 6px;
    letter-spacing: -0.02em;
  }

  .countdown-flip-lbl {
    font-family: var(--font-royal);
    font-size: clamp(9px, 1.4vw, 12px);
    font-weight: 800;
    color: #94A3B8;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }

  .countdown-actions-wrap {
    display: flex;
    gap: 12px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 6px;
  }

  @media (max-width: 850px) {
    .countdown-enhanced-section {
      padding: 16px 10px;
    }
    .countdown-container-stage {
      padding: 20px 14px;
      border-radius: 22px;
    }
    .countdown-flip-grid {
      gap: 8px;
      margin: 8px 0 18px 0;
    }
    .countdown-flip-card {
      padding: 12px 4px;
      border-radius: 14px;
    }
    .countdown-flip-num {
      font-size: 28px;
    }
    .countdown-flip-lbl {
      font-size: 8.5px;
    }
    .date-sub-text {
      margin-bottom: 14px;
    }
  }

"""

html = re.sub(css_pattern, new_countdown_css, html, flags=re.DOTALL)

# 2. Update Countdown HTML
html_cd_pattern = r'<section class="countdown-enhanced-section" id="countdown">.*?</section>'

new_cd_html = """<section class="countdown-enhanced-section" id="countdown">
    <div class="countdown-ambient-aura" id="cd-aura"></div>
    <div class="countdown-orbital-ring" id="cd-ring"></div>

    <div class="countdown-container-stage" id="cd-stage">
      <div class="countdown-eyebrow-pill" id="cd-pill">
        <span>👑 Grand Launch Live Countdown</span>
      </div>

      <h2 class="countdown-date-display" id="countdown-heading">
        SEP 07, 2026 &bull; 09:30 AM IST
      </h2>

      <div class="date-sub-text" id="cd-subtext">
        MONDAY &bull; GROUND FLOOR AUDITORIUM &bull; JEPPIAAR INSTITUTE OF TECHNOLOGY
      </div>

      <div class="countdown-flip-grid" id="countdown-grid">
        <div class="countdown-flip-card">
          <div class="countdown-flip-num" id="cd-days">00</div>
          <div class="countdown-flip-lbl">DAYS</div>
        </div>
        <div class="countdown-flip-card">
          <div class="countdown-flip-num" id="cd-hours">00</div>
          <div class="countdown-flip-lbl">HOURS</div>
        </div>
        <div class="countdown-flip-card">
          <div class="countdown-flip-num" id="cd-mins">00</div>
          <div class="countdown-flip-lbl">MINUTES</div>
        </div>
        <div class="countdown-flip-card">
          <div class="countdown-flip-num" id="cd-secs">00</div>
          <div class="countdown-flip-lbl">SECONDS</div>
        </div>
      </div>

      <div id="countdown-live-msg" style="display: none; font-family: var(--font-royal); font-size: 22px; font-weight: 800; color: #D4AF37; margin-bottom: 18px; text-shadow: 0 0 15px rgba(212,175,55,0.7);">
        ✨ The Grand Launch is Live!
      </div>

      <div class="countdown-actions-wrap" id="cd-actions">
        <button class="btn-material-primary" onclick="addToCalendar()">
          <span>📅 Add to Calendar (.ics)</span>
        </button>
        <button class="btn-material-secondary" onclick="window.location.href='#venue'" style="background: rgba(255,255,255,0.1); color: #FEF3C7; border-color: #D4AF37;">
          <span>📍 Campus Map &amp; Navigation</span>
        </button>
      </div>
    </div>
  </section>"""

html = re.sub(html_cd_pattern, new_cd_html, html, flags=re.DOTALL)

# 3. Update ScrollTrigger for Fullscreen Pinning and Pause
js_cd_trigger_pattern = r'//\s*\(F\)\s*COUNTDOWN SCALE.*?\}\s*\n\s*\}\s*\n\s*//\s*4\.\s*Live Countdown'

new_cd_trigger = """// (F) FULLSCREEN PINNED COUNTDOWN SCROLL ANIMATION (#countdown)
      const cdSection = document.getElementById('countdown');
      const cdStage = document.getElementById('cd-stage');
      const cdRing = document.getElementById('cd-ring');
      const cdHeading = document.getElementById('countdown-heading');
      const cdCards = document.querySelectorAll('.countdown-flip-card');

      if (cdSection && cdStage) {
        // Pinned Fullscreen Scroll Scene
        const cdTl = gsap.timeline({
          scrollTrigger: {
            trigger: '#countdown',
            start: 'top top',
            end: '+=1200',
            pin: true,
            pinSpacing: true,
            scrub: 1,
            invalidateOnRefresh: true,
            onEnter: () => {
              gsap.to('#cd-aura', { scale: 1.25, opacity: 1, duration: 1.0 });
            },
            onLeaveBack: () => {
              gsap.to('#cd-aura', { scale: 1, opacity: 0.8, duration: 0.8 });
            }
          }
        });

        // Entrance scale & glow
        cdTl.fromTo(cdStage,
          { scale: 0.88, opacity: 0.6, y: 40 },
          { scale: 1.0, opacity: 1, y: 0, ease: 'power2.out', duration: 0.4 }
        );

        // Orbital ring acceleration during scroll
        if (cdRing) {
          cdTl.to(cdRing, { rotate: 180, scale: 1.15, ease: 'none', duration: 0.6 }, 0);
        }

        // Heading golden pulse
        if (cdHeading) {
          cdTl.fromTo(cdHeading,
            { scale: 0.95 },
            { scale: 1.05, ease: 'power1.inOut', duration: 0.5 },
            0.1
          );
        }

        // Staggered Flip Cards bounce
        if (cdCards.length > 0) {
          cdTl.fromTo(cdCards,
            { y: 30, opacity: 0.7, scale: 0.92 },
            { y: 0, opacity: 1, scale: 1, stagger: 0.08, ease: 'back.out(1.7)', duration: 0.5 },
            0.2
          );
        }

        // Actions entrance
        cdTl.fromTo('#cd-actions',
          { y: 20, opacity: 0 },
          { y: 0, opacity: 1, ease: 'power2.out', duration: 0.3 },
          0.5
        );
      }
    }

// 4. Live Countdown"""

html = re.sub(js_cd_trigger_pattern, new_cd_trigger, html, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html with Fullscreen Pinned Live Countdown!")
