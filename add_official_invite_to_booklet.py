# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Section 2 HTML to feature the Official Invitation Card on the booklet
# Let's inspect the buttons in the header hint and add the authentic card view
hint_controls_pattern = r'<div class="envelope-hint-controls">.*?</div>'

new_hint_controls = """<div class="envelope-hint-controls">
          <span class="envelope-hint-pill">👑 Official Royal Booklet &bull; 2026</span>
          <button class="btn-envelope-action" onclick="replayBookletAnimation()">✨ Open / Close Booklet</button>
          <button class="btn-envelope-action" onclick="toggleBookFold()">📖 3D Perspective</button>
          <button class="btn-envelope-action" onclick="openOfficialCardModal()" style="background: linear-gradient(135deg, #B45309 0%, #D4AF37 100%); color: #0F172A; font-weight: 800; border-color: #FEF3C7;">📜 View Full Official Card (HD)</button>
        </div>"""

html = re.sub(hint_controls_pattern, new_hint_controls, html, flags=re.DOTALL)

# Add the official card image on the booklet and an HD card modal
folio_pattern = r'<div class="royal-book-folio" id="invitation-card">.*?</section>'

new_folio_html = """<div class="royal-book-folio" id="invitation-card">
            <div class="card-sheen-overlay" id="card-sheen"></div>

            <!-- 3D DOUBLE-SIDE OPENING COVERS (LEFT & RIGHT GATEFOLD DOORS) -->
            <div class="book-gate-cover gate-left" id="gate-cover-left" onclick="openRoyalBooklet(false)">
              <div class="gate-cover-content">
                <img src="__JIT_CREST__" alt="JIT Crest" class="gate-cover-crest">
                <div class="gate-cover-title">OFFICIAL INVITATION</div>
                <div class="gate-cover-sub">JEPPIAAR INSTITUTE OF TECHNOLOGY</div>
              </div>
            </div>

            <div class="book-gate-cover gate-right" id="gate-cover-right" onclick="openRoyalBooklet(false)">
              <div class="gate-cover-content">
                <img src="__MASCOT__" alt="LeukQuant Mascot" class="gate-cover-crest">
                <div class="gate-cover-title">LEUKQUANT 2026</div>
                <div class="gate-cover-sub">AUTONOMOUS CYBERSECURITY</div>
              </div>
            </div>

            <!-- Central Golden Seal / Latch -->
            <div class="gate-center-seal" id="gate-center-seal" onclick="openRoyalBooklet(false)" title="Click or Scroll to Open Booklet!">
              <img src="__MASCOT__" alt="LeukQuant Seal">
              <span>👑 OPEN</span>
            </div>

            <!-- ================= PAGE 1: LEFT PAGE (DIGNITARIES) ================= -->
            <div class="book-page book-page-left" id="book-page-left">
              <!-- Botanical Corner Foliage Vines in Dark Navy -->
              <svg class="corner-vignette corner-tl" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 108 C12 45 45 12 108 12 M28 108 C28 58 58 28 108 28 M12 72 C36 48 72 36 108 12" stroke="#2A3B5C" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="28" cy="28" r="4.5" fill="#2A3B5C"/>
                <circle cx="68" cy="18" r="3.5" fill="#2A3B5C"/>
                <circle cx="18" cy="68" r="3.5" fill="#2A3B5C"/>
                <path d="M40 16 C52 28 52 46 40 58 C28 46 28 28 40 16 Z" fill="#2A3B5C" opacity="0.85"/>
                <path d="M16 40 C28 52 46 52 58 40 C46 28 28 28 16 40 Z" fill="#2A3B5C" opacity="0.85"/>
              </svg>
              <svg class="corner-vignette corner-bl" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 108 C12 45 45 12 108 12 M28 108 C28 58 58 28 108 28 M12 72 C36 48 72 36 108 12" stroke="#2A3B5C" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="28" cy="28" r="4.5" fill="#2A3B5C"/>
                <circle cx="68" cy="18" r="3.5" fill="#2A3B5C"/>
                <circle cx="18" cy="68" r="3.5" fill="#2A3B5C"/>
                <path d="M40 16 C52 28 52 46 40 58 C28 46 28 28 40 16 Z" fill="#2A3B5C" opacity="0.85"/>
                <path d="M16 40 C28 52 46 52 58 40 C46 28 28 28 16 40 Z" fill="#2A3B5C" opacity="0.85"/>
              </svg>

              <!-- Top Header & Crest -->
              <div>
                <div class="royal-header-tag">I N V I T A T I O N</div>
                <svg class="royal-gold-crest" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M32 4 L42 22 L62 25 L47 39 L51 59 L32 49 L13 59 L17 39 L2 25 L22 22 Z" stroke="#C5A059" stroke-width="2" fill="rgba(197, 160, 89, 0.15)"/>
                  <circle cx="32" cy="32" r="8" stroke="#C5A059" stroke-width="1.5"/>
                </svg>
                <div class="royal-lead-title">WE ARE HONOURED TO CORDIALLY INVITE YOU</div>
                <div class="royal-gold-flourish">«««««——————»»»»»</div>
                <div class="royal-sub-line">AN INCUBATED STARTUP AT JIT FOUNDATION</div>
                <div class="royal-sub-line">FOR THE GRAND LAUNCH</div>
              </div>

              <!-- Dignitaries Grid -->
              <div class="royal-dignitaries-grid">
                <!-- Dignitary 1: Dr. N. Marie Wilson (Chief Guest) -->
                <div class="royal-dignitary-card">
                  <div class="royal-guest-img-frame">
                    <img src="__GUEST_PHOTO__" alt="Dr. N. Marie Wilson" class="royal-guest-img">
                  </div>
                  <div class="royal-guest-content">
                    <span class="royal-guest-kicker">CHIEF GUEST</span>
                    <h3 class="royal-guest-title-name">DR N.MARIE WILSON</h3>
                    <div class="royal-guest-detail-text">MINISTER FOR FINANCE, PENSIONS,</div>
                    <div class="royal-guest-detail-text">PLANNING &amp; DEVELOPMENT</div>
                    <div class="royal-guest-detail-text">MEMBER OF LEGISLATIVE ASSEMBLY</div>
                    <div class="royal-gold-flourish" style="margin: 2px auto;">«««««——————»»»»»</div>
                    <div class="royal-guest-detail-text" style="font-weight: 700;">CHAIRMAN &amp; DIRECTOR</div>
                    <div class="royal-guest-detail-text" style="font-weight: 800; color: #0F172A;">JEPPIAAR INSTITUTE OF TECHNOLOGY</div>
                  </div>
                </div>

                <!-- Dignitary 2: Soundarraj Kannan (Special Guest of Honour) -->
                <div class="royal-dignitary-card">
                  <div class="royal-guest-img-frame">
                    <img src="__GUEST_SOUNDARRAJ__" alt="Soundarraj Kannan" class="royal-guest-img">
                  </div>
                  <div class="royal-guest-content">
                    <span class="royal-guest-kicker">SPECIAL GUEST OF HONOUR</span>
                    <h3 class="royal-guest-title-name">SOUNDARRAJ KANNAN</h3>
                    <div class="royal-guest-detail-text">DIRECTOR &bull; KRP TECH SOLUTIONS</div>
                    <div class="royal-guest-detail-text">STRATEGIC ADVISOR &amp; INDUSTRY VETERAN</div>
                    <div class="royal-guest-detail-text">CYBER PLATFORMS INNOVATOR</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- ================= CENTER BOOK SPINE ================= -->
            <div class="book-spine-crease">
              <div class="book-ribbon-tassel"></div>
            </div>

            <!-- ================= PAGE 2: RIGHT PAGE (LAUNCH & CREDENTIALS) ================= -->
            <div class="book-page book-page-right" id="book-page-right">
              <!-- Botanical Corner Foliage Vines in Dark Navy -->
              <svg class="corner-vignette corner-tr" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 108 C12 45 45 12 108 12 M28 108 C28 58 58 28 108 28 M12 72 C36 48 72 36 108 12" stroke="#2A3B5C" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="28" cy="28" r="4.5" fill="#2A3B5C"/>
                <circle cx="68" cy="18" r="3.5" fill="#2A3B5C"/>
                <circle cx="18" cy="68" r="3.5" fill="#2A3B5C"/>
                <path d="M40 16 C52 28 52 46 40 58 C28 46 28 28 40 16 Z" fill="#2A3B5C" opacity="0.85"/>
                <path d="M16 40 C28 52 46 52 58 40 C46 28 28 28 16 40 Z" fill="#2A3B5C" opacity="0.85"/>
              </svg>
              <svg class="corner-vignette corner-br" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 108 C12 45 45 12 108 12 M28 108 C28 58 58 28 108 28 M12 72 C36 48 72 36 108 12" stroke="#2A3B5C" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="28" cy="28" r="4.5" fill="#2A3B5C"/>
                <circle cx="68" cy="18" r="3.5" fill="#2A3B5C"/>
                <circle cx="18" cy="68" r="3.5" fill="#2A3B5C"/>
                <path d="M40 16 C52 28 52 46 40 58 C28 46 28 28 40 16 Z" fill="#2A3B5C" opacity="0.85"/>
                <path d="M16 40 C28 52 46 52 58 40 C46 28 28 28 16 40 Z" fill="#2A3B5C" opacity="0.85"/>
              </svg>

              <!-- LeukQuant Section -->
              <div>
                <div class="royal-sub-line" style="margin-top: 4px;">FOR THE GRAND LAUNCH OF</div>
                <div class="royal-logo-center-wrap">
                  <img src="__LEUKQUANT_LOGO__" alt="LeukQuant" class="royal-leukquant-logo">
                </div>
                <div class="royal-gold-flourish">»»»——————«««</div>
                <div class="royal-sub-line">AI-POWERED ACTIVE DECEPTION &amp; AUTONOMOUS CYBERSECURITY</div>

                <!-- Date Display -->
                <div class="royal-date-big">SEP 07, 2026</div>

                <!-- Meta Pills -->
                <div class="royal-meta-list">
                  <div class="royal-meta-item">
                    <span class="royal-meta-badge-num">1</span>
                    <span><strong>VENUE:</strong> Ground Floor Auditorium, JIT Kunnam Campus</span>
                  </div>
                  <div class="royal-meta-item">
                    <span class="royal-meta-badge-num">2</span>
                    <span><strong>TIME:</strong> 09:30 AM IST &bull; Live Demonstrations &amp; Keynote</span>
                  </div>
                </div>
              </div>

              <!-- Institutional Footer -->
              <div>
                <div class="royal-inst-footer">
                  <img src="__JIT_CREST__" alt="JIT Crest" class="royal-inst-left-crest">
                  <div class="royal-inst-mid-info">
                    <h4>JEPPIAAR INSTITUTE OF TECHNOLOGY</h4>
                    <p>Self-Financing Technical Institution &bull; Kunnam, Sunguvarchatram</p>
                    <p>Sriperumbudur, Tamil Nadu 631604</p>
                  </div>
                  <div class="royal-inst-right-seals">
                    <img src="__NAAC_SEAL__" alt="NAAC A Grade">
                    <img src="__NBA_LOGO__" alt="NBA Accredited">
                  </div>
                </div>

                <!-- Action Buttons -->
                <div class="royal-actions-container">
                  <button class="btn-material-primary" onclick="openOfficialCardModal()" style="background: linear-gradient(135deg, #B45309 0%, #D4AF37 100%); color: #0F172A; font-weight: 800;">
                    <span>📜 Official Card (HD)</span>
                  </button>
                  <button class="btn-material-primary" onclick="window.location.href='#venue'">
                    <span>📍 Navigate to Venue</span>
                  </button>
                  <button class="btn-material-secondary" onclick="addToCalendar()">
                    <span>📅 Add to Calendar</span>
                  </button>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Authentic Official Invitation Card Inline Container -->
        <div class="official-card-inline-wrap" id="official-card-inline">
          <div class="official-card-header">
            <span class="official-card-tag">📜 OFFICIAL PRINTED INVITATION CARD</span>
            <button class="btn-envelope-action" onclick="openOfficialCardModal()" style="font-size: 10.5px; padding: 4px 12px;">🔍 Fullscreen HD Zoom</button>
          </div>
          <div class="official-card-frame">
            <img src="__OFFICIAL_INVITE_FULL__" alt="LeukQuant Official Grand Launch Invitation Card" class="official-card-img" onclick="openOfficialCardModal()" title="Click to View Fullscreen Official Card">
          </div>
        </div>

      </div>
    </div>

    <!-- Official Fullscreen Modal -->
    <div id="official-card-modal" class="official-modal-backdrop" onclick="closeOfficialCardModal()">
      <div class="official-modal-content" onclick="event.stopPropagation()">
        <button class="official-modal-close" onclick="closeOfficialCardModal()" title="Close">&times;</button>
        <div class="official-modal-header">
          <span class="official-modal-title">👑 LeukQuant Official Grand Launch 2026 Invitation Card</span>
          <a href="__OFFICIAL_INVITE_FULL__" download="LeukQuant_Official_Invitation_2026.png" class="btn-envelope-action" style="background: #D4AF37; color: #0F172A;">📥 Download HD Card</a>
        </div>
        <div class="official-modal-img-wrap">
          <img src="__OFFICIAL_INVITE_FULL__" alt="Official Invitation Card HD" class="official-modal-img">
        </div>
      </div>
    </div>
  </section>"""

