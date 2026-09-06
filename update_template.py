# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 2 CSS
css_section_2 = """  /* =========================================================
     3. SECTION 2: 3D LUXURY ENVELOPE & ROYAL CARD (PINNED & UNSEALING)
     ========================================================= */
  .envelope-pinned-section {
    min-height: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 16px 80px 16px;
    overflow: visible;
  }

  .envelope-gold-spotlight {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 980px;
    height: 780px;
    border-radius: 50%;
    background: radial-gradient(ellipse at center, rgba(212, 175, 55, 0.22) 0%, rgba(212, 175, 55, 0.04) 50%, transparent 75%);
    filter: blur(65px);
    pointer-events: none;
    z-index: 0;
    opacity: 0.85;
  }

  .envelope-stage-wrapper {
    position: relative;
    width: 100%;
    max-width: 1260px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 2;
  }

  .envelope-header-hint {
    text-align: center;
    margin-bottom: 24px;
  }

  .envelope-hint-controls {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 8px;
  }

  .envelope-hint-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FFFBEB;
    border: 1.5px solid #FDE68A;
    color: #B45309;
    padding: 6px 18px;
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: 11.5px;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    box-shadow: 0 6px 14px rgba(180, 83, 9, 0.1);
  }

  .btn-envelope-action {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    border: 1.5px solid #D4AF37;
    color: #FEF3C7;
    padding: 6px 16px;
    border-radius: var(--radius-full);
    font-family: var(--font-royal);
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .btn-envelope-action:hover {
    background: linear-gradient(135deg, #2D3D58 0%, #172133 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(212, 175, 55, 0.35);
    border-color: #FEF3C7;
  }

  .envelope-hint-title {
    font-family: var(--font-royal);
    font-size: clamp(24px, 4vw, 36px);
    font-weight: 900;
    color: var(--text-heading);
    letter-spacing: 0.04em;
    margin: 8px 0 4px 0;
  }

  .envelope-hint-subtitle {
    font-size: 14px;
    color: var(--text-muted);
    font-weight: 600;
  }

  /* 3D Physical Envelope Bed / Frame */
  .royal-envelope-bed {
    position: relative;
    width: 100%;
    max-width: 1240px;
    min-height: 620px;
    background: linear-gradient(145deg, #111A2E 0%, #080D18 100%);
    border: 3.5px solid #D4AF37;
    border-radius: 28px;
    box-shadow: 0 45px 120px rgba(8, 13, 24, 0.8), inset 0 0 50px rgba(0, 0, 0, 0.85), 0 0 35px rgba(212, 175, 55, 0.22);
    padding: 34px 28px 30px 28px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 auto;
    perspective: 1800px;
    transform-style: preserve-3d;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
  }

  .envelope-bed-lining {
    position: absolute;
    inset: 10px;
    border: 1.5px dashed rgba(212, 175, 55, 0.45);
    border-radius: 20px;
    pointer-events: none;
    z-index: 1;
  }

  /* Envelope Top Crest Ribbon Bar */
  .envelope-top-crest-bar {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: linear-gradient(135deg, #243147 0%, #131D2D 100%);
    border: 1.5px solid #D4AF37;
    padding: 8px 24px;
    border-radius: var(--radius-full);
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), inset 0 1px 2px rgba(255, 255, 255, 0.15);
    z-index: 15;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .envelope-top-crest-bar:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(212, 175, 55, 0.35);
  }
  .envelope-top-crest-bar img {
    height: 28px;
    width: auto;
    filter: drop-shadow(0 2px 6px rgba(0, 102, 255, 0.6));
  }
  .envelope-top-crest-bar span {
    font-family: var(--font-royal);
    font-size: 12.5px;
    font-weight: 800;
    color: #FEF3C7;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }

  /* 3D Hinged Envelope Top Flap */
  .envelope-flap-top {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 240px;
    transform-origin: top center;
    transform-style: preserve-3d;
    z-index: 35;
    filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.6));
    transition: transform 1.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.6s ease;
    pointer-events: none;
  }
  .envelope-flap-top.opened {
    transform: rotateX(180deg);
    z-index: 2;
    opacity: 0;
    pointer-events: none;
  }

  .flap-triangle-shape {
    position: absolute;
    inset: 0;
    clip-path: polygon(0 0, 100% 0, 50% 100%);
    background: linear-gradient(180deg, #223046 0%, #111B2C 100%);
    border-top: 3.5px solid #D4AF37;
  }

  /* Royal Wax Seal on Flap Point */
  .royal-wax-seal {
    position: absolute;
    bottom: -36px;
    left: 50%;
    transform: translateX(-50%);
    width: 82px;
    height: 82px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, #F59E0B 0%, #D4AF37 40%, #8D6105 85%, #593D02 100%);
    border: 3.5px solid #FEF3C7;
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.6), inset 0 2px 6px rgba(255, 255, 255, 0.8), inset 0 -3px 8px rgba(0, 0, 0, 0.5), 0 0 25px rgba(212, 175, 55, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 50;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, opacity 0.5s ease;
    overflow: hidden;
    pointer-events: auto;
    animation: sealGlowPulse 2.4s infinite alternate;
  }
  @keyframes sealGlowPulse {
    0% { box-shadow: 0 14px 30px rgba(0,0,0,0.6), 0 0 15px rgba(212,175,55,0.4); transform: translateX(-50%) scale(1); }
    100% { box-shadow: 0 18px 40px rgba(0,0,0,0.8), 0 0 35px rgba(212,175,55,0.8); transform: translateX(-50%) scale(1.06); }
  }
  .royal-wax-seal:hover {
    transform: translateX(-50%) scale(1.15) !important;
    box-shadow: 0 20px 45px rgba(212, 175, 55, 0.8), inset 0 2px 6px rgba(255, 255, 255, 0.95);
  }
  .royal-wax-seal.broken {
    animation: none;
    transform: translateX(-50%) scale(1.35) rotate(20deg) !important;
    opacity: 0;
    pointer-events: none;
  }

  .seal-mascot-img {
    height: 40px;
    width: 40px;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4)) brightness(1.15);
  }
  .seal-label {
    font-family: var(--font-royal);
    font-size: 8.5px;
    font-weight: 900;
    letter-spacing: 0.14em;
    color: #FEF3C7;
    margin-top: -3px;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
  }

  /* Envelope Front Pocket Triangular Flaps */
  .envelope-pocket-flaps {
    position: absolute;
    inset: 0;
    z-index: 25;
    pointer-events: none;
    border-radius: 28px;
    overflow: hidden;
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  .envelope-pocket-flaps.hidden {
    opacity: 0;
    transform: translateY(40px);
    pointer-events: none;
  }
  .pocket-flap-left {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    clip-path: polygon(0 0, 0 100%, 50% 55%);
    background: linear-gradient(135deg, #1C273A 0%, #0F1726 100%);
    border-left: 3px solid #D4AF37;
  }
  .pocket-flap-right {
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    clip-path: polygon(100% 0, 100% 100%, 50% 55%);
    background: linear-gradient(-135deg, #1C273A 0%, #0F1726 100%);
    border-right: 3px solid #D4AF37;
  }
  .pocket-flap-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    clip-path: polygon(0 100%, 100% 100%, 50% 48%);
    background: linear-gradient(0deg, #0A101D 0%, #172233 100%);
    border-bottom: 3px solid #D4AF37;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 20px;
  }
  .pocket-embossed-title {
    font-family: var(--font-royal);
    font-size: 13px;
    font-weight: 800;
    color: #D4AF37;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
    letter-spacing: 0.18em;
  }

  /* =========================================================
     ROYAL BOOK FOLIO (2-PAGE BI-FOLD SPREAD)
     ========================================================= */
  .royal-book-folio {
    display: grid;
    grid-template-columns: 1fr 22px 1fr;
    background: #FAF7F2;
    border: 3.5px solid #C5A059;
    border-radius: 22px;
    box-shadow: inset 0 0 0 5px #FAF7F2, inset 0 0 0 8px #C5A059, 0 35px 90px rgba(0, 0, 0, 0.6);
    position: relative;
    width: 100%;
    overflow: hidden;
    z-index: 20;
    will-change: transform, opacity;
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
  }

  .card-sheen-overlay {
    position: absolute;
    top: 0;
    left: -150%;
    width: 80%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.8), rgba(212, 175, 55, 0.4), transparent);
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 100;
  }

  /* Book Left & Right Pages */
  .book-page {
    padding: 34px 28px 26px 28px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    min-width: 0;
    box-sizing: border-box;
    word-break: normal;
    overflow-wrap: break-word;
  }

  .book-page-left {
    background: linear-gradient(90deg, #FCFBF8 0%, #F5EFE4 100%);
    border-right: 1px solid rgba(197, 160, 89, 0.35);
    box-shadow: inset -15px 0 25px -10px rgba(0, 0, 0, 0.08);
  }

  .book-page-right {
    background: linear-gradient(270deg, #FCFBF8 0%, #F5EFE4 100%);
    border-left: 1px solid rgba(197, 160, 89, 0.35);
    box-shadow: inset 15px 0 25px -10px rgba(0, 0, 0, 0.08);
  }

  /* 3D Center Book Spine Crease */
  .book-spine-crease {
    width: 22px;
    height: 100%;
    background: linear-gradient(90deg, rgba(0, 0, 0, 0.18) 0%, rgba(197, 160, 89, 0.8) 50%, rgba(0, 0, 0, 0.18) 100%);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 0 12px rgba(0, 0, 0, 0.35);
  }

  .book-ribbon-tassel {
    width: 4px;
    height: 90%;
    background: linear-gradient(180deg, #D4AF37 0%, #F59E0B 50%, #B45309 85%, transparent 100%);
    border-radius: 2px;
    box-shadow: 0 0 12px rgba(212, 175, 55, 0.85);
    animation: ribbonWave 4s ease-in-out infinite;
  }

  @keyframes ribbonWave {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(4px) rotate(1deg); }
  }

  /* Botanical Corner Vignettes in Dark Navy */
  .corner-vignette {
    position: absolute;
    width: 65px;
    height: 65px;
    pointer-events: none;
    z-index: 5;
    opacity: 0.85;
  }
  .corner-tl { top: 10px; left: 10px; }
  .corner-tr { top: 10px; right: 10px; transform: scaleX(-1); }
  .corner-bl { bottom: 10px; left: 10px; transform: scaleY(-1); }
  .corner-br { bottom: 10px; right: 10px; transform: scale(-1); }

  /* Header Section (Left Page) */
  .royal-header-tag {
    font-family: var(--font-royal);
    font-size: 15px;
    letter-spacing: 0.36em;
    color: #334155;
    font-weight: 800;
    margin-top: 2px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }

  .royal-gold-crest {
    width: 40px;
    height: auto;
    margin: 0 auto 8px auto;
    display: block;
    filter: drop-shadow(0 2px 8px rgba(212, 175, 55, 0.4));
    animation: crestGlow 3s ease-in-out infinite alternate;
  }

  @keyframes crestGlow {
    0% { transform: scale(1); filter: drop-shadow(0 2px 6px rgba(212, 175, 55, 0.3)); }
    100% { transform: scale(1.06); filter: drop-shadow(0 4px 14px rgba(212, 175, 55, 0.7)); }
  }

  .royal-lead-title {
    font-family: var(--font-royal);
    font-size: 13px;
    font-weight: 800;
    color: #1E293B;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
  }

  .royal-gold-flourish {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    color: #C5A059;
    font-size: 13px;
    margin: 3px auto;
  }
  .royal-gold-flourish::before,
  .royal-gold-flourish::after {
    content: "";
    display: inline-block;
    width: 45px;
    height: 1.5px;
    background: #C5A059;
  }

  .royal-sub-line {
    font-family: var(--font-royal);
    font-size: 12px;
    font-weight: 700;
    color: #1E293B;
    letter-spacing: 0.06em;
    margin: 2px 0;
  }

  /* Dignitaries Grid (Left Page) */
  .royal-dignitaries-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 12px 0 8px 0;
    position: relative;
    text-align: center;
  }

  .royal-dignitary-card {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 245, 238, 0.98) 100%);
    border: 1.5px solid rgba(197, 160, 89, 0.55);
    border-radius: 16px;
    padding: 12px 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 6px 18px rgba(15, 30, 75, 0.06);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
  }
  .royal-dignitary-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(197, 160, 89, 0.28);
    border-color: #C5A059;
  }

  .royal-guest-img-frame {
    width: 96px;
    height: 110px;
    border: 2px solid #C5A059;
    border-radius: 12px;
    overflow: hidden;
    flex-shrink: 0;
    background: #E8D7B8;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12);
    margin-bottom: 7px;
    transition: transform 0.3s ease;
  }
  .royal-dignitary-card:hover .royal-guest-img-frame {
    transform: scale(1.03);
  }
  .royal-guest-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .royal-guest-content {
    width: 100%;
    text-align: center;
  }

  .royal-guest-kicker {
    font-family: var(--font-royal);
    font-size: 10px;
    font-weight: 800;
    color: #B45309;
    background: #FEF3C7;
    padding: 2px 8px;
    border-radius: 4px;
    letter-spacing: 0.12em;
    margin-bottom: 4px;
    display: inline-block;
    text-transform: uppercase;
  }

  .royal-guest-title-name {
    font-family: var(--font-royal);
    font-size: 15.5px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: 0.02em;
    margin-bottom: 3px;
    line-height: 1.15;
  }

  .royal-guest-detail-text {
    font-family: var(--font-royal);
    font-size: 9px;
    font-weight: 600;
    color: #334155;
    letter-spacing: 0.03em;
    line-height: 1.35;
    margin: 1.5px 0;
  }

  /* Logo & Date Section (Right Page) */
  .royal-logo-center-wrap {
    margin: 6px 0 2px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .royal-leukquant-logo {
    height: 60px;
    width: auto;
    object-fit: contain;
    margin: 2px 0;
    filter: drop-shadow(0 4px 14px rgba(0, 102, 255, 0.32));
    transition: transform 0.3s ease;
  }
  .royal-leukquant-logo:hover {
    transform: scale(1.05);
  }

  .royal-date-big {
    font-family: var(--font-royal);
    font-size: 32px;
    font-weight: 900;
    color: #334155;
    letter-spacing: 0.05em;
    margin: 4px 0 3px 0;
    background: linear-gradient(135deg, #0F172A 0%, #334155 50%, #0F172A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .royal-meta-list {
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: center;
    margin: 6px 0 12px 0;
  }

  .royal-meta-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-royal);
    font-size: 11.5px;
    font-weight: 700;
    color: #1E293B;
    letter-spacing: 0.05em;
    background: rgba(255, 255, 255, 0.85);
    padding: 4px 14px;
    border-radius: var(--radius-full);
    border: 1px solid rgba(197, 160, 89, 0.4);
  }

  .royal-meta-badge-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 17px;
    height: 17px;
    background: #C5A059;
    color: #FFFFFF;
    border-radius: 50%;
    font-size: 9.5px;
    font-weight: 800;
  }

  /* Institutional Footer (Right Page) */
  .royal-inst-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding-top: 12px;
    border-top: 1.5px solid #E2D9C2;
    margin-top: 10px;
    flex-wrap: wrap;
    text-align: center;
  }

  .royal-inst-left-crest {
    height: 48px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.08));
  }

  .royal-inst-mid-info {
    flex: 1;
    min-width: 180px;
  }
  .royal-inst-mid-info h4 {
    font-family: var(--font-royal);
    font-size: 12px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: 0.04em;
    margin-bottom: 2px;
  }
  .royal-inst-mid-info p {
    font-size: 9px;
    color: #475569;
    line-height: 1.35;
    margin: 1px 0;
  }

  .royal-inst-right-seals {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .royal-inst-right-seals img {
    height: 32px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.08));
  }

  .royal-actions-container {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 14px;
  }

  .btn-material-primary {
    background: var(--primary);
    color: #FFFFFF;
    border: none;
    border-radius: var(--radius-full);
    padding: 11px 24px;
    font-family: var(--font-body);
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(0, 102, 255, 0.3);
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
  }

  .btn-material-primary:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 12px 26px rgba(0, 102, 255, 0.38);
  }

  .btn-material-outline {
    background: #FFFFFF;
    color: var(--text-heading);
    border: 1.5px solid #E2E8F0;
    border-radius: var(--radius-full);
    padding: 11px 20px;
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
  }

  .btn-material-outline:hover {
    border-color: var(--primary);
    color: var(--primary);
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(15, 30, 75, 0.06);
  }"""

