# -*- coding: utf-8 -*-
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Section 2 CSS
css_pattern = r'/\*\s*=========================================================\s*3\.\s*SECTION 2:.*?(?=/\*\s*=========================================================\s*4\.|\.showcase-pinned-section)'

new_css = """/* =========================================================
     3. SECTION 2: LUXURY 3D DOUBLE-SIDE OPENING BOOKLET
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

  /* Desktop Envelope Bed / Frame */
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

  /* =========================================================
     3D DOUBLE-SIDE OPENING BOOKLET (ROYAL BOOK FOLIO)
     ========================================================= */
  .book-stage-perspective {
    width: 100%;
    position: relative;
    perspective: 2000px;
    transform-style: preserve-3d;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .royal-book-folio {
    display: grid;
    grid-template-columns: 1fr 22px 1fr;
    background: #FAF7F2;
    border: 3.5px solid #C5A059;
    border-radius: 22px;
    box-shadow: inset 0 0 0 5px #FAF7F2, inset 0 0 0 8px #C5A059, 0 35px 90px rgba(0, 0, 0, 0.6);
    position: relative;
    width: 100%;
    overflow: visible;
    z-index: 20;
    transform-style: preserve-3d;
    will-change: transform, opacity;
    transition: box-shadow 0.4s ease;
  }

  /* 3D DOUBLE-SIDED BOOK COVERS (GATEFOLD DOORS) */
  .book-gate-cover {
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
    transition: transform 1.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.8s ease, visibility 0.8s;
    cursor: pointer;
    overflow: hidden;
  }

  .book-gate-cover::before {
    content: '';
    position: absolute;
    inset: 8px;
    border: 1.5px dashed rgba(212, 175, 55, 0.5);
    border-radius: 12px;
    pointer-events: none;
  }

  .gate-left {
    left: 0;
    border-radius: 20px 0 0 20px;
    border-right: 2px solid #D4AF37;
    transform-origin: left center;
  }

  .gate-right {
    right: 0;
    border-radius: 0 20px 20px 0;
    border-left: 2px solid #D4AF37;
    transform-origin: right center;
  }

  .book-gate-cover.opened.gate-left {
    transform: rotateY(-140deg);
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
  }

  .book-gate-cover.opened.gate-right {
    transform: rotateY(140deg);
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
  }

  /* Center Gold Latch Seal on Closed Covers */
  .gate-center-seal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, #F59E0B 0%, #D4AF37 45%, #8D6105 85%, #593D02 100%);
    border: 3.5px solid #FEF3C7;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.7), 0 0 25px rgba(212, 175, 55, 0.6);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 50;
    pointer-events: auto;
    cursor: pointer;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.6s ease;
    animation: sealGlowPulse 2.4s infinite alternate;
  }

  .gate-center-seal.opened {
    transform: translate(-50%, -50%) scale(1.4) rotate(25deg);
    opacity: 0;
    pointer-events: none;
    visibility: hidden;
  }

  @keyframes sealGlowPulse {
    0% { box-shadow: 0 10px 25px rgba(0,0,0,0.7), 0 0 15px rgba(212,175,55,0.4); transform: translate(-50%, -50%) scale(1); }
    100% { box-shadow: 0 15px 35px rgba(0,0,0,0.9), 0 0 35px rgba(212,175,55,0.85); transform: translate(-50%, -50%) scale(1.06); }
  }

  .gate-center-seal img {
    height: 38px;
    width: 38px;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4)) brightness(1.15);
  }

  .gate-center-seal span {
    font-family: var(--font-royal);
    font-size: 8px;
    font-weight: 900;
    letter-spacing: 0.14em;
    color: #FEF3C7;
    margin-top: -2px;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
  }

  .gate-cover-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    z-index: 2;
  }

  .gate-cover-crest {
    height: 48px;
    width: auto;
    filter: drop-shadow(0 4px 10px rgba(212, 175, 55, 0.5));
  }

  .gate-cover-title {
    font-family: var(--font-royal);
    font-size: 15px;
    font-weight: 900;
    color: #FEF3C7;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);
  }

  .gate-cover-sub {
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 700;
    color: #D4AF37;
    letter-spacing: 0.12em;
    text-transform: uppercase;
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
    transform-style: preserve-3d;
    transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .book-page-left {
    background: linear-gradient(90deg, #FCFBF8 0%, #F5EFE4 100%);
    border-right: 1px solid rgba(197, 160, 89, 0.35);
    box-shadow: inset -15px 0 25px -10px rgba(0, 0, 0, 0.08);
    transform-origin: right center;
  }

  .book-page-right {
    background: linear-gradient(270deg, #FCFBF8 0%, #F5EFE4 100%);
    border-left: 1px solid rgba(197, 160, 89, 0.35);
    box-shadow: inset 15px 0 25px -10px rgba(0, 0, 0, 0.08);
    transform-origin: left center;
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
    box-shadow: 0 4px 14px rgba(0, 102, 255, 0.35);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .btn-material-primary:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(0, 102, 255, 0.45);
  }

  .btn-material-secondary {
    background: #FFFFFF;
    color: var(--text-heading);
    border: 1.5px solid #CBD5E1;
    border-radius: var(--radius-full);
    padding: 10px 22px;
    font-family: var(--font-body);
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .btn-material-secondary:hover {
    background: #F8FAFC;
    border-color: #94A3B8;
    transform: translateY(-2px);
  }

  /* =========================================================
     MOBILE RESPONSIVE: NO ENVELOPE + COMPACT 2-PAGE SPREAD BOOKLET
     ========================================================= */
  @media (max-width: 850px) {
    .envelope-pinned-section {
      padding: 30px 8px 50px 8px !important;
    }

    /* IN MOBILE: REMOVE ENVELOPE BED COMPLETELY */
    .royal-envelope-bed {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
      min-height: auto !important;
      max-width: 100% !important;
      perspective: 1200px;
    }

    .envelope-bed-lining,
    .envelope-top-crest-bar {
      display: none !important;
    }

    .envelope-header-hint {
      margin-bottom: 14px;
    }

    .envelope-hint-title {
      font-size: 22px !important;
    }

    .envelope-hint-subtitle {
      font-size: 12px !important;
    }

    /* BOOKLET SIZING ON MOBILE: Compact side-by-side 2-page book spread */
    .royal-book-folio {
      grid-template-columns: 1fr 14px 1fr !important;
      border: 2px solid #C5A059 !important;
      border-radius: 14px !important;
      box-shadow: inset 0 0 0 3px #FAF7F2, inset 0 0 0 4.5px #C5A059, 0 16px 40px rgba(0,0,0,0.25) !important;
      width: 100% !important;
      max-width: 600px !important;
      margin: 0 auto !important;
    }

    .book-page {
      padding: 14px 8px 12px 8px !important;
    }

    .book-spine-crease {
      width: 14px !important;
    }

    .book-ribbon-tassel {
      width: 2.5px !important;
    }

    .corner-vignette {
      width: 32px !important;
      height: 32px !important;
    }

    .royal-header-tag {
      font-size: 10.5px !important;
      letter-spacing: 0.2em !important;
      margin-bottom: 2px !important;
    }

    .royal-gold-crest {
      width: 24px !important;
      margin-bottom: 3px !important;
    }

    .royal-lead-title {
      font-size: 8.5px !important;
      line-height: 1.15 !important;
      letter-spacing: 0.02em !important;
    }

    .royal-gold-flourish {
      font-size: 9px !important;
      margin: 2px auto !important;
    }
    .royal-gold-flourish::before,
    .royal-gold-flourish::after {
      width: 18px !important;
    }

    .royal-sub-line {
      font-size: 8px !important;
      line-height: 1.2 !important;
    }

    .royal-dignitaries-grid {
      grid-template-columns: 1fr 1fr !important;
      gap: 5px !important;
      margin: 6px 0 4px 0 !important;
    }

    .royal-dignitary-card {
      padding: 6px 3px !important;
      border-radius: 10px !important;
    }

    .royal-guest-img-frame {
      width: 52px !important;
      height: 60px !important;
      border-radius: 8px !important;
      margin-bottom: 3px !important;
    }

    .royal-guest-kicker {
      font-size: 6.5px !important;
      padding: 1px 4px !important;
      margin-bottom: 2px !important;
    }

    .royal-guest-title-name {
      font-size: 9.5px !important;
      line-height: 1.1 !important;
      margin-bottom: 1.5px !important;
    }

    .royal-guest-detail-text {
      font-size: 6.5px !important;
      line-height: 1.2 !important;
      margin: 1px 0 !important;
    }

    /* RIGHT PAGE MOBILE STYLING */
    .royal-leukquant-logo {
      height: 34px !important;
      margin: 1px 0 !important;
    }

    .royal-date-big {
      font-size: 17px !important;
      margin: 2px 0 !important;
    }

    .royal-meta-list {
      gap: 3px !important;
      margin: 3px 0 6px 0 !important;
    }

    .royal-meta-item {
      font-size: 8px !important;
      padding: 2px 8px !important;
      gap: 4px !important;
    }

    .royal-meta-badge-num {
      width: 13px !important;
      height: 13px !important;
      font-size: 7.5px !important;
    }

    .royal-inst-footer {
      gap: 4px !important;
      padding-top: 6px !important;
      margin-top: 5px !important;
      justify-content: center !important;
    }

    .royal-inst-left-crest {
      height: 24px !important;
    }

    .royal-inst-mid-info {
      min-width: 100px !important;
    }
    .royal-inst-mid-info h4 {
      font-size: 8px !important;
      margin-bottom: 1px !important;
    }
    .royal-inst-mid-info p {
      font-size: 6.5px !important;
      line-height: 1.15 !important;
    }

    .royal-inst-right-seals img {
      height: 18px !important;
    }

    .royal-actions-container {
      margin-top: 6px !important;
      gap: 5px !important;
    }

    .btn-material-primary {
      padding: 6px 14px !important;
      font-size: 9.5px !important;
    }

    .btn-material-secondary {
      padding: 5px 12px !important;
      font-size: 9.5px !important;
    }

    /* Mobile Covers */
    .book-gate-cover {
      padding: 12px 6px !important;
    }
    .gate-cover-crest {
      height: 32px !important;
    }
    .gate-cover-title {
      font-size: 11px !important;
      letter-spacing: 0.1em !important;
    }
    .gate-cover-sub {
      font-size: 8px !important;
    }
    .gate-center-seal {
      width: 58px !important;
      height: 58px !important;
    }
    .gate-center-seal img {
      height: 26px !important;
      width: 26px !important;
    }
    .gate-center-seal span {
      font-size: 6.5px !important;
    }
  }

"""

