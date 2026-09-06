# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update all date and time strings across template.html
# Replace dates
html = html.replace('September 07, 2026', 'September 10, 2026')
html = html.replace('September 7, 2026', 'September 10, 2026')
html = html.replace('SEP 07, 2026', 'SEP 10, 2026')
html = html.replace('September 07, Monday', 'September 10, Thursday')
html = html.replace('Monday, September 07, 2026', 'Thursday, September 10, 2026')
html = html.replace('MONDAY &bull;', 'THURSDAY &bull;')
html = html.replace('Monday', 'Thursday')

# Replace times to 10:30 AM IST
html = html.replace('09:30 AM IST', '10:30 AM IST')
html = html.replace('09:30 AM', '10:30 AM')
html = html.replace('10:00 AM IST', '10:30 AM IST')

# 2. Update Countdown JS target date
html = re.sub(
    r'targetLaunchDate\s*=\s*new Date\([^)]+\)\.getTime\(\)',
    "targetLaunchDate = new Date('2026-09-10T10:30:00+05:30').getTime()",
    html
)

# 3. Update Calendar .ics generator function
calendar_ics_pattern = r'function addToCalendar\(\)\s*\{.*?\}'

new_calendar_ics = """function addToCalendar() {
      const icsData = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//LeukQuant//Launch Invitation//EN',
        'CALSCALE:GREGORIAN',
        'METHOD:PUBLISH',
        'BEGIN:VEVENT',
        'UID:leukquant-grand-launch-20260910@leukquant.com',
        'DTSTAMP:20260901T000000Z',
        'DTSTART:20260910T050000Z',
        'DTEND:20260910T080000Z',
        'SUMMARY:LeukQuant Grand Launch 2026 | Official Inauguration',
        'DESCRIPTION:Official Grand Launch of LeukQuant - AI-Powered Active Deception & Autonomous Cybersecurity Platform.\\\\nChief Guest: Dr. N. Marie Wilson (Director, JIT).\\\\nSpecial Guest: Soundarraj Kannan (Target Product Security).\\\\nVenue: Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam, Chennai.',
        'LOCATION:Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam, Sriperumbudur, Tamil Nadu 631604',
        'STATUS:CONFIRMED',
        'BEGIN:VALARM',
        'TRIGGER:-PT2H',
        'ACTION:DISPLAY',
        'DESCRIPTION:LeukQuant Grand Launch in 2 Hours',
        'END:VALARM',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('\\r\\n');

      const blob = new Blob([icsData], { type: 'text/calendar;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'LeukQuant_Grand_Launch_Sep10_2026.ics';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('📅 Calendar Event (.ics) Downloaded for Sep 10, 2026!');
    }"""

html = re.sub(calendar_ics_pattern, new_calendar_ics, html, flags=re.DOTALL)

# 4. In the Booklet right page action buttons, add direct link to the Timing & Countdown screen
buttons_pattern = r'<div class="royal-actions-container">.*?</div>'

new_buttons = """<div class="royal-actions-container">
                  <button class="btn-material-primary" onclick="window.location.href='#countdown'" style="background: linear-gradient(135deg, #B45309 0%, #D4AF37 100%); color: #0F172A; font-weight: 800;">
                    <span>⏰ Live Timing &amp; Countdown</span>
                  </button>
                  <button class="btn-material-primary" onclick="window.location.href='#venue'">
                    <span>📍 Venue &amp; Map</span>
                  </button>
                  <button class="btn-material-secondary" onclick="addToCalendar()">
                    <span>📅 Add to Calendar</span>
                  </button>
                </div>"""

html = re.sub(buttons_pattern, new_buttons, html, flags=re.DOTALL)

# 5. In the Hero section, ensure there is also a direct button to the Timing Screen
hero_subtitle_pattern = r'<div class="hero-stage-preview">.*?<div class="hero-scroll-indicator"'

new_hero_preview = """<div class="hero-stage-preview">
      <img src="__ISO_LAUNCH_STAGE__" alt="LeukQuant Launch Stage" class="hero-stage-img">
      <div class="hero-mascot-badge" onclick="mascotPulse()" title="Interact with mascot!">
        <img src="__MASCOT__" alt="Mascot">
        <span style="font-size: 12.5px; font-weight: 700; color: var(--text-heading);">Click Mascot for AI Cheer!</span>
      </div>
    </div>

    <!-- Quick Action Links on Hero -->
    <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 24px; z-index: 5;">
      <button class="btn-material-primary" onclick="smoothScrollTo('#invitation')" style="padding: 10px 22px; font-size: 13px;">
        <span>📖 Open Royal Booklet</span>
      </button>
      <button class="btn-material-secondary" onclick="smoothScrollTo('#countdown')" style="padding: 10px 20px; font-size: 13px; background: rgba(255,255,255,0.85);">
        <span>⏰ Live Countdown &bull; Sep 10</span>
      </button>
    </div>

    <div class="hero-scroll-indicator" """

html = re.sub(hero_subtitle_pattern, new_hero_preview, html, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html with September 10, 2026, 10:30 AM IST and direct Timing Screen navigation!")
