# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Schedule CSS
schedule_css = """  /* =========================================================
     3B. SECTION 2B: OFFICIAL INAUGURATION SCHEDULE (FULL-SCREEN PINNED)
     ========================================================= */
  .schedule-fullscreen-section {
    position: relative;
    min-height: 100vh;
    background: radial-gradient(circle at center 40%, #152238 0%, #0A101D 70%, #050811 100%);
    color: #F8FAFC;
    padding: 90px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    z-index: 2;
  }

  .schedule-gold-aura {
    position: absolute;
    top: 35%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 900px;
    height: 700px;
    border-radius: 50%;
    background: radial-gradient(ellipse at center, rgba(212, 175, 55, 0.22) 0%, rgba(0, 102, 255, 0.1) 50%, transparent 75%);
    filter: blur(75px);
    pointer-events: none;
    z-index: 0;
  }

  .schedule-container-card {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1180px;
    margin: 0 auto;
    background: rgba(17, 26, 46, 0.85);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 2px solid rgba(212, 175, 55, 0.55);
    border-radius: 28px;
    padding: 44px 36px;
    box-shadow: 0 40px 100px rgba(0, 0, 0, 0.7), 0 0 45px rgba(212, 175, 55, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.15);
  }

  .schedule-header-center {
    text-align: center;
    margin-bottom: 32px;
  }

  .schedule-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(212, 175, 55, 0.15);
    border: 1.5px solid #D4AF37;
    color: #FDE68A;
    padding: 6px 20px;
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    box-shadow: 0 6px 16px rgba(212, 175, 55, 0.25);
    margin-bottom: 14px;
  }

  .schedule-hero-date {
    font-family: var(--font-royal);
    font-size: clamp(30px, 5.5vw, 56px);
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: 0.04em;
    margin-bottom: 10px;
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
    background: linear-gradient(135deg, #FFFFFF 0%, #FEF3C7 50%, #D4AF37 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .schedule-time-vip-banner {
    display: inline-flex;
    align-items: center;
    gap: 16px;
    background: linear-gradient(90deg, rgba(212, 175, 55, 0.25) 0%, rgba(0, 102, 255, 0.25) 100%);
    border: 1.5px solid #D4AF37;
    padding: 10px 28px;
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: clamp(14px, 2.2vw, 19px);
    font-weight: 800;
    color: #FEF3C7;
    letter-spacing: 0.08em;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 20px rgba(212, 175, 55, 0.35);
    margin-bottom: 8px;
  }

  .schedule-venue-subtext {
    font-family: var(--font-body);
    font-size: 14.5px;
    color: #CBD5E1;
    font-weight: 600;
    margin-top: 6px;
  }

  /* Schedule Flow Timeline Grid */
  .schedule-timeline-grid {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin: 32px 0 24px 0;
  }

  .schedule-timeline-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1.5px solid rgba(212, 175, 55, 0.3);
    border-radius: 18px;
    padding: 18px 22px;
    display: grid;
    grid-template-columns: 160px 1fr auto;
    gap: 20px;
    align-items: center;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .schedule-timeline-card:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: #D4AF37;
    transform: translateX(6px);
    box-shadow: 0 12px 30px rgba(212, 175, 55, 0.25);
  }

  .timeline-time-badge {
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    border: 1.5px solid #D4AF37;
    color: #FEF3C7;
    font-family: var(--font-mono);
    font-size: 12.5px;
    font-weight: 800;
    padding: 8px 14px;
    border-radius: 10px;
    text-align: center;
    letter-spacing: 0.05em;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    white-space: nowrap;
  }

  .timeline-info-wrap h4 {
    font-family: var(--font-royal);
    font-size: 16px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.03em;
    margin-bottom: 4px;
  }

  .timeline-info-wrap p {
    font-size: 12.5px;
    color: #94A3B8;
    line-height: 1.45;
  }

  .timeline-speaker-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-mono);
    font-size: 10.5px;
    font-weight: 700;
    color: #FDE68A;
    background: rgba(212, 175, 55, 0.18);
    border: 1px solid rgba(212, 175, 55, 0.4);
    padding: 4px 12px;
    border-radius: var(--radius-full);
    text-transform: uppercase;
    white-space: nowrap;
  }

  .schedule-actions-row {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 24px;
  }

  @media (max-width: 850px) {
    .schedule-container-card {
      padding: 24px 16px;
      border-radius: 20px;
    }
    .schedule-timeline-card {
      grid-template-columns: 1fr;
      gap: 10px;
      padding: 14px 14px;
    }
    .timeline-time-badge {
      width: fit-content;
      font-size: 11px;
      padding: 5px 10px;
    }
    .timeline-info-wrap h4 {
      font-size: 14.5px;
    }
    .timeline-info-wrap p {
      font-size: 11.5px;
    }
    .schedule-hero-date {
      font-size: clamp(24px, 6.5vw, 36px);
    }
    .schedule-time-vip-banner {
      font-size: 13px;
      padding: 8px 16px;
      flex-direction: column;
      gap: 4px;
    }
  }"""

# Insert schedule CSS before Section 3 CSS
css_pattern = r'(\/\* =+\s*4\.\s*SECTION 3:)'
content = re.sub(css_pattern, schedule_css + '\n\n  \\1', content)