html = re.sub(folio_pattern, new_folio_html, html, flags=re.DOTALL)

# Add CSS for the official card inline & modal
extra_css = """
  /* Authentic Official Invitation Card Display & Modal */
  .official-card-inline-wrap {
    width: 100%;
    max-width: 980px;
    margin: 28px auto 0 auto;
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(16px);
    border: 2px solid rgba(212, 175, 55, 0.4);
    border-radius: 20px;
    padding: 16px 20px 20px 20px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 25;
  }

  .official-card-header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    flex-wrap: wrap;
    gap: 8px;
  }

  .official-card-tag {
    font-family: var(--font-royal);
    font-size: 11.5px;
    font-weight: 800;
    color: #FEF3C7;
    letter-spacing: 0.12em;
  }

  .official-card-frame {
    width: 100%;
    border-radius: 14px;
    overflow: hidden;
    border: 2px solid #C5A059;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(212, 175, 55, 0.2);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .official-card-frame:hover {
    transform: scale(1.01);
    box-shadow: 0 20px 55px rgba(212, 175, 55, 0.35);
  }

  .official-card-img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: contain;
  }

  /* Fullscreen Modal */
  .official-modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(5, 8, 16, 0.88);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    z-index: 9999999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .official-modal-backdrop.active {
    opacity: 1;
    pointer-events: auto;
  }

  .official-modal-content {
    background: #0F172A;
    border: 2px solid #D4AF37;
    border-radius: 20px;
    padding: 16px 20px;
    max-width: 95vw;
    max-height: 92vh;
    display: flex;
    flex-direction: column;
    position: relative;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9), 0 0 40px rgba(212, 175, 55, 0.4);
    transform: scale(0.92);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .official-modal-backdrop.active .official-modal-content {
    transform: scale(1);
  }

  .official-modal-close {
    position: absolute;
    top: 10px;
    right: 14px;
    background: transparent;
    border: none;
    color: #FEF3C7;
    font-size: 28px;
    cursor: pointer;
    line-height: 1;
    z-index: 10;
  }

  .official-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    padding-right: 32px;
    flex-wrap: wrap;
    gap: 8px;
  }

  .official-modal-title {
    font-family: var(--font-royal);
    font-size: 13.5px;
    font-weight: 800;
    color: #FEF3C7;
    letter-spacing: 0.08em;
  }

  .official-modal-img-wrap {
    overflow: auto;
    max-height: 80vh;
    border-radius: 12px;
    border: 1px solid rgba(212, 175, 55, 0.3);
  }

  .official-modal-img {
    width: 100%;
    max-width: 1100px;
    height: auto;
    display: block;
  }

  @media (max-width: 850px) {
    .official-card-inline-wrap {
      padding: 10px;
      margin-top: 14px;
      border-radius: 14px;
    }
    .official-card-tag {
      font-size: 9px;
    }
  }
"""

# Insert extra CSS before </style>
html = html.replace('</style>', extra_css + '\n</style>')

# Add JS functions for modal
modal_js = """
    function openOfficialCardModal() {
      const modal = document.getElementById('official-card-modal');
      if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeOfficialCardModal() {
      const modal = document.getElementById('official-card-modal');
      if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
      }
    }
"""

html = html.replace('function initGsapAnimations() {', modal_js + '\n    function initGsapAnimations() {')

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html with official invite on booklet and HD modal!")