css_pattern = r'(\/\* =+\s*3\.\s*SECTION 2:.*?)(?=\/\* =+\s*4\.\s*SECTION 3:)'
content = re.sub(css_pattern, css_section_2 + '\n\n  ', content, flags=re.DOTALL)


# 2. Update Responsive Media Queries for Mobile
mobile_css = """  /* Tablets & Mobile Devices (<= 850px) - Direct Double-Sided Open Folio */
  @media (max-width: 850px) {
    .envelope-flap-top,
    .royal-wax-seal,
    .envelope-pocket-flaps,
    .envelope-bed-lining,
    .envelope-hint-controls {
      display: none !important;
    }
    .envelope-pinned-section {
      padding: 30px 10px 50px 10px !important;
    }
    .royal-envelope-bed {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      min-height: auto !important;
    }
    .envelope-top-crest-bar {
      margin-bottom: 12px !important;
      font-size: 10.5px !important;
      padding: 6px 14px !important;
      width: 95% !important;
      justify-content: center !important;
      background: linear-gradient(135deg, #1E293B, #0F172A) !important;
    }
    .envelope-top-crest-bar span {
      font-size: 10.5px !important;
      letter-spacing: 0.08em !important;
    }
    .royal-book-folio {
      grid-template-columns: 1fr !important;
      opacity: 1 !important;
      transform: none !important;
      border-radius: 18px !important;
      box-shadow: 0 16px 40px rgba(15, 30, 75, 0.12) !important;
      background: #FAF7F2 !important;
      border: 2.5px solid #C5A059 !important;
    }
    .book-page {
      padding: 24px 14px 20px 14px !important;
    }
    .book-page-left {
      border-right: none !important;
      border-bottom: 2px dashed #C5A059 !important;
      box-shadow: none !important;
    }
    .book-spine-crease {
      width: 100% !important;
      height: 14px !important;
      background: linear-gradient(180deg, rgba(0,0,0,0.06) 0%, rgba(197, 160, 89, 0.75) 50%, rgba(0,0,0,0.06) 100%) !important;
    }
    .book-ribbon-tassel {
      width: 45% !important;
      height: 3px !important;
    }
    .book-page-right {
      border-left: none !important;
      box-shadow: none !important;
      padding-top: 20px !important;
    }
    .royal-dignitaries-grid {
      grid-template-columns: 1fr !important;
      gap: 12px !important;
      margin: 12px 0 6px 0 !important;
    }
    .royal-dignitary-card {
      padding: 12px 10px !important;
    }
    .royal-guest-img-frame {
      width: 96px !important;
      height: 110px !important;
      margin-bottom: 6px !important;
    }
    .royal-guest-title-name {
      font-size: 15.5px !important;
    }
    .royal-guest-detail-text {
      font-size: 9.5px !important;
    }
    .royal-leukquant-logo {
      height: 48px !important;
    }
    .royal-date-big {
      font-size: 26px !important;
      margin: 4px 0 !important;
    }
    .royal-meta-item {
      font-size: 11px !important;
      padding: 4px 10px !important;
    }
    .royal-inst-footer {
      flex-direction: column !important;
      gap: 8px !important;
      padding-top: 10px !important;
    }
    .royal-inst-left-crest {
      height: 42px !important;
    }
    .royal-actions-container {
      flex-direction: column !important;
      width: 100% !important;
      gap: 8px !important;
    }
    .btn-material-primary, .btn-material-outline {
      width: 100% !important;
      justify-content: center !important;
      padding: 11px 16px !important;
      font-size: 13px !important;
    }
  }

  /* Small Smartphones (<= 480px) */
  @media (max-width: 480px) {
    .hero-badge-pill {
      font-size: 10px !important;
      padding: 5px 12px !important;
    }
    .royal-header-tag {
      font-size: 12px !important;
      letter-spacing: 0.22em !important;
    }
    .royal-lead-title {
      font-size: 11px !important;
    }
    .royal-guest-title-name {
      font-size: 14.5px !important;
    }
    .royal-guest-img-frame {
      width: 85px !important;
      height: 98px !important;
    }
    .royal-date-big {
      font-size: 22px !important;
    }
    .audio-toggle-btn {
      width: 40px !important;
      height: 40px !important;
      bottom: 16px !important;
      right: 16px !important;
      font-size: 14px !important;
    }
  }"""