html = re.sub(css_pattern, new_css, html, flags=re.DOTALL)

# 2. Update Section 1 HTML (Double-sided opening booklet)
html_section_pattern = r'<section class="envelope-pinned-section" id="invitation">.*?</section>'

new_section_html = """<section class="envelope-pinned-section" id="invitation">
    <div class="envelope-gold-spotlight" id="envelope-spotlight"></div>

    <div class="envelope-stage-wrapper" id="envelope-stage">
      <div class="envelope-header-hint" id="envelope-hint">
        <div class="envelope-hint-controls">
          <span class="envelope-hint-pill">👑 Royal Double-Side Booklet &bull; 2026</span>
          <button class="btn-envelope-action" onclick="replayBookletAnimation()">✨ Open / Close Booklet</button>
          <button class="btn-envelope-action" onclick="toggleBookFold()">📖 3D Perspective</button>
        </div>
        <h2 class="envelope-hint-title">Grand Launch Invitation</h2>
        <p class="envelope-hint-subtitle">Official Inauguration &bull; September 07, 2026 &bull; 09:30 AM IST</p>
      </div>

      <!-- Luxury Envelope / Book Bed -->
      <div class="royal-envelope-bed" id="envelope-bed">
        <div class="envelope-bed-lining"></div>

        <!-- Top Envelope Header Crest Ribbon (Desktop) -->
        <div class="envelope-top-crest-bar">
          <img src="__MASCOT__" alt="LeukQuant Royal Seal">
          <span>👑 Official Royal Invitation &bull; Jeppiaar Institute of Technology</span>
        </div>

        <!-- 3D Perspective Stage for Booklet -->
        <div class="book-stage-perspective" id="book-stage">
          
          <!-- 2-Page Bi-Fold Royal Book Folio -->
          <div class="royal-book-folio" id="invitation-card">
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
                    <div class="royal-gold-flourish" style="margin: 2px auto;">«««««——————»»»»»</div>
                    <div class="royal-guest-detail-text" style="font-weight: 700;">INDUSTRY 5.0 MENTOR</div>
                    <div class="royal-guest-detail-text" style="font-weight: 800; color: #0F172A;">ACTIVE DEFENSE ADVISORY</div>
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
      </div>
    </div>
  </section>"""

