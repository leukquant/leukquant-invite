import json
import base64
import os

print("Running render_portal.py...")

# Load assets
with open(r'extracted/assets.json', 'r', encoding='utf-8') as f:
    assets = json.load(f)

# Ensure mascot uses extracted/mascot_trans.png
mascot_path = r'extracted/mascot_trans.png'
if os.path.exists(mascot_path):
    with open(mascot_path, 'rb') as mf:
        assets['mascot'] = f"data:image/png;base64,{base64.b64encode(mf.read()).decode('utf-8')}"

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>LeukQuant Grand Launch 2026 | Official Invitation & Interactive Portal</title>
<meta name="description" content="Official Grand Launch & Inauguration of LeukQuant - AI-Powered Active Deception & Autonomous Cybersecurity. Chief Guest: Dr N. Marie Wilson on September 07, 2026 at Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam.">
<meta name="theme-color" content="#070B14">

<!-- Social OpenGraph -->
<meta property="og:title" content="LeukQuant Grand Launch 2026 // Official Invitation">
<meta property="og:description" content="Join us for the Grand Launch of LeukQuant at Ground Floor Auditorium, JIT Kunnam. Chief Guest: Dr. N. Marie Wilson.">
<meta property="og:type" content="website">

<!-- Premium Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">

<style>
  :root {{
    --bg-dark: #070B14;
    --bg-surface: #0B1222;
    --bg-card: rgba(13, 21, 38, 0.88);
    --bg-card-glow: rgba(0, 240, 255, 0.08);
    
    --brand-blue: #0066FF;
    --brand-blue-glow: rgba(0, 102, 255, 0.4);
    --brand-cyan: #00F0FF;
    --brand-cyan-glow: rgba(0, 240, 255, 0.45);
    --brand-purple: #8B5CF6;
    --brand-emerald: #10B981;
    
    --text-heading: #FFFFFF;
    --text-body: #CBD5E1;
    --text-muted: #94A3B8;
    --text-dim: #64748B;
    
    --border-card: 1px solid rgba(0, 240, 255, 0.3);
    --border-glass: 1px solid rgba(255, 255, 255, 0.12);
    
    --radius-full: 9999px;
    --radius-xl: 26px;
    --radius-lg: 18px;
    --radius-md: 12px;
    --radius-sm: 8px;
    
    --font-heading: 'Plus Jakarta Sans', 'Space Grotesk', -apple-system, sans-serif;
    --font-body: 'Plus Jakarta Sans', -apple-system, sans-serif;
    --font-mono: 'Fira Code', monospace;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    scroll-behavior: smooth;
  }}

  body {{
    background-color: var(--bg-dark);
    background-image: 
      radial-gradient(circle at 50% 0%, rgba(0, 102, 255, 0.22) 0%, transparent 60%),
      radial-gradient(circle at 10% 35%, rgba(0, 240, 255, 0.12) 0%, transparent 50%),
      radial-gradient(circle at 90% 65%, rgba(139, 92, 246, 0.18) 0%, transparent 55%),
      radial-gradient(circle at 50% 100%, rgba(0, 240, 255, 0.15) 0%, transparent 70%),
      linear-gradient(180deg, #070B14 0%, #0D162B 50%, #050811 100%);
    min-height: 100vh;
    font-family: var(--font-body);
    color: var(--text-body);
    overflow-x: hidden;
    position: relative;
    padding-bottom: 60px;
  }}

  /* Ambient Particle Canvas & Matrix Grid */
  #particles-canvas {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }}

  #confetti-canvas {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 99999;
  }}

  .cyber-grid-backdrop {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: 44px 44px;
    background-image: 
      linear-gradient(to right, rgba(0, 240, 255, 0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0, 240, 255, 0.035) 1px, transparent 1px);
    pointer-events: none;
    z-index: 2;
  }}

  /* Ambient Scanning Radar Beam on Body */
  .radar-sweep-beam {{
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg at 50% 50%, rgba(0, 240, 255, 0.04) 0deg, transparent 60deg, transparent 360deg);
    pointer-events: none;
    z-index: 2;
    animation: rotateRadar 14s linear infinite;
  }}

  @keyframes rotateRadar {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
  }}

  /* Top Floating Cyber Controls Bar (No Navbar) */
  .top-hud-bar {{
    position: fixed;
    top: 18px;
    right: 20px;
    z-index: 1000;
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .hud-pill-btn {{
    background: rgba(11, 18, 34, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 240, 255, 0.3);
    color: var(--brand-cyan);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 600;
    padding: 7px 14px;
    border-radius: var(--radius-full);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 12px rgba(0, 240, 255, 0.15);
    transition: all 0.25s ease;
  }}

  .hud-pill-btn:hover {{
    background: rgba(0, 240, 255, 0.15);
    border-color: var(--brand-cyan);
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
  }}

  .hud-pill-btn.active {{
    border-color: #10B981;
    color: #10B981;
  }}

  /* Main Wrapper */
  .portal-wrapper {{
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 18px 60px 18px;
    position: relative;
    z-index: 10;
  }}

  /* =========================================================
     3D PERSPECTIVE INVITATION CARD (#card)
     ========================================================= */
  .card-3d-wrap {{
    perspective: 1400px;
    margin-bottom: 40px;
  }}

  #card {{
    background: var(--bg-card);
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    border: 1px solid rgba(0, 240, 255, 0.35);
    border-radius: var(--radius-xl);
    box-shadow: 
      0 0 60px rgba(0, 240, 255, 0.18),
      0 30px 80px rgba(0, 0, 0, 0.85),
      inset 0 0 40px rgba(0, 240, 255, 0.06);
    padding: 44px 38px;
    position: relative;
    overflow: hidden;
    transition: transform 0.15s ease-out, box-shadow 0.3s ease;
    transform-style: preserve-3d;
  }}

  @media (max-width: 640px) {{
    #card {{
      padding: 30px 20px;
    }}
  }}

  /* Specular Glare Layer for 3D card tilt */
  .card-glare {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at 50% 0%, rgba(0, 240, 255, 0.18) 0%, transparent 70%);
    pointer-events: none;
    mix-blend-mode: overlay;
    opacity: 0.8;
    transition: opacity 0.3s ease;
  }}

  /* Cyber Corner HUD Brackets */
  .hud-bracket {{
    position: absolute;
    width: 24px;
    height: 24px;
    border: 2px solid var(--brand-cyan);
    pointer-events: none;
    filter: drop-shadow(0 0 6px var(--brand-cyan));
  }}
  .hud-tl {{ top: 14px; left: 14px; border-right: none; border-bottom: none; }}
  .hud-tr {{ top: 14px; right: 14px; border-left: none; border-bottom: none; }}
  .hud-bl {{ bottom: 14px; left: 14px; border-right: none; border-top: none; }}
  .hud-br {{ bottom: 14px; right: 14px; border-left: none; border-top: none; }}

  /* Top Institutional Row */
  .inst-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    padding-bottom: 22px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 28px;
  }}

  .inst-left {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}

  .inst-crest {{
    height: 58px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 0 14px rgba(255, 255, 255, 0.35));
    transition: transform 0.3s ease;
  }}
  .inst-crest:hover {{
    transform: scale(1.05) rotate(-2deg);
  }}

  .inst-titles {{
    display: flex;
    flex-direction: column;
  }}

  .inst-name {{
    font-family: var(--font-heading);
    font-size: 17px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    line-height: 1.25;
  }}

  .inst-sub {{
    font-size: 12px;
    color: var(--text-muted);
    font-weight: 500;
    margin-top: 2px;
  }}

  .inst-badges {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .accred-badge {{
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: var(--radius-md);
    transition: all 0.25s ease;
  }}
  .accred-badge:hover {{
    background: rgba(0, 240, 255, 0.08);
    border-color: var(--brand-cyan);
    transform: translateY(-2px);
  }}

  .badge-icon {{
    height: 26px;
    width: auto;
    object-fit: contain;
  }}

  .badge-lbl {{
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--brand-cyan);
    font-weight: 700;
    line-height: 1.2;
    text-transform: uppercase;
  }}

  /* Hero Centerpiece inside Card */
  .hero-block {{
    text-align: center;
    padding: 6px 0 24px 0;
  }}

  .launch-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 18px;
    background: linear-gradient(90deg, rgba(0, 240, 255, 0.14), rgba(139, 92, 246, 0.14));
    border: 1px solid rgba(0, 240, 255, 0.4);
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    color: var(--brand-cyan);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 22px;
    box-shadow: 0 0 16px rgba(0, 240, 255, 0.2);
    animation: pillPulse 3s infinite ease-in-out;
  }}

  @keyframes pillPulse {{
    0%, 100% {{ box-shadow: 0 0 16px rgba(0, 240, 255, 0.2); }}
    50% {{ box-shadow: 0 0 28px rgba(0, 240, 255, 0.5); }}
  }}

  .launch-pill .dot {{
    width: 7px;
    height: 7px;
    background: var(--brand-cyan);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--brand-cyan);
    animation: blinkBeacon 1.2s infinite;
  }}

  @keyframes blinkBeacon {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.3; transform: scale(1.4); }}
  }}

  /* Mascot & Logo Stage */
  .visuals-stage {{
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 22px;
    margin-bottom: 20px;
  }}

  /* Floating Mascot Container */
  .mascot-wrap {{
    position: relative;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .mascot-aura {{
    position: absolute;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0, 240, 255, 0.35) 0%, rgba(139, 92, 246, 0.2) 45%, transparent 70%);
    filter: blur(12px);
    animation: auraPulse 3.5s infinite ease-in-out;
    pointer-events: none;
  }}

  @keyframes auraPulse {{
    0%, 100% {{ transform: scale(0.9); opacity: 0.7; }}
    50% {{ transform: scale(1.25); opacity: 1; }}
  }}

  .mascot-img {{
    height: 145px;
    width: auto;
    max-width: 135px;
    object-fit: contain;
    filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.85));
    animation: floatMascot 4s ease-in-out infinite;
    position: relative;
    z-index: 2;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.3s ease;
  }}

  .mascot-img:hover {{
    transform: translateY(-12px) scale(1.08) rotate(3deg);
    filter: drop-shadow(0 20px 40px rgba(0, 240, 255, 0.5));
  }}

  @keyframes floatMascot {{
    0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
    50% {{ transform: translateY(-10px) rotate(1.5deg); }}
  }}

  .logo-img {{
    height: 62px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 0 22px rgba(0, 240, 255, 0.55));
    transition: transform 0.3s ease, filter 0.3s ease;
  }}
  .logo-img:hover {{
    transform: scale(1.04);
    filter: drop-shadow(0 0 30px rgba(0, 240, 255, 0.8));
  }}

  .launch-subheading {{
    font-family: var(--font-heading);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.24em;
    color: var(--brand-cyan);
    text-transform: uppercase;
    margin-bottom: 8px;
    text-shadow: 0 0 14px rgba(0, 240, 255, 0.6);
  }}

  .launch-title {{
    font-family: var(--font-heading);
    font-size: 40px;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.02em;
    text-transform: uppercase;
    color: #FFFFFF;
    margin-bottom: 14px;
    background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 40%, #00F0FF 80%, #8B5CF6 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShine 6s linear infinite;
    text-shadow: 0 0 35px rgba(0, 240, 255, 0.35);
  }}

  @keyframes textShine {{
    0% {{ background-position: 0% center; }}
    50% {{ background-position: 100% center; }}
    100% {{ background-position: 0% center; }}
  }}

  .platform-tagline {{
    font-size: 15px;
    color: var(--text-body);
    max-width: 680px;
    margin: 0 auto 20px auto;
    line-height: 1.6;
  }}
  .platform-tagline strong {{
    color: #FFFFFF;
    font-weight: 700;
  }}

  .invitation-callout {{
    background: linear-gradient(135deg, rgba(0, 240, 255, 0.06) 0%, rgba(139, 92, 246, 0.06) 100%);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: var(--radius-md);
    padding: 16px 24px;
    font-size: 13.5px;
    color: #E2E8F0;
    line-height: 1.65;
    text-align: center;
    margin-bottom: 26px;
    box-shadow: inset 0 0 20px rgba(0, 240, 255, 0.05);
  }}

  /* VIP Chief Guest Spotlight Card */
  .guest-spotlight {{
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(26, 36, 60, 0.85) 100%);
    border: 1px solid rgba(0, 240, 255, 0.35);
    border-radius: var(--radius-lg);
    padding: 22px 26px;
    margin-bottom: 26px;
    display: flex;
    align-items: center;
    gap: 22px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(0, 240, 255, 0.15);
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
  }}
  .guest-spotlight:hover {{
    border-color: var(--brand-cyan);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 35px rgba(0, 240, 255, 0.3);
    transform: translateY(-2px);
  }}

  .guest-spotlight::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(180deg, var(--brand-cyan), var(--brand-purple));
  }}

  .guest-photo-ring {{
    width: 100px;
    height: 100px;
    flex-shrink: 0;
    border-radius: 50%;
    padding: 3px;
    background: linear-gradient(135deg, var(--brand-cyan), var(--brand-blue), var(--brand-purple));
    box-shadow: 0 0 22px rgba(0, 240, 255, 0.45);
    position: relative;
  }}

  .guest-photo {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    background: #1E293B;
  }}

  .guest-info {{
    flex: 1;
  }}

  .guest-vip-tag {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    background: rgba(0, 240, 255, 0.12);
    border: 1px solid rgba(0, 240, 255, 0.35);
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: 10.5px;
    font-weight: 700;
    color: var(--brand-cyan);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }}

  .guest-name {{
    font-family: var(--font-heading);
    font-size: 22px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.01em;
    margin-bottom: 3px;
  }}

  .guest-title {{
    font-size: 13.5px;
    color: var(--brand-cyan);
    font-weight: 600;
    margin-bottom: 2px;
  }}

  .guest-org {{
    font-size: 12.5px;
    color: var(--text-muted);
  }}

  @media (max-width: 640px) {{
    .guest-spotlight {{
      flex-direction: column;
      text-align: center;
    }}
    .launch-title {{
      font-size: 28px;
    }}
  }}

  /* Event Details 3-Column Grid */
  .meta-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 26px;
  }}

  @media (max-width: 700px) {{
    .meta-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  .meta-card {{
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-md);
    padding: 16px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all 0.25s ease;
  }}
  .meta-card:hover {{
    border-color: var(--brand-cyan);
    background: rgba(15, 23, 42, 0.95);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 240, 255, 0.16);
  }}

  .meta-icon-box {{
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: rgba(0, 240, 255, 0.1);
    border: 1px solid rgba(0, 240, 255, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: var(--brand-cyan);
    flex-shrink: 0;
  }}

  .meta-content {{
    display: flex;
    flex-direction: column;
  }}

  .m-lbl {{
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 700;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
  }}

  .m-val {{
    font-family: var(--font-heading);
    font-size: 14.5px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 1px;
  }}

  .m-sub {{
    font-size: 11.5px;
    color: var(--brand-cyan);
    font-weight: 500;
  }}

  /* Real-Time Countdown Radar HUD */
  .countdown-card {{
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(8, 13, 24, 0.95) 100%);
    border: 1px solid rgba(0, 240, 255, 0.3);
    border-radius: var(--radius-lg);
    padding: 22px 20px;
    text-align: center;
    margin-bottom: 26px;
    box-shadow: inset 0 0 25px rgba(0, 240, 255, 0.05);
  }}

  .countdown-lbl {{
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    color: var(--brand-cyan);
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 14px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }}

  .countdown-grid {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
  }}

  .time-tile {{
    background: rgba(5, 8, 16, 0.9);
    border: 1px solid rgba(0, 240, 255, 0.3);
    border-radius: 10px;
    padding: 10px 16px;
    min-width: 74px;
    box-shadow: 0 0 14px rgba(0, 240, 255, 0.12);
  }}

  .time-num {{
    font-family: var(--font-mono);
    font-size: 26px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1;
    margin-bottom: 4px;
    text-shadow: 0 0 14px rgba(0, 240, 255, 0.65);
  }}

  .time-tag {{
    font-family: var(--font-mono);
    font-size: 9px;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }}

  .time-sep {{
    font-family: var(--font-mono);
    font-size: 20px;
    font-weight: 700;
    color: var(--brand-cyan);
    animation: blinkBeacon 1s infinite;
  }}

  /* Quick Actions Row inside Card */
  .card-actions {{
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 20px;
  }}

  .btn-primary-cyan {{
    padding: 11px 24px;
    background: linear-gradient(135deg, #00F0FF 0%, #0066FF 100%);
    color: #05070E;
    font-family: var(--font-heading);
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    border-radius: var(--radius-full);
    border: none;
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.45);
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }}
  .btn-primary-cyan:hover {{
    transform: translateY(-2px);
    box-shadow: 0 0 32px rgba(0, 240, 255, 0.75);
  }}

  .btn-secondary-glass {{
    padding: 11px 20px;
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(0, 240, 255, 0.3);
    color: #FFFFFF;
    font-family: var(--font-heading);
    font-size: 13px;
    font-weight: 600;
    border-radius: var(--radius-full);
    cursor: pointer;
    text-decoration: none;
    transition: all 0.25s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }}
  .btn-secondary-glass:hover {{
    background: rgba(0, 240, 255, 0.14);
    border-color: var(--brand-cyan);
    color: var(--brand-cyan);
    transform: translateY(-2px);
  }}

  /* Card Bottom Stamp */
  .card-footer-stamp {{
    text-align: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 18px;
    margin-top: 24px;
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-dim);
    letter-spacing: 0.06em;
  }}

  /* =========================================================
     INTERACTIVE ACTIVE DECEPTION RADAR SIMULATOR SECTION
     ========================================================= */
  .radar-sim-card {{
    background: linear-gradient(135deg, rgba(13, 21, 38, 0.95) 0%, rgba(8, 14, 28, 0.95) 100%);
    border: 1px solid rgba(0, 240, 255, 0.3);
    border-radius: var(--radius-xl);
    padding: 32px 28px;
    margin-bottom: 40px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
  }}

  .sim-layout {{
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 26px;
    align-items: center;
  }}

  @media (max-width: 768px) {{
    .sim-layout {{
      grid-template-columns: 1fr;
    }}
  }}

  .radar-screen-wrap {{
    position: relative;
    width: 100%;
    aspect-ratio: 1;
    max-width: 320px;
    margin: 0 auto;
    border-radius: 50%;
    border: 2px solid rgba(0, 240, 255, 0.4);
    background: radial-gradient(circle, rgba(0, 240, 255, 0.06) 0%, rgba(5, 9, 18, 0.95) 80%);
    overflow: hidden;
    box-shadow: 0 0 35px rgba(0, 240, 255, 0.25), inset 0 0 25px rgba(0, 240, 255, 0.15);
  }}

  .radar-crosshair-h, .radar-crosshair-v {{
    position: absolute;
    background: rgba(0, 240, 255, 0.2);
    pointer-events: none;
  }}
  .radar-crosshair-h {{ top: 50%; left: 0; width: 100%; height: 1px; }}
  .radar-crosshair-v {{ top: 0; left: 50%; width: 1px; height: 100%; }}

  .radar-ring {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px dashed rgba(0, 240, 255, 0.25);
    pointer-events: none;
  }}
  .ring-1 {{ width: 33%; height: 33%; }}
  .ring-2 {{ width: 66%; height: 66%; }}
  .ring-3 {{ width: 95%; height: 95%; }}

  .radar-sweep {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: conic-gradient(from 0deg, rgba(0, 240, 255, 0.4) 0deg, transparent 50deg, transparent 360deg);
    animation: radarSpin 4s linear infinite;
    pointer-events: none;
  }}

  @keyframes radarSpin {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
  }}

  .radar-blip {{
    position: absolute;
    width: 8px;
    height: 8px;
    background: #00F0FF;
    border-radius: 50%;
    box-shadow: 0 0 10px #00F0FF;
    animation: blipPulse 2s infinite;
  }}

  @keyframes blipPulse {{
    0%, 100% {{ transform: scale(1); opacity: 0.9; }}
    50% {{ transform: scale(1.6); opacity: 0.4; }}
  }}

  .terminal-box {{
    background: rgba(5, 8, 16, 0.92);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: var(--radius-md);
    padding: 16px;
    font-family: var(--font-mono);
    font-size: 12px;
    color: #A7F3D0;
    height: 200px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .log-line {{
    line-height: 1.4;
  }}
  .log-cyan {{ color: var(--brand-cyan); }}
  .log-purple {{ color: #C084FC; }}
  .log-amber {{ color: #FBBF24; }}
  .log-red {{ color: #F87171; }}

  /* =========================================================
     LAUNCH AGENDA TIMELINE
     ========================================================= */
  .agenda-section {{
    margin-bottom: 40px;
  }}

  .agenda-timeline {{
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: relative;
    padding-left: 28px;
  }}

  .agenda-timeline::before {{
    content: '';
    position: absolute;
    top: 10px;
    bottom: 10px;
    left: 10px;
    width: 2px;
    background: linear-gradient(180deg, var(--brand-cyan), var(--brand-blue), var(--brand-purple));
  }}

  .agenda-item {{
    position: relative;
    background: rgba(13, 21, 38, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-md);
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    transition: all 0.25s ease;
  }}
  .agenda-item:hover {{
    border-color: var(--brand-cyan);
    background: rgba(13, 21, 38, 0.95);
    transform: translateX(4px);
    box-shadow: 0 6px 20px rgba(0, 240, 255, 0.15);
  }}

  .agenda-dot {{
    position: absolute;
    left: -24px;
    top: 50%;
    transform: translateY(-50%);
    width: 12px;
    height: 12px;
    background: var(--brand-cyan);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--brand-cyan);
  }}

  .agenda-time {{
    font-family: var(--font-mono);
    font-size: 13px;
    font-weight: 700;
    color: var(--brand-cyan);
    min-width: 90px;
  }}

  .agenda-title {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 700;
    color: #FFFFFF;
  }}

  .agenda-speaker {{
    font-size: 12px;
    color: var(--text-muted);
  }}

  /* =========================================================
     HOLOGRAPHIC VIP PASS GENERATOR
     ========================================================= */
  .vip-pass-card {{
    background: linear-gradient(135deg, rgba(13, 21, 38, 0.95) 0%, rgba(9, 14, 27, 0.95) 100%);
    border: 1px solid rgba(0, 240, 255, 0.35);
    border-radius: var(--radius-xl);
    padding: 34px 30px;
    margin-bottom: 40px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
  }}

  .pass-layout {{
    display: grid;
    grid-template-columns: 1fr 1.1fr;
    gap: 30px;
    align-items: center;
  }}

  @media (max-width: 800px) {{
    .pass-layout {{
      grid-template-columns: 1fr;
    }}
  }}

  .form-group {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .form-lbl {{
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--brand-cyan);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }}

  .form-input, .form-select {{
    padding: 12px 16px;
    background: rgba(5, 8, 16, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    color: #FFFFFF;
    font-family: var(--font-body);
    font-size: 14px;
    outline: none;
    transition: all 0.25s ease;
  }}
  .form-input:focus, .form-select:focus {{
    border-color: var(--brand-cyan);
    box-shadow: 0 0 16px rgba(0, 240, 255, 0.3);
  }}

  .form-select option {{
    background: #0B1120;
    color: #FFFFFF;
  }}

  /* The Digital VIP Badge */
  .digital-badge {{
    position: relative;
    background: linear-gradient(135deg, rgba(20, 32, 58, 0.95) 0%, rgba(10, 16, 32, 0.95) 100%);
    border: 1px solid rgba(0, 240, 255, 0.5);
    border-radius: var(--radius-lg);
    padding: 24px;
    box-shadow: 0 0 35px rgba(0, 240, 255, 0.25), 0 15px 40px rgba(0, 0, 0, 0.85);
    overflow: hidden;
  }}

  .digital-badge::before {{
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent 40%, rgba(0, 240, 255, 0.15) 50%, transparent 60%);
    animation: holoSweep 6s infinite linear;
    pointer-events: none;
  }}

  @keyframes holoSweep {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
  }}

  .badge-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 12px;
    margin-bottom: 16px;
  }}

  .badge-brand {{
    font-family: var(--font-heading);
    font-size: 18px;
    font-weight: 800;
    color: #FFFFFF;
  }}

  .badge-tier-pill {{
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 700;
    padding: 4px 10px;
    background: linear-gradient(135deg, var(--brand-cyan), var(--brand-blue));
    color: #05070E;
    border-radius: 4px;
    text-transform: uppercase;
  }}

  .badge-body {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
  }}

  .badge-user-name {{
    font-family: var(--font-heading);
    font-size: 20px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 2px;
  }}

  .badge-user-org {{
    font-size: 12px;
    color: var(--text-muted);
  }}

  .badge-meta {{
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--brand-cyan);
    margin-top: 8px;
    line-height: 1.4;
  }}

  .badge-qr {{
    width: 80px;
    height: 80px;
    background: #FFFFFF;
    border-radius: 8px;
    padding: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    flex-shrink: 0;
  }}
  .badge-qr svg {{
    width: 100%;
    height: 100%;
  }}

  /* =========================================================
     VENUE SECTION (JIT KUNNAM)
     ========================================================= */
  .venue-card {{
    background: linear-gradient(135deg, rgba(13, 21, 38, 0.85) 0%, rgba(8, 13, 25, 0.95) 100%);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: var(--radius-xl);
    padding: 32px;
    margin-bottom: 40px;
  }}

  .venue-layout {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
    align-items: center;
  }}

  @media (max-width: 768px) {{
    .venue-layout {{
      grid-template-columns: 1fr;
    }}
  }}

  .venue-info {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  .venue-tag {{
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--brand-cyan);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }}

  .venue-name {{
    font-family: var(--font-heading);
    font-size: 24px;
    font-weight: 800;
    color: #FFFFFF;
  }}

  .venue-addr {{
    font-size: 14px;
    color: var(--text-muted);
    line-height: 1.6;
  }}

  .venue-gps-tag {{
    font-family: var(--font-mono);
    font-size: 11px;
    color: #10B981;
  }}

  .venue-map-wrap {{
    height: 220px;
    border-radius: var(--radius-lg);
    border: 1px solid rgba(0, 240, 255, 0.3);
    overflow: hidden;
    background: #040711;
  }}

  .venue-map-wrap iframe {{
    width: 100%;
    height: 100%;
    border: none;
    filter: invert(90%) hue-rotate(180deg) brightness(85%) contrast(120%);
  }}

  /* Footer */
  .site-footer {{
    text-align: center;
    padding: 40px 20px 20px 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
  }}

  .footer-logo {{
    height: 48px;
    width: auto;
    object-fit: contain;
    margin-bottom: 16px;
    filter: drop-shadow(0 0 16px rgba(0, 240, 255, 0.4));
  }}

  .footer-text {{
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 8px;
  }}

  .footer-sub {{
    font-family: var(--font-mono);
    font-size: 10px;
    color: var(--text-dim);
  }}

  /* Toast Notification */
  #toast {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    padding: 12px 24px;
    background: rgba(11, 18, 34, 0.95);
    backdrop-filter: blur(12px);
    border: 1px solid var(--brand-cyan);
    border-radius: 8px;
    color: #FFFFFF;
    font-family: var(--font-mono);
    font-size: 12px;
    box-shadow: 0 0 25px rgba(0, 240, 255, 0.45);
    z-index: 100000;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.3s ease;
    pointer-events: none;
  }}

  #toast.show {{
    opacity: 1;
    transform: translateY(0);
  }}
