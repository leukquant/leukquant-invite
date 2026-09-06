# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace mobile styling with clean, pixel-perfect aligned box & text typography
mobile_css_pattern = r'/\*\s*=========================================================\s*MOBILE RESPONSIVE: COMPACT SMALL 2-PAGE SPREAD BOOKLET.*?(?=\/\*\s*=========================================================\s*4\.|\.showcase-pinned-section)'

new_mobile_css = """/* =========================================================
     MOBILE RESPONSIVE: PERFECTLY ALIGNED 2-PAGE BI-FOLD SPREAD BOOKLET
     ========================================================= */
  @media (max-width: 850px) {
    .envelope-pinned-section {
      padding: 20px 8px 36px 8px !important;
    }

    /* IN MOBILE: REMOVE ENVELOPE BED COMPLETELY */
    .royal-envelope-bed {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
      min-height: auto !important;
      max-width: 100% !important;
      perspective: 1400px !important;
    }

    .envelope-bed-lining,
    .envelope-top-crest-bar,
    .envelope-flap-top,
    .envelope-pocket-flaps,
    .royal-wax-seal {
      display: none !important;
    }

    .envelope-header-hint {
      margin-bottom: 12px !important;
    }

    .envelope-hint-title {
      font-size: 22px !important;
      margin: 4px 0 2px 0 !important;
    }

    .envelope-hint-subtitle {
      font-size: 11.5px !important;
    }

    /* COMPACT MINIATURE BOOKLET (PERFECT 50/50 2-PAGE SPREAD) */
    .book-stage-perspective {
      width: 100% !important;
      max-width: 580px !important;
      margin: 0 auto !important;
    }

    .royal-book-folio {
      display: grid !important;
      grid-template-columns: 1fr 12px 1fr !important;
      align-items: stretch !important;
      border: 2px solid #C5A059 !important;
      border-radius: 16px !important;
      box-shadow: inset 0 0 0 2.5px #FAF7F2, inset 0 0 0 4.5px #C5A059, 0 15px 40px rgba(0,0,0,0.25) !important;
      width: 100% !important;
      max-width: 580px !important;
      margin: 0 auto !important;
      background: #FAF7F2 !important;
      min-height: 380px !important;
    }

    .book-page {
      padding: 12px 8px 10px 8px !important;
      min-width: 0 !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      text-align: center !important;
      box-sizing: border-box !important;
    }

    .book-page-left {
      border-right: 1px solid rgba(197, 160, 89, 0.4) !important;
      border-bottom: none !important;
    }

    .book-page-right {
      border-left: 1px solid rgba(197, 160, 89, 0.4) !important;
      border-top: none !important;
      padding-top: 12px !important;
    }

    .book-spine-crease {
      width: 12px !important;
      height: 100% !important;
    }

    .book-ribbon-tassel {
      width: 2.5px !important;
      height: 88% !important;
    }

    .corner-vignette {
      width: 24px !important;
      height: 24px !important;
    }

    /* LEFT PAGE ALIGNMENT & TYPOGRAPHY */
    .royal-header-tag {
      font-size: 10px !important;
      letter-spacing: 0.22em !important;
      margin-bottom: 2px !important;
      font-weight: 800 !important;
    }

    .royal-gold-crest {
      width: 20px !important;
      margin: 1px auto 2px auto !important;
    }

    .royal-lead-title {
      font-size: 8px !important;
      line-height: 1.18 !important;
      letter-spacing: 0.03em !important;
      margin-bottom: 1px !important;
      font-weight: 800 !important;
    }

    .royal-gold-flourish {
      font-size: 8px !important;
      margin: 1px auto !important;
    }
    .royal-gold-flourish::before,
    .royal-gold-flourish::after {
      width: 16px !important;
      height: 1px !important;
    }

    .royal-sub-line {
      font-size: 7.5px !important;
      line-height: 1.2 !important;
      margin: 1px 0 !important;
      font-weight: 700 !important;
    }

    /* DIGNITARIES GRID & ALIGNED BOXES */
    .royal-dignitaries-grid {
      display: grid !important;
      grid-template-columns: 1fr 1fr !important;
      gap: 6px !important;
      margin: 6px 0 4px 0 !important;
      align-items: stretch !important;
    }

    .royal-dignitary-card {
      padding: 6px 4px !important;
      border-radius: 10px !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: flex-start !important;
      text-align: center !important;
      background: linear-gradient(180deg, #FFFFFF 0%, #F8F5EE 100%) !important;
      border: 1px solid rgba(197, 160, 89, 0.6) !important;
      box-shadow: 0 4px 10px rgba(15, 30, 75, 0.05) !important;
      min-height: 150px !important;
    }

    .royal-guest-img-frame {
      width: 48px !important;
      height: 54px !important;
      border-radius: 8px !important;
      margin-bottom: 4px !important;
      border: 1.5px solid #C5A059 !important;
      flex-shrink: 0 !important;
    }

    .royal-guest-kicker {
      font-size: 6.5px !important;
      padding: 1.5px 4px !important;
      margin-bottom: 2px !important;
      font-weight: 800 !important;
    }

    .royal-guest-title-name {
      font-size: 9.5px !important;
      line-height: 1.15 !important;
      margin-bottom: 2px !important;
      font-weight: 800 !important;
    }

    .royal-guest-detail-text {
      font-size: 6.8px !important;
      line-height: 1.22 !important;
      margin: 0.5px 0 !important;
      color: #334155 !important;
    }

    /* RIGHT PAGE ALIGNMENT & TYPOGRAPHY */
    .royal-leukquant-logo {
      height: 30px !important;
      margin: 2px 0 !important;
    }

    .royal-date-big {
      font-size: 18px !important;
      margin: 2px 0 !important;
      font-weight: 900 !important;
    }

    .royal-meta-list {
      gap: 3px !important;
      margin: 3px 0 6px 0 !important;
    }

    .royal-meta-item {
      font-size: 7.8px !important;
      padding: 2px 8px !important;
      gap: 4px !important;
      font-weight: 700 !important;
      border-radius: 14px !important;
    }

    .royal-meta-badge-num {
      width: 12px !important;
      height: 12px !important;
      font-size: 7px !important;
    }

    .royal-inst-footer {
      display: flex !important;
      flex-direction: row !important;
      gap: 4px !important;
      padding-top: 6px !important;
      margin-top: 6px !important;
      align-items: center !important;
      justify-content: space-between !important;
      border-top: 1px solid #E2D9C2 !important;
    }

    .royal-inst-left-crest {
      height: 24px !important;
    }

    .royal-inst-mid-info {
      min-width: 70px !important;
      flex: 1 !important;
    }
    .royal-inst-mid-info h4 {
      font-size: 7.5px !important;
      margin-bottom: 1px !important;
      font-weight: 800 !important;
    }
    .royal-inst-mid-info p {
      font-size: 6.2px !important;
      line-height: 1.15 !important;
    }

    .royal-inst-right-seals img {
      height: 16px !important;
    }

    .royal-actions-container {
      display: flex !important;
      flex-direction: row !important;
      margin-top: 6px !important;
      gap: 5px !important;
      justify-content: center !important;
    }

    .btn-material-primary {
      padding: 5px 12px !important;
      font-size: 9px !important;
      width: auto !important;
      border-radius: 16px !important;
    }

    .btn-material-secondary {
      padding: 5px 10px !important;
      font-size: 9px !important;
      width: auto !important;
      border-radius: 16px !important;
    }

    /* Mobile Gatefold Covers */
    .book-gate-cover {
      padding: 10px 6px !important;
    }
    .gate-cover-crest {
      height: 28px !important;
    }
    .gate-cover-title {
      font-size: 10.5px !important;
      letter-spacing: 0.1em !important;
    }
    .gate-cover-sub {
      font-size: 7.5px !important;
    }
    .gate-center-seal {
      width: 52px !important;
      height: 52px !important;
    }
    .gate-center-seal img {
      height: 24px !important;
      width: 24px !important;
    }
    .gate-center-seal span {
      font-size: 6.5px !important;
    }
  }

"""

html = re.sub(mobile_css_pattern, new_mobile_css, html, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html with pixel-perfect box & text alignment on mobile!")