html = re.sub(html_section_pattern, new_section_html, html, flags=re.DOTALL)

# 3. Update JavaScript animations for double-sided booklet opening
js_function_pattern = r'//\s*2\.\s*SECTION 2 ENVELOPE INTERACTION.*?function initGsapAnimations\(\)\s*\{'

new_js_functions = """// 2. SECTION 2: 3D DOUBLE-SIDE OPENING BOOKLET INTERACTION
    let isBookletOpened = false;
    let isFolioFolded = false;

    function openRoyalBooklet(autoTriggered = false) {
      if (isBookletOpened && !autoTriggered) return;
      isBookletOpened = true;

      const coverLeft = document.getElementById('gate-cover-left');
      const coverRight = document.getElementById('gate-cover-right');
      const centerSeal = document.getElementById('gate-center-seal');
      const pageLeft = document.getElementById('book-page-left');
      const pageRight = document.getElementById('book-page-right');
      const sheen = document.getElementById('card-sheen');

      // 1. Break / Open Center Seal
      if (centerSeal) {
        centerSeal.classList.add('opened');
      }

      // 2. Swing open Left and Right covers simultaneously (Double-Side Open!)
      if (coverLeft && coverRight) {
        coverLeft.classList.add('opened');
        coverRight.classList.add('opened');
      }

      // 3. Unfold left & right pages from subtle 3D perspective to crisp flat spread
      if (pageLeft && pageRight) {
        gsap.fromTo(pageLeft,
          { rotateY: 15, transformOrigin: 'right center' },
          { rotateY: 0, duration: 1.2, ease: 'power2.out', delay: 0.1 }
        );
        gsap.fromTo(pageRight,
          { rotateY: -15, transformOrigin: 'left center' },
          { rotateY: 0, duration: 1.2, ease: 'power2.out', delay: 0.1 }
        );
      }

      // 4. Gold sheen sweep across unfolded 2-page spread
      if (sheen) {
        gsap.fromTo(sheen,
          { left: '-150%' },
          { left: '150%', duration: 1.8, ease: 'power2.inOut', delay: 0.4 }
        );
      }

      if (!autoTriggered) {
        showToast('📖 Royal Double-Side Booklet Opened!');
      }
    }

    function replayBookletAnimation() {
      const coverLeft = document.getElementById('gate-cover-left');
      const coverRight = document.getElementById('gate-cover-right');
      const centerSeal = document.getElementById('gate-center-seal');
      const pageLeft = document.getElementById('book-page-left');
      const pageRight = document.getElementById('book-page-right');

      if (isBookletOpened) {
        // Close booklet
        isBookletOpened = false;
        if (coverLeft && coverRight) {
          coverLeft.classList.remove('opened');
          coverRight.classList.remove('opened');
        }
        if (centerSeal) {
          centerSeal.classList.remove('opened');
        }
        if (pageLeft && pageRight) {
          gsap.to([pageLeft, pageRight], { rotateY: 0, duration: 0.4 });
        }
        showToast('📖 Booklet Closed');
      } else {
        // Open booklet
        openRoyalBooklet(false);
      }
    }

    function toggleBookFold() {
      const leftPage = document.getElementById('book-page-left');
      const rightPage = document.getElementById('book-page-right');
      if (!leftPage || !rightPage) return;

      if (!isFolioFolded) {
        isFolioFolded = true;
        gsap.to(leftPage, { rotateY: -16, transformOrigin: 'right center', duration: 0.6, ease: 'power2.out' });
        gsap.to(rightPage, { rotateY: 16, transformOrigin: 'left center', duration: 0.6, ease: 'power2.out' });
        showToast('📖 3D Booklet Perspective Flexed');
      } else {
        isFolioFolded = false;
        gsap.to([leftPage, rightPage], { rotateY: 0, duration: 0.6, ease: 'power2.out' });
        showToast('📖 2-Page Royal Spread Flat');
      }
    }

    function initGsapAnimations() {"""

html = re.sub(js_function_pattern, new_js_functions, html, flags=re.DOTALL)

# 4. Update ScrollTrigger for #invitation
trigger_pattern = r'//\s*\(C\)\s*SECTION 2:.*?//\s*Card polish sheen sweep'

new_trigger = """// (C) SECTION 2: OFFICIAL ROYAL BOOKLET SCROLL TRIGGER
      ScrollTrigger.create({
        trigger: '#invitation',
        start: 'top 75%',
        once: true,
        onEnter: () => {
          // Smooth scroll-triggered double-sided opening!
          setTimeout(() => {
            openRoyalBooklet(true);
          }, 350);
        }
      });

      // Card polish sheen sweep"""

html = re.sub(trigger_pattern, new_trigger, html, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html successfully!")