</style>
</head>
<body>

  <!-- Background Ambient FX -->
  <canvas id="particles-canvas"></canvas>
  <canvas id="confetti-canvas"></canvas>
  <div class="cyber-grid-backdrop"></div>
  <div class="radar-sweep-beam"></div>

  <!-- Top HUD Quick Controls (No Navbar) -->
  <div class="top-hud-bar">
    <button class="hud-pill-btn" id="audio-toggle-btn" onclick="toggleAudioFx()">
      <span id="audio-icon">&#128266;</span>
      <span id="audio-label">FX: ON</span>
    </button>
    <a href="#vip-pass" class="hud-pill-btn" onclick="playBeep()">
      &#127915; VIP Pass
    </a>
  </div>

  <!-- Main Content Wrapper -->
  <div class="portal-wrapper">

    <!-- =========================================================
         3D INTERACTIVE INVITATION CARD CENTERPIECE (#card)
         ========================================================= -->
    <div class="card-3d-wrap">
      <div id="card">
        <div class="card-glare" id="card-glare"></div>

        <!-- Corner HUD brackets -->
        <div class="hud-bracket hud-tl"></div>
        <div class="hud-bracket hud-tr"></div>
        <div class="hud-bracket hud-bl"></div>
        <div class="hud-bracket hud-br"></div>

        <!-- Institutional Header -->
        <div class="inst-header">
          <div class="inst-left">
            <img src="{assets["jit_crest"]}" alt="Jeppiaar Institute of Technology" class="inst-crest">
            <div class="inst-titles">
              <div class="inst-name">JEPPIAAR INSTITUTE OF TECHNOLOGY</div>
              <div class="inst-sub">JIT Foundation Incubation Center & AI Excellence Hub</div>
            </div>
          </div>

          <div class="inst-badges">
            <div class="accred-badge">
              <img src="{assets["naac_seal"]}" alt="NAAC A+" class="badge-icon">
              <div class="badge-lbl">NAAC<br>A+ Grade</div>
            </div>
            <div class="accred-badge">
              <img src="{assets["nba_logo"]}" alt="NBA Accredited" class="badge-icon">
              <div class="badge-lbl">NBA<br>Tier-1</div>
            </div>
          </div>
        </div>

        <!-- Hero Centerpiece -->
        <div class="hero-block">
          <div class="launch-pill">
            <span class="dot"></span>
            <span>Official Grand Launch &bull; September 07, 2026</span>
          </div>

          <div class="visuals-stage">
            <div class="mascot-wrap" onclick="mascotReact()">
              <div class="mascot-aura"></div>
              <img src="{assets["mascot"]}" alt="LeukQuant Mascot" class="mascot-img" id="mascot-avatar" title="Click for Cyber Reaction!">
            </div>
            <img src="{assets["leukquant_logo"]}" alt="LeukQuant Logo" class="logo-img">
          </div>

          <div class="launch-subheading">// OFFICIAL INAUGURATION &amp; PRODUCT LAUNCH //</div>
          <h1 class="launch-title">GRAND LAUNCH 2026</h1>

          <p class="platform-tagline">
            Introducing <strong>AI-Powered Active Deception &amp; Autonomous Cybersecurity</strong> with dynamic Honeypots, Ghost-Net AI decoys, and sub-10s canary tripwires.
          </p>

          <div class="invitation-callout">
            The Management, Faculty, Research Innovation Council, and Founding Team of <strong>LeukQuant</strong> cordially invite you to the auspicious Grand Launch and Live Demonstration of our AI-Powered Cybersecurity Platform.
          </div>
        </div>

        <!-- Chief Guest VIP Spotlight Card -->
        <div class="guest-spotlight">
          <div class="guest-photo-ring">
            <img src="{assets["guest_photo"]}" alt="Dr N. Marie Wilson" class="guest-photo">
          </div>
          <div class="guest-info">
            <div class="guest-vip-tag">&#9733; CHIEF GUEST &amp; KEYNOTE SPEAKER</div>
            <div class="guest-name">DR. N. MARIE WILSON, B.Tech., M.B.A., Ph.D.</div>
            <div class="guest-title">Director, Jeppiaar Institute of Technology</div>
            <div class="guest-org">Managing Trustee, Jeppiaar Educational Trust &amp; JIT Foundation</div>
          </div>
        </div>

        <!-- Event Details 3-Column Grid -->
        <div class="meta-grid">
          <div class="meta-card">
            <div class="meta-icon-box">&#128197;</div>
            <div class="meta-content">
              <div class="m-lbl">LAUNCH DATE</div>
              <div class="m-val">SEP 07, 2026</div>
              <div class="m-sub">Monday &bull; 10:00 AM IST</div>
            </div>
          </div>

          <div class="meta-card">
            <div class="meta-icon-box">&#9200;</div>
            <div class="meta-content">
              <div class="m-lbl">SESSION</div>
              <div class="m-val">10:00 AM &ndash; 01:30 PM</div>
              <div class="m-sub">Keynote, Live Demo &amp; High Tea</div>
            </div>
          </div>

          <div class="meta-card">
            <div class="meta-icon-box">&#128205;</div>
            <div class="meta-content">
              <div class="m-lbl">VENUE</div>
              <div class="m-val">GROUND FLOOR AUDITORIUM</div>
              <div class="m-sub">JIT Kunnam, Chennai</div>
            </div>
          </div>
        </div>

        <!-- Real-Time Countdown Radar -->
        <div class="countdown-card">
          <div class="countdown-lbl">
            <span>&#9889; TIME TO HISTORIC LAUNCH RADAR</span>
          </div>
          <div class="countdown-grid">
            <div class="time-tile">
              <div class="time-num" id="cd-days">00</div>
              <div class="time-tag">DAYS</div>
            </div>
            <div class="time-sep">:</div>
            <div class="time-tile">
              <div class="time-num" id="cd-hours">00</div>
              <div class="time-tag">HOURS</div>
            </div>
            <div class="time-sep">:</div>
            <div class="time-tile">
              <div class="time-num" id="cd-mins">00</div>
              <div class="time-tag">MINUTES</div>
            </div>
            <div class="time-sep">:</div>
            <div class="time-tile">
              <div class="time-num" id="cd-secs">00</div>
              <div class="time-tag">SECONDS</div>
            </div>
          </div>
        </div>

        <!-- Card Quick Action Buttons -->
        <div class="card-actions">
          <button class="btn-primary-cyan" onclick="addToCalendar()">
            &#128197; Add to Calendar (.ics)
          </button>
          <button class="btn-secondary-glass" onclick="shareWhatsapp()">
            &#128172; Share via WhatsApp
          </button>
          <button class="btn-secondary-glass" onclick="copyInviteLink()">
            &#128279; Copy Link
          </button>
        </div>

        <div class="card-footer-stamp">
          LEUKQUANT INCUBATED CYBERSECURITY STARTUP &bull; JIT FOUNDATION &bull; ACTIVE DECEPTION PLATFORM &bull; CHENNAI, INDIA
        </div>
      </div>
    </div> <!-- End of #card -->

    <!-- =========================================================
         LIVE ACTIVE DECEPTION RADAR & TELEMETRY SIMULATOR
         ========================================================= -->
    <section class="radar-sim-card">
      <div style="text-align: center; margin-bottom: 24px;">
        <div style="font-family: var(--font-mono); font-size: 11px; color: var(--brand-cyan); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 6px;">
          // INTERACTIVE PLATFORM SIMULATOR //
        </div>
        <h2 style="font-family: var(--font-heading); font-size: 26px; font-weight: 800; color: #FFFFFF;">
          Active Deception Honeypot Radar
        </h2>
      </div>

      <div class="sim-layout">
        <!-- Radar View -->
        <div class="radar-screen-wrap" id="radar-screen">
          <div class="radar-crosshair-h"></div>
          <div class="radar-crosshair-v"></div>
          <div class="radar-ring ring-1"></div>
          <div class="radar-ring ring-2"></div>
          <div class="radar-ring ring-3"></div>
          <div class="radar-sweep"></div>
          <!-- Dynamic Blips will be placed here -->
          <div class="radar-blip" style="top: 30%; left: 65%;"></div>
          <div class="radar-blip" style="top: 70%; left: 35%;"></div>
        </div>

        <!-- Interactive Telemetry Console -->
        <div>
          <div style="display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;">
            <button class="btn-secondary-glass" style="font-size: 11.5px; padding: 7px 14px;" onclick="deployDecoy()">
              &#128373; Deploy Decoy
            </button>
            <button class="btn-secondary-glass" style="font-size: 11.5px; padding: 7px 14px;" onclick="triggerTripwire()">
              &#9889; Trigger Canary Tripwire
            </button>
            <button class="btn-secondary-glass" style="font-size: 11.5px; padding: 7px 14px;" onclick="clearLogs()">
              &#129529; Clear
            </button>
          </div>

          <div class="terminal-box" id="telemetry-terminal">
            <div class="log-line log-cyan">[00:00:01] LeukQuant Deception Core v2.4 initialized.</div>
            <div class="log-line log-purple">[00:00:02] Ghost-Net AI synthetic network topology active.</div>
            <div class="log-line log-amber">[00:00:04] 24 Canary tripwire tokens listening on internal subnets.</div>
            <div class="log-line">[00:00:05] Monitoring active threat vectors... Ready.</div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         LAUNCH EVENT AGENDA TIMELINE
         ========================================================= -->
    <section class="agenda-section">
      <div style="text-align: center; margin-bottom: 24px;">
        <div style="font-family: var(--font-mono); font-size: 11px; color: var(--brand-cyan); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 6px;">
          // EVENT ITINERARY //
        </div>
        <h2 style="font-family: var(--font-heading); font-size: 26px; font-weight: 800; color: #FFFFFF;">
          Launch Schedule &amp; Keynotes
        </h2>
      </div>

      <div class="agenda-timeline">
        <div class="agenda-item">
          <div class="agenda-dot"></div>
          <div class="agenda-time">10:00 AM</div>
          <div style="flex: 1;">
            <div class="agenda-title">Inaugural Address &amp; Dignitary Welcome</div>
            <div class="agenda-speaker">JIT Faculty &amp; Research Innovation Council</div>
          </div>
        </div>

        <div class="agenda-item">
          <div class="agenda-dot"></div>
          <div class="agenda-time">10:30 AM</div>
          <div style="flex: 1;">
            <div class="agenda-title">Keynote Speech: Next-Gen AI Defense</div>
            <div class="agenda-speaker">Dr. N. Marie Wilson &bull; Director, Jeppiaar Institute of Technology</div>
          </div>
        </div>

        <div class="agenda-item">
          <div class="agenda-dot"></div>
          <div class="agenda-time">11:15 AM</div>
          <div style="flex: 1;">
            <div class="agenda-title">Official Unveiling of LeukQuant Platform</div>
            <div class="agenda-speaker">Founding Engineering Team &amp; Product Architects</div>
          </div>
        </div>

        <div class="agenda-item">
          <div class="agenda-dot"></div>
          <div class="agenda-time">11:45 AM</div>
          <div style="flex: 1;">
            <div class="agenda-title">Live Attack Simulation &amp; Canary Demo</div>
            <div class="agenda-speaker">Autonomous Honeypots &amp; Ghost-Net Defense in Action</div>
          </div>
        </div>

        <div class="agenda-item">
          <div class="agenda-dot"></div>
          <div class="agenda-time">12:30 PM</div>
          <div style="flex: 1;">
            <div class="agenda-title">Networking, Incubation Tour &amp; High Tea</div>
            <div class="agenda-speaker">JIT Foundation Incubation Center</div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         HOLOGRAPHIC VIP PASS GENERATOR (RSVP)
         ========================================================= -->
    <section id="vip-pass" class="vip-pass-card">
      <div style="text-align: center; margin-bottom: 28px;">
        <div style="font-family: var(--font-mono); font-size: 11px; color: var(--brand-cyan); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 6px;">
          // DIGITAL CREDENTIAL PASS //
        </div>
        <h2 style="font-family: var(--font-heading); font-size: 26px; font-weight: 800; color: #FFFFFF;">
          Generate Your Official VIP Pass
        </h2>
      </div>

      <div class="pass-layout">
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div class="form-group">
            <label class="form-lbl">Attendee Full Name</label>
            <input type="text" id="pass-name" class="form-input" placeholder="e.g. Dr. Alexander Vance" value="Honored Delegate" oninput="updatePass()">
          </div>

          <div class="form-group">
            <label class="form-lbl">Organization / Institution</label>
            <input type="text" id="pass-org" class="form-input" placeholder="e.g. Cybersecurity Enterprise / JIT" value="Jeppiaar Institute of Technology" oninput="updatePass()">
          </div>

          <div class="form-group">
            <label class="form-lbl">Access Tier</label>
            <select id="pass-tier" class="form-select" onchange="updatePass()">
              <option value="VIP DELEGATE">VIP Delegate</option>
              <option value="SPECIAL INVITED GUEST">Special Invited Guest</option>
              <option value="CYBER RESEARCHER">Cyber Researcher</option>
              <option value="FACULTY & CLINICIAN">Faculty &amp; Leadership</option>
              <option value="INDUSTRY PARTNER">Industry Partner</option>
            </select>
          </div>

          <button class="btn-primary-cyan" style="width: 100%; justify-content: center; margin-top: 4px;" onclick="claimPass()">
            &#10004; Confirm RSVP &amp; Claim Digital Pass
          </button>
        </div>

        <!-- The Live Holographic Pass -->
        <div class="digital-badge" id="holo-pass-badge">
          <div class="badge-top">
            <div class="badge-brand">LEUKQUANT // ACCESS</div>
            <div class="badge-tier-pill" id="preview-tier">VIP DELEGATE</div>
          </div>

          <div class="badge-body">
            <div>
              <div class="badge-user-name" id="preview-name">Honored Delegate</div>
              <div class="badge-user-org" id="preview-org">Jeppiaar Institute of Technology</div>
              <div class="badge-meta">
                <span>SEP 07, 2026 // 10:00 AM IST</span><br>
                <span>GROUND FLOOR AUDITORIUM, JIT</span>
              </div>
            </div>

            <div class="badge-qr">
              <svg viewBox="0 0 100 100">
                <rect width="100" height="100" fill="#FFFFFF"/>
                <rect x="10" y="10" width="25" height="25" fill="#000000"/>
                <rect x="15" y="15" width="15" height="15" fill="#FFFFFF"/>
                <rect x="18" y="18" width="9" height="9" fill="#000000"/>
                <rect x="65" y="10" width="25" height="25" fill="#000000"/>
                <rect x="70" y="15" width="15" height="15" fill="#FFFFFF"/>
                <rect x="73" y="18" width="9" height="9" fill="#000000"/>
                <rect x="10" y="65" width="25" height="25" fill="#000000"/>
                <rect x="15" y="70" width="15" height="15" fill="#FFFFFF"/>
                <rect x="18" y="73" width="9" height="9" fill="#000000"/>
                <rect x="42" y="15" width="8" height="8" fill="#000000"/>
                <rect x="42" y="35" width="8" height="8" fill="#000000"/>
                <rect x="15" y="45" width="8" height="8" fill="#000000"/>
                <rect x="45" y="55" width="15" height="15" fill="#000000"/>
                <rect x="68" y="45" width="20" height="8" fill="#000000"/>
                <rect x="68" y="65" width="10" height="20" fill="#000000"/>
                <rect x="85" y="75" width="8" height="10" fill="#000000"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         VENUE SECTION (JIT KUNNAM)
         ========================================================= -->
    <section class="venue-card">
      <div class="venue-layout">
        <div class="venue-info">
          <div class="venue-tag">&#128205; VENUE LOCATION</div>
          <h2 class="venue-name">Ground Floor Auditorium</h2>
          <p class="venue-addr">
            Jeppiaar Institute of Technology,<br>
            Kunnam, Sunguvarchatram, Sriperumbudur,<br>
            Chennai, Tamil Nadu &ndash; 631604, India.
          </p>
          <div class="venue-gps-tag">
            <span>&#9889; Coordinates: 12.8711&deg; N, 79.9142&deg; E</span>
          </div>

          <div style="margin-top: 10px;">
            <a href="https://maps.google.com/?q=Jeppiaar+Institute+of+Technology+Kunnam" target="_blank" class="btn-primary-cyan" style="font-size: 12px; padding: 9px 20px;">
              &#10148; Open in Google Maps
            </a>
          </div>
        </div>

        <div class="venue-map-wrap">
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.7656641203914!2d79.9116!3d12.8711!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a52f4eb27e449df%3A0x6b04859f9ef21228!2sJeppiaar%20Institute%20of%20Technology!5e0!3m2!1sen!2sin!4v1690000000000" 
            allowfullscreen="" 
            loading="lazy">
          </iframe>
        </div>
      </div>
    </section>

  </div> <!-- End of .portal-wrapper -->

  <!-- Site Footer -->
  <footer class="site-footer">
    <img src="{assets["leukquant_logo"]}" alt="LeukQuant" class="footer-logo">
    <div class="footer-text">
      &copy; 2026 LeukQuant Inc. Incubated at JIT Foundation, Jeppiaar Institute of Technology. All Rights Reserved.
    </div>
    <div class="footer-sub">
      AI-POWERED ACTIVE DECEPTION &bull; AUTONOMOUS HONEYPOTS &bull; GHOST-NET &bull; SUB-10S CANARIES &bull; JIT KUNNAM
    </div>
  </footer>

  <!-- Toast Notification -->
  <div id="toast"></div>

  <!-- Interactive JavaScript -->
  <script>
    // =========================================================
    // 1. WEB AUDIO API SYNTHESIZER (ZERO EXTERNAL DEPENDENCY)
    // =========================================================
    let audioFxEnabled = true;
    let audioCtx = null;

    function initAudio() {{
      if (!audioCtx) {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {{
          audioCtx = new AudioContext();
        }}
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
    }}

    function toggleAudioFx() {{
      initAudio();
      audioFxEnabled = !audioFxEnabled;
      const icon = document.getElementById('audio-icon');
      const lbl = document.getElementById('audio-label');
      const btn = document.getElementById('audio-toggle-btn');
      
      if (audioFxEnabled) {{
        icon.innerHTML = '&#128266;';
        lbl.innerText = 'FX: ON';
        btn.classList.remove('active');
        playChime(600, 0.1);
        showToast('Cyber Audio FX Enabled');
      }} else {{
        icon.innerHTML = '&#128263;';
        lbl.innerText = 'FX: MUTED';
        btn.classList.add('active');
        showToast('Cyber Audio FX Muted');
      }}
    }}

    function playBeep(freq = 880, type = 'sine', duration = 0.08) {{
      if (!audioFxEnabled) return;
      try {{
        initAudio();
        if (!audioCtx) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{}}
    }}

    function playChime(freq = 523.25, duration = 0.35) {{
      if (!audioFxEnabled) return;
      try {{
        initAudio();
        if (!audioCtx) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(freq * 1.5, audioCtx.currentTime + duration);
        gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{}}
    }}

    // =========================================================
    // 2. AMBIENT PARTICLES CANVAS CONSTELLATION
    // =========================================================
    const pCanvas = document.getElementById('particles-canvas');
    const pCtx = pCanvas.getContext('2d');
    let pWidth, pHeight;
    let particles = [];

    function resizeCanvas() {{
      pWidth = pCanvas.width = window.innerWidth;
      pHeight = pCanvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Particle {{
      constructor() {{
        this.reset();
      }}
      reset() {{
        this.x = Math.random() * pWidth;
        this.y = Math.random() * pHeight;
        this.vx = (Math.random() - 0.5) * 0.6;
        this.vy = (Math.random() - 0.5) * 0.6;
        this.radius = Math.random() * 1.8 + 0.8;
        this.alpha = Math.random() * 0.5 + 0.2;
        this.color = Math.random() > 0.4 ? '#00F0FF' : '#8B5CF6';
      }}
      update() {{
        this.x += this.vx;
        this.y += this.vy;
        if (this.x < 0 || this.x > pWidth) this.vx *= -1;
        if (this.y < 0 || this.y > pHeight) this.vy *= -1;
      }}
      draw() {{
        pCtx.beginPath();
        pCtx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        pCtx.fillStyle = this.color;
        pCtx.globalAlpha = this.alpha;
        pCtx.fill();
      }}
    }}

    for (let i = 0; i < 55; i++) {{
      particles.push(new Particle());
    }}

    function animateParticles() {{
      pCtx.clearRect(0, 0, pWidth, pHeight);
      for (let i = 0; i < particles.length; i++) {{
        particles[i].update();
        particles[i].draw();

        // Connect nearby particles
        for (let j = i + 1; j < particles.length; j++) {{
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 110) {{
            pCtx.beginPath();
            pCtx.moveTo(particles[i].x, particles[i].y);
            pCtx.lineTo(particles[j].x, particles[j].y);
            pCtx.strokeStyle = '#00F0FF';
            pCtx.globalAlpha = (1 - dist / 110) * 0.15;
            pCtx.lineWidth = 0.75;
            pCtx.stroke();
          }}
        }}
      }}
      requestAnimationFrame(animateParticles);
    }}
    animateParticles();

    // =========================================================
    // 3. 3D CARD INTERACTIVE TILT & GLARE EFFECT
    // =========================================================
    const cardEl = document.getElementById('card');
    const glareEl = document.getElementById('card-glare');

    if (cardEl && glareEl) {{
      window.addEventListener('mousemove', (e) => {{
        const rect = cardEl.getBoundingClientRect();
        const cardCenterX = rect.left + rect.width / 2;
        const cardCenterY = rect.top + rect.height / 2;
        
        const mouseX = e.clientX - cardCenterX;
        const mouseY = e.clientY - cardCenterY;

        // Calculate rotation limits (subtle smooth tilt)
        const rotY = Math.max(Math.min((mouseX / (window.innerWidth / 2)) * 7, 7), -7);
        const rotX = Math.max(Math.min((-mouseY / (window.innerHeight / 2)) * 7, 7), -7);

        cardEl.style.transform = `rotateX(${{rotX.toFixed(2)}}deg) rotateY(${{rotY.toFixed(2)}}deg)`;
        
        // Glare tracking
        const glareX = ((e.clientX - rect.left) / rect.width) * 100;
        const glareY = ((e.clientY - rect.top) / rect.height) * 100;
        glareEl.style.background = `radial-gradient(circle at ${{glareX.toFixed(1)}}% ${{glareY.toFixed(1)}}%, rgba(0, 240, 255, 0.22) 0%, transparent 65%)`;
      }});

      window.addEventListener('mouseleave', () => {{
        cardEl.style.transform = `rotateX(0deg) rotateY(0deg)`;
      }});
    }}

    // =========================================================
    // 4. MASCOT INTERACTIVE REACTION
    // =========================================================
    function mascotReact() {{
      const mascot = document.getElementById('mascot-avatar');
      playChime(784, 0.25);
      showToast('⚡ LeukQuant Mascot: Active Defense Armed & Ready!');
      mascot.style.transform = 'translateY(-20px) scale(1.18) rotate(8deg)';
      setTimeout(() => {{
        mascot.style.transform = '';
      }}, 400);
      spawnConfettiBurst();
    }}

    // =========================================================
    // 5. LIVE COUNTDOWN TIMER
    // =========================================================
    const targetLaunchDate = new Date('September 7, 2026 10:00:00 GMT+0530').getTime();

    function updateCountdown() {{
      const now = new Date().getTime();
      const distance = targetLaunchDate - now;

      if (distance < 0) {{
        document.getElementById('cd-days').innerText = '00';
        document.getElementById('cd-hours').innerText = '00';
        document.getElementById('cd-mins').innerText = '00';
        document.getElementById('cd-secs').innerText = '00';
        return;
      }}

      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((distance % (1000 * 60)) / 1000);

      document.getElementById('cd-days').innerText = String(days).padStart(2, '0');
      document.getElementById('cd-hours').innerText = String(hours).padStart(2, '0');
      document.getElementById('cd-mins').innerText = String(mins).padStart(2, '0');
      document.getElementById('cd-secs').innerText = String(secs).padStart(2, '0');
    }}
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // =========================================================
    // 6. RADAR & TELEMETRY SIMULATOR
    // =========================================================
    const terminal = document.getElementById('telemetry-terminal');
    const radarScreen = document.getElementById('radar-screen');

    function logMessage(msg, type = 'cyan') {{
      const now = new Date();
      const timeStr = now.toTimeString().split(' ')[0];
      const div = document.createElement('div');
      div.className = `log-line log-${{type}}`;
      div.innerText = `[${{timeStr}}] ${{msg}}`;
      terminal.appendChild(div);
      terminal.scrollTop = terminal.scrollHeight;
    }}

    function deployDecoy() {{
      playBeep(1046.5, 'sine', 0.1);
      const decoys = [
        'Ghost SSH Honeypot port :2222 deployed on subnet 10.0.4.x',
        'Synthetic MySQL Database decoy seeded with canary tables.',
        'Simulated Active Directory Kerberos token trap established.',
        'High-interaction AWS IAM fake credential decoy activated.'
      ];
      const decoy = decoys[Math.floor(Math.random() * decoys.length)];
      logMessage(decoy, 'purple');

      // Add a dynamic radar blip
      const blip = document.createElement('div');
      blip.className = 'radar-blip';
      blip.style.top = `${{Math.random() * 70 + 15}}%`;
      blip.style.left = `${{Math.random() * 70 + 15}}%`;
      radarScreen.appendChild(blip);
      setTimeout(() => blip.remove(), 7000);
      showToast('Decoy Deployed to Network Mesh');
    }}

    function triggerTripwire() {{
      playBeep(440, 'sawtooth', 0.2);
      playBeep(659.25, 'sawtooth', 0.2);
      const alerts = [
        'TRIPWIRE HIT: Intruder probed fake config.env! Canary pinged in 3.4s.',
        'HONEYPOT BREACH: Unauthorized login attempt on decoy SSH trapped & forensic dumped.',
        'GHOST-NET ENGAGED: Lateral movement redirecting attacker into isolated sandbox.',
        'SUB-10S CANARY: Alert dispatched to Security Operations Slack & SOC.'
      ];
      const alert = alerts[Math.floor(Math.random() * alerts.length)];
      logMessage(alert, 'red');
      showToast('🚨 Tripwire Alert Triggered & Isolated in < 10s!');
      spawnConfettiBurst();
    }}

    function clearLogs() {{
      playBeep(500, 'sine', 0.05);
      terminal.innerHTML = '<div class="log-line log-cyan">System telemetry cleared. Monitoring active...</div>';
    }}

    // =========================================================
    // 7. HOLOGRAPHIC VIP PASS GENERATOR
    // =========================================================
    function updatePass() {{
      const name = document.getElementById('pass-name').value.trim() || 'Honored Delegate';
      const org = document.getElementById('pass-org').value.trim() || 'Jeppiaar Institute of Technology';
      const tier = document.getElementById('pass-tier').value;

      document.getElementById('preview-name').innerText = name;
      document.getElementById('preview-org').innerText = org;
      document.getElementById('preview-tier').innerText = tier;
    }}

    function claimPass() {{
      playChime(880, 0.4);
      spawnConfettiBurst();
      showToast('🎉 VIP Pass Registered & Claimed! Ready for Grand Launch.');
    }}

    // =========================================================
    // 8. CALENDAR & SHARE UTILITIES
    // =========================================================
    function addToCalendar() {{
      playBeep(600, 'triangle', 0.1);
      const icsData = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//LeukQuant//Launch Invitation//EN',
        'BEGIN:VEVENT',
        'UID:leukquant-launch-2026@jit',
        'DTSTAMP:20260901T000000Z',
        'DTSTART:20260907T043000Z',
        'DTEND:20260907T080000Z',
        'SUMMARY:LeukQuant Grand Launch & AI Deception Demonstration',
        'DESCRIPTION:Grand Launch of LeukQuant AI Cybersecurity Platform. Chief Guest: Dr N. Marie Wilson. Venue: Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam.',
        'LOCATION:Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam, Chennai, India',
        'STATUS:CONFIRMED',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('\\r\\n');

      const blob = new Blob([icsData], {{ type: 'text/calendar;charset=utf-8' }});
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute('download', 'LeukQuant_Grand_Launch.ics');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('📅 Calendar Event (.ics) Downloaded!');
    }}

    function shareWhatsapp() {{
      playBeep(700, 'sine', 0.1);
      const text = encodeURIComponent('Join us for the Grand Launch of LeukQuant (AI-Powered Active Deception & Cybersecurity Platform) on Sep 07, 2026 at Ground Floor Auditorium, Jeppiaar Institute of Technology! Chief Guest: Dr. N. Marie Wilson.');
      window.open(`https://api.whatsapp.com/send?text=${{text}}`, '_blank');
    }}

    function copyInviteLink() {{
      playBeep(800, 'sine', 0.1);
      navigator.clipboard.writeText(window.location.href).then(() => {{
        showToast('🔗 Invite Link Copied to Clipboard!');
      }}).catch(() => {{
        showToast('🔗 Link ready: ' + window.location.href);
      }});
    }}

    // =========================================================
    // 9. TOAST NOTIFICATION
    // =========================================================
    let toastTimeout = null;
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        t.classList.remove('show');
      }}, 3200);
    }}

    // =========================================================
    // 10. CONFETTI BURST CELEBRATION
    // =========================================================
    function spawnConfettiBurst() {{
      const cCanvas = document.getElementById('confetti-canvas');
      const cCtx = cCanvas.getContext('2d');
      cCanvas.width = window.innerWidth;
      cCanvas.height = window.innerHeight;

      let confettis = [];
      const colors = ['#00F0FF', '#0066FF', '#8B5CF6', '#10B981', '#FFD700', '#FFFFFF'];

      for (let i = 0; i < 90; i++) {{
        confettis.push({{
          x: cCanvas.width / 2,
          y: cCanvas.height * 0.45,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.8) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rot: Math.random() * 360,
          vrot: (Math.random() - 0.5) * 12,
          alpha: 1
        }});
      }}

      function renderConfetti() {{
        cCtx.clearRect(0, 0, cCanvas.width, cCanvas.height);
        let active = false;
        confettis.forEach(c => {{
          c.x += c.vx;
          c.y += c.vy;
          c.vy += 0.38;
          c.rot += c.vrot;
          c.alpha -= 0.015;
          if (c.alpha > 0) {{
            active = true;
            cCtx.save();
            cCtx.translate(c.x, c.y);
            cCtx.rotate((c.rot * Math.PI) / 180);
            cCtx.fillStyle = c.color;
            cCtx.globalAlpha = Math.max(0, c.alpha);
            cCtx.fillRect(-c.size/2, -c.size/2, c.size, c.size * 0.65);
            cCtx.restore();
          }}
        }});

        if (active) {{
          requestAnimationFrame(renderConfetti);
        }} else {{
          cCtx.clearRect(0, 0, cCanvas.width, cCanvas.height);
        }}
      }}
      renderConfetti();
    }}
  </script>
</body>
</html>
'''

# Write to index.html
with open(r'c:\Users\rickj\.cache\LEUKQUANT_INVITE\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Write to invitation.html
with open(r'c:\Users\rickj\.cache\LEUKQUANT_INVITE\invitation.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: Wrote index.html and invitation.html!")