responsive_pattern = r'(\/\* Tablets & Mobile Devices.*?)(\/\* Print Stylesheet)'
content = re.sub(responsive_pattern, mobile_css + '\n\n  \\2', content, flags=re.DOTALL)


# 3. Update JavaScript logic with Generous Pacing for Unsealing
js_animations = """    // 3. GSAP Master Animations & Royal Envelope Functions
    let isEnvelopeOpened = false;

    function openRoyalEnvelope(isAuto = false) {
      if (window.innerWidth <= 850) {
        // Mobile: directly flat & fully open
        isEnvelopeOpened = true;
        const card = document.getElementById('invitation-card');
        if (card) gsap.to(card, { opacity: 1, y: 0, scale: 1, duration: 0.5 });
        triggerCardPolishReveal();
        return;
      }

      if (isEnvelopeOpened && isAuto) return;
      isEnvelopeOpened = true;

      const seal = document.getElementById('royal-wax-seal');
      const flap = document.getElementById('envelope-flap');
      const pocket = document.getElementById('envelope-pocket-flaps');
      const card = document.getElementById('invitation-card');

      showToast('👑 Unsealing Royal Mascot Signet...');
      
      const tl = gsap.timeline();

      // Step 1: Wax seal crack & burst (clearly visible unsealing pace)
      tl.to(seal, {
        scale: 1.25,
        boxShadow: '0 0 45px rgba(212, 175, 55, 1)',
        duration: 0.7,
        ease: 'power2.out',
        onComplete: () => {
          spawnConfettiBurst();
          if (seal) seal.classList.add('broken');
        }
      });

      // Step 2: Flap rotates open majestically
      tl.to(flap, {
        rotateX: 180,
        opacity: 0,
        duration: 1.4,
        ease: 'power3.inOut'
      }, '+=0.2');

      // Step 3: Pocket flaps gently dissolve
      tl.to(pocket, {
        opacity: 0,
        y: 40,
        duration: 0.9,
        ease: 'power2.out'
      }, '-=0.8');

      // Step 4: Card emerges upward & expands flat
      tl.fromTo(card,
        { y: 70, scale: 0.90, opacity: 0.3 },
        {
          y: 0,
          scale: 1.0,
          opacity: 1,
          duration: 1.5,
          ease: 'power3.out'
        },
        '-=0.7'
      );

      // Step 5: Card polish sheen sweep
      tl.add(() => {
        showToast('✨ Royal Invitation Folio Unfolded');
        triggerCardPolishReveal();
      }, '-=0.4');
    }

    function replayEnvelopeAnimation() {
      if (window.innerWidth <= 850) {
        showToast('👑 Royal Invitation Folio Active');
        triggerCardPolishReveal();
        return;
      }
      const seal = document.getElementById('royal-wax-seal');
      const flap = document.getElementById('envelope-flap');
      const pocket = document.getElementById('envelope-pocket-flaps');
      const card = document.getElementById('invitation-card');

      isEnvelopeOpened = false;
      if (seal) seal.classList.remove('broken');
      if (flap) flap.classList.remove('opened');
      if (pocket) pocket.classList.remove('hidden');

      gsap.set(seal, { scale: 1, opacity: 1 });
      gsap.set(flap, { rotateX: 0, opacity: 1 });
      gsap.set(pocket, { opacity: 1, y: 0 });
      gsap.set(card, { y: 70, scale: 0.90, opacity: 0.3 });

      setTimeout(() => {
        openRoyalEnvelope(false);
      }, 400);
    }

    let isFolioFolded = false;
    function toggleBookFold() {
      const leftPage = document.querySelector('.book-page-left');
      const rightPage = document.querySelector('.book-page-right');
      if (!leftPage || !rightPage) return;

      if (!isFolioFolded) {
        isFolioFolded = true;
        gsap.to(leftPage, { rotateY: -18, transformOrigin: 'right center', duration: 0.6, ease: 'power2.out' });
        gsap.to(rightPage, { rotateY: 18, transformOrigin: 'left center', duration: 0.6, ease: 'power2.out' });
        showToast('📖 3D Folio Perspective Flexed');
      } else {
        isFolioFolded = false;
        gsap.to([leftPage, rightPage], { rotateY: 0, duration: 0.6, ease: 'power2.out' });
        showToast('📖 2-Page Royal Spread Flat');
      }
    }

    function initGsapAnimations() {
      // (A) Parallax Blobs
      gsap.to('.pblob-1', {
        y: -180,
        x: 60,
        scale: 1.2,
        ease: 'none',
        scrollTrigger: {
          trigger: 'body',
          start: 'top top',
          end: 'bottom bottom',
          scrub: 1.5,
          invalidateOnRefresh: true
        }
      });
      gsap.to('.pblob-2', {
        y: 220,
        x: -80,
        scale: 0.9,
        ease: 'none',
        scrollTrigger: {
          trigger: 'body',
          start: 'top top',
          end: 'bottom bottom',
          scrub: 2,
          invalidateOnRefresh: true
        }
      });
      gsap.to('.pblob-3', {
        y: -140,
        scale: 1.15,
        ease: 'none',
        scrollTrigger: {
          trigger: 'body',
          start: 'top top',
          end: 'bottom bottom',
          scrub: 1.2,
          invalidateOnRefresh: true
        }
      });

      // (B) Hero Section Entrance
      const heroTitle = document.getElementById('hero-title-split');
      if (heroTitle) {
        const text = heroTitle.innerText.trim();
        heroTitle.innerHTML = text.split('').map(c => `<span class="char" style="display:inline-block;">${c === ' ' ? '&nbsp;' : c}</span>`).join('');
        
        gsap.from('#hero-title-split .char', {
          y: 60,
          opacity: 0,
          duration: 0.9,
          stagger: 0.04,
          ease: 'power3.out',
          delay: 0.1
        });
      }

      gsap.from('.hero-badge-pill', {
        y: -30,
        opacity: 0,
        duration: 0.9,
        ease: 'power3.out',
        delay: 0.05
      });

      gsap.from('.hero-subtitle', {
        y: 35,
        opacity: 0,
        duration: 0.9,
        ease: 'power3.out',
        delay: 0.3
      });

      // Hero Parallax Background Layers
      gsap.to('#hero-far', {
        y: 120,
        ease: 'none',
        scrollTrigger: {
          trigger: '#hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 0.25,
          invalidateOnRefresh: true
        }
      });

      gsap.to('#hero-mid', {
        y: 200,
        ease: 'none',
        scrollTrigger: {
          trigger: '#hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 0.5,
          invalidateOnRefresh: true
        }
      });

      // Gold Scroll Line fade
      gsap.to('#hero-gold-line', {
        opacity: 0,
        ease: 'power1.out',
        scrollTrigger: {
          trigger: '#hero',
          start: 'top top',
          end: '+=60',
          scrub: true,
          invalidateOnRefresh: true
        }
      });

      // Spotlight Glow on Envelope
      gsap.fromTo('#envelope-spotlight',
        { opacity: 0 },
        {
          opacity: 0.65,
          ease: 'power2.inOut',
          scrollTrigger: {
            trigger: '#invitation',
            start: 'top 80%',
            end: 'top 20%',
            scrub: 1,
            invalidateOnRefresh: true
          }
        }
      );

      // (C) SECTION 2: OFFICIAL ROYAL INVITATION TRIGGER
      if (window.innerWidth <= 850) {
        gsap.fromTo('#invitation-card',
          { opacity: 0, y: 35 },
          {
            opacity: 1,
            y: 0,
            duration: 0.9,
            ease: 'power2.out',
            scrollTrigger: {
              trigger: '#invitation',
              start: 'top 80%',
              once: true,
              onEnter: () => {
                triggerCardPolishReveal();
              }
            }
          }
        );
      } else {
        ScrollTrigger.create({
          trigger: '#invitation',
          start: 'top 70%',
          once: true,
          onEnter: () => {
            // Generous visible delay so user sees the sealed envelope first
            setTimeout(() => {
              openRoyalEnvelope(true);
            }, 800);
          }
        });
      }

      // Card polish sheen sweep
      function triggerCardPolishReveal() {
        const sheen = document.getElementById('card-sheen');
        if (sheen) {
          gsap.fromTo(sheen,
            { left: '-150%' },
            { left: '150%', duration: 1.6, ease: 'power2.inOut' }
          );
        }
      }

      // 3D Mouse Parallax Tilt on Envelope Bed (Desktop only)
      if (window.innerWidth > 900 && !isReducedMotion) {
        const envelope = document.getElementById('envelope-bed');
        const card = document.getElementById('invitation-card');
        if (envelope && card) {
          envelope.addEventListener('mousemove', (e) => {
            const rect = envelope.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotX = ((y - centerY) / centerY) * -4.5;
            const rotY = ((x - centerX) / centerX) * 4.5;
            gsap.to(envelope, {
              rotateX: rotX,
              rotateY: rotY,
              duration: 0.35,
              ease: 'power2.out',
              transformPerspective: 1600
            });
          });
          envelope.addEventListener('mouseleave', () => {
            gsap.to(envelope, {
              rotateX: 0,
              rotateY: 0,
              duration: 0.7,
              ease: 'power3.out'
            });
          });
        }
      }

      // Auto Gold Sheen Sweep every 8s
      setInterval(() => {
        triggerCardPolishReveal();
      }, 8000);

      // (D) DIORAMA SHOWCASE PINNED HORIZONTAL SCROLL (#showcase)
      const showcaseTrack = document.getElementById('showcase-track');
      if (showcaseTrack && window.innerWidth > 900 && !isReducedMotion) {
        const getScrollAmount = () => -(showcaseTrack.scrollWidth - window.innerWidth + 80);

        gsap.to(showcaseTrack, {
          x: getScrollAmount,
          ease: 'none',
          scrollTrigger: {
            trigger: '#showcase',
            start: 'top top',
            end: () => `+=${showcaseTrack.scrollWidth}`,
            pin: true,
            scrub: 1,
            invalidateOnRefresh: true,
            onUpdate: (self) => {
              const fill = document.getElementById('showcase-progress');
              if (fill) fill.style.width = (self.progress * 100) + '%';
            }
          }
        });

        document.querySelectorAll('.showcase-img').forEach((img) => {
          gsap.fromTo(img,
            { xPercent: -12 },
            {
              xPercent: 12,
              ease: 'none',
              scrollTrigger: {
                trigger: '#showcase',
                start: 'top top',
                end: () => `+=${showcaseTrack.scrollWidth}`,
                scrub: 0.85,
                invalidateOnRefresh: true
              }
            }
          );
        });
      }

      // (E) VENUE SECTION PARALLAX (#venue)
      gsap.to('#venue-bg', {
        y: 100,
        ease: 'none',
        scrollTrigger: {
          trigger: '#venue',
          start: 'top bottom',
          end: 'bottom top',
          scrub: 0.3,
          invalidateOnRefresh: true
        }
      });

      gsap.fromTo('#venue-card',
        { y: 50, opacity: 0, scale: 0.96 },
        {
          y: 0,
          opacity: 1,
          scale: 1,
          duration: 1.0,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: '#venue-card',
            start: 'top 85%',
            invalidateOnRefresh: true
          }
        }
      );

      // (F) COUNTDOWN SCALE (#countdown)
      if (!isReducedMotion) {
        gsap.fromTo('#countdown-heading',
          { scale: 1.25, opacity: 0.4 },
          {
            scale: 1.0,
            opacity: 1,
            ease: 'none',
            scrollTrigger: {
              trigger: '#countdown',
              start: 'top 80%',
              end: 'top 20%',
              scrub: 1,
              invalidateOnRefresh: true
            }
          }
        );
      }
    }"""

js_pattern = r'\/\/\s*3\.\s*GSAP Master Animations.*?(?=\/\/\s*4\.\s*Live Countdown)'
content = re.sub(js_pattern, js_animations + '\n\n', content, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated template.html with paced unsealing! Total length: {len(content)} characters.")