# 2. Add Schedule HTML right after #invitation section
schedule_html = """  <!-- =========================================================
       SECTION 2B: OFFICIAL INAUGURATION SCHEDULE (FULL-SCREEN PINNED)
       ========================================================= -->
  <section class="schedule-fullscreen-section" id="schedule">
    <div class="schedule-gold-aura"></div>

    <div class="schedule-container-card" id="schedule-card">
      <div class="schedule-header-center">
        <span class="schedule-badge-pill">👑 Official Inauguration Timetable &bull; 2026</span>
        <h2 class="schedule-hero-date">MONDAY, SEPTEMBER 07, 2026</h2>
        
        <div class="schedule-time-vip-banner">
          <span>⏰ 10:30 AM IST ONWARDS</span>
          <span>&bull;</span>
          <span>📍 GROUND FLOOR AUDITORIUM, JIT</span>
        </div>
        
        <p class="schedule-venue-subtext">
          Jeppiaar Institute of Technology, Kunnam, Sriperumbudur, Chennai &bull; Autonomous Institution
        </p>
      </div>

      <!-- Schedule Flow Timeline Cards -->
      <div class="schedule-timeline-grid">
        <!-- Event 1 -->
        <div class="schedule-timeline-card">
          <div class="timeline-time-badge">10:30 AM &ndash; 10:45 AM</div>
          <div class="timeline-info-wrap">
            <h4>Grand Inaugural Assembly &amp; Lamp Lighting</h4>
            <p>Reception of Chief Guest, Traditional Lamp Lighting &amp; Invocational Ceremony.</p>
          </div>
          <span class="timeline-speaker-pill">👑 Inaugural Ceremony</span>
        </div>

        <!-- Event 2 -->
        <div class="schedule-timeline-card">
          <div class="timeline-time-badge">10:45 AM &ndash; 11:15 AM</div>
          <div class="timeline-info-wrap">
            <h4>Presidential Address by Chief Guest</h4>
            <p>Keynote address by <strong>Dr. N. Marie Wilson</strong> (Minister for Finance, Pensions &amp; JIT Chairman).</p>
          </div>
          <span class="timeline-speaker-pill">⭐ Dr. N. Marie Wilson</span>
        </div>

        <!-- Event 3 -->
        <div class="schedule-timeline-card">
          <div class="timeline-time-badge">11:15 AM &ndash; 11:45 AM</div>
          <div class="timeline-info-wrap">
            <h4>Special Guest Keynote Address</h4>
            <p>Industry 5.0 Active Defense insights by <strong>Soundarraj Kannan</strong> (Director, KRP Tech Solutions).</p>
          </div>
          <span class="timeline-speaker-pill">🛡️ Soundarraj Kannan</span>
        </div>

        <!-- Event 4 -->
        <div class="schedule-timeline-card">
          <div class="timeline-time-badge">11:45 AM &ndash; 12:15 PM</div>
          <div class="timeline-info-wrap">
            <h4>LeukQuant AI Platform Live Unveiling</h4>
            <p>Live cyber demonstration of AI Autonomous Active Deception Architecture &amp; Enterprise Rollout.</p>
          </div>
          <span class="timeline-speaker-pill">⚡ LeukQuant AI Demo</span>
        </div>

        <!-- Event 5 -->
        <div class="schedule-timeline-card">
          <div class="timeline-time-badge">12:15 PM &ndash; 12:30 PM</div>
          <div class="timeline-info-wrap">
            <h4>Felicitations &amp; Networking High Tea</h4>
            <p>Vote of Thanks by JIT Innovation Foundation leadership followed by networking session.</p>
          </div>
          <span class="timeline-speaker-pill">☕ High Tea &amp; Close</span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="schedule-actions-row">
        <button class="btn-material-primary" onclick="addToCalendar()">
          📅 Add Schedule to Calendar (.ics)
        </button>
        <button class="btn-material-outline" onclick="shareWhatsapp()" style="color:#FFF; background:rgba(255,255,255,0.08); border-color:rgba(212,175,55,0.4);">
          💬 Share Schedule on WhatsApp
        </button>
        <a href="https://www.google.com/maps/search/?api=1&query=Jeppiaar+Institute+of+Technology+Kunnam" target="_blank" rel="noopener" class="btn-material-outline" style="color:#FFF; background:rgba(255,255,255,0.08); border-color:rgba(212,175,55,0.4);">
          🧭 Get Auditorium Directions
        </a>
      </div>
    </div>
  </section>"""

# Insert schedule HTML before Section 3 HTML
html_pattern = r'(<!-- =+\s*SECTION 3:)'
content = re.sub(html_pattern, schedule_html + '\n\n  \\1', content)


# 3. Add GSAP Pinned Animation for #schedule in JS
js_schedule_anim = """      // (C2) SECTION 2B: OFFICIAL INAUGURATION SCHEDULE PINNED FULL-SCREEN
      gsap.fromTo('#schedule-card',
        { y: 60, opacity: 0, scale: 0.95 },
        {
          y: 0,
          opacity: 1,
          scale: 1.0,
          duration: 1.1,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: '#schedule',
            start: 'top 80%',
            invalidateOnRefresh: true
          }
        }
      );

      gsap.from('.schedule-timeline-card', {
        x: -40,
        opacity: 0,
        stagger: 0.15,
        duration: 0.8,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '#schedule',
          start: 'top 70%',
          invalidateOnRefresh: true
        }
      });"""

js_pattern = r'(\/\/\s*\(D\)\s*DIORAMA SHOWCASE)'
content = re.sub(js_pattern, js_schedule_anim + '\n\n      \\1', content)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Added Official Inauguration Schedule section successfully! Total length: {len(content)} characters.")
