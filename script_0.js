
    // 1. Lenis Smooth Scroll Setup
    let lenis = null;
    const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    try {
      if (!isReducedMotion && typeof Lenis !== 'undefined') {
        lenis = new Lenis({
          duration: 1.2,
          easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
          smoothWheel: true,
          touchMultiplier: 1.6
        });

        function raf(time) {
          lenis.raf(time);
          requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => {
          lenis.raf(time * 1000);
        });
        gsap.ticker.lagSmoothing(0);
      }
    } catch (e) {
      console.warn('Lenis fallback active', e);
    }

    gsap.registerPlugin(ScrollTrigger);

    function smoothScrollTo(target) {
      if (lenis) {
        lenis.scrollTo(target, { duration: 1.2, offset: target === '#invitation' ? 0 : -20 });
      } else {
        const el = document.querySelector(target);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }
    }

    // 2. Ultra-Smooth Fast Loading & Preloader Sequence
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
    });

                // 3. GSAP Master Animations & Royal Envelope Functions
    // 3. GSAP Master Animations & Royal Booklet Functions
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

    // Aliases for backwards compatibility
    function openRoyalEnvelope(auto = false) { openRoyalBooklet(auto); }
    function replayEnvelopeAnimation() { replayBookletAnimation(); }


    
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

      // (C) SECTION 2: OFFICIAL ROYAL BOOKLET SCROLL TRIGGER
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

            // (C2) SECTION 2B: OFFICIAL INAUGURATION SCHEDULE PINNED FULL-SCREEN
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
      });

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

      // (F) FULLSCREEN PINNED COUNTDOWN SCROLL ANIMATION (#countdown)
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

// 4. Live Countdown to September 10, 2026 at 10:30 AM IST
    const targetLaunchDate = new Date('2026-09-10T10:30:00+05:30').getTime();

    function updateCountdown() {
      const now = new Date().getTime();
      const distance = targetLaunchDate - now;

      if (distance <= 0) {
        ['cd-days', 'radar-days'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = '00'; });
        ['cd-hours', 'radar-hours'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = '00'; });
        ['cd-mins', 'radar-mins'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = '00'; });
        ['cd-secs', 'radar-secs'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = '00'; });
        const msg = document.getElementById('countdown-live-msg');
        if (msg) msg.style.display = 'block';
        return;
      }

      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((distance % (1000 * 60)) / 1000);

      const dStr = String(days).padStart(2, '0');
      const hStr = String(hours).padStart(2, '0');
      const mStr = String(mins).padStart(2, '0');
      const sStr = String(secs).padStart(2, '0');

      ['cd-days', 'radar-days'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = dStr; });
      ['cd-hours', 'radar-hours'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = hStr; });
      ['cd-mins', 'radar-mins'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = mStr; });
      ['cd-secs', 'radar-secs'].forEach(id => { const el = document.getElementById(id); if (el) el.innerText = sStr; });
    }
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // 5. Scroll Progress Bar
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      const pBar = document.getElementById('scroll-progress');
      if (pBar) pBar.style.width = scrollPercent + '%';
    });

    // 6. Interactive Features (Confetti, Mascot Cheer)
    function mascotPulse() {
      showToast('⚡ LeukQuant AI Mascot: Ready for Grand Launch!');
      spawnConfettiBurst();
    }

    // 7. Ambient Audio Synthesizer Toggle
    let audioCtx = null;
    let isAudioPlaying = false;
    let audioInterval = null;

    function toggleAudio() {
      const btn = document.getElementById('audio-toggle');
      if (!isAudioPlaying) {
        if (!audioCtx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          audioCtx = new AudioContext();
        }
        if (audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
        isAudioPlaying = true;
        btn.classList.add('playing');
        btn.innerHTML = '🔊';
        showToast('🎵 Launch Ambience Synthesizer Active');
        playHarmonicChime();
        audioInterval = setInterval(playHarmonicChime, 6000);
      } else {
        isAudioPlaying = false;
        btn.classList.remove('playing');
        btn.innerHTML = '🎵';
        if (audioInterval) clearInterval(audioInterval);
        showToast('🔇 Audio Muted');
      }
    }

    function playHarmonicChime() {
      if (!audioCtx || !isAudioPlaying) return;
      const notes = [261.63, 329.63, 392.00, 523.25, 659.25];
      const freq = notes[Math.floor(Math.random() * notes.length)];
      
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      
      gain.gain.setValueAtTime(0.001, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.08, audioCtx.currentTime + 0.4);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 3.0);
      
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      
      osc.start();
      osc.stop(audioCtx.currentTime + 3.2);
    }

    // 8. Calendar, WhatsApp & Link Sharing
    function addToCalendar() {
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
        'DESCRIPTION:Official Grand Launch of LeukQuant - AI-Powered Active Deception & Autonomous Cybersecurity Platform.\nChief Guest: Dr. N. Marie Wilson (Director, JIT).\nSpecial Guest: Soundarraj Kannan (Target Product Security).\nVenue: Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam, Chennai.',
        'LOCATION:Ground Floor Auditorium, Jeppiaar Institute of Technology, Kunnam, Sriperumbudur, Tamil Nadu 631604',
        'STATUS:CONFIRMED',
        'BEGIN:VALARM',
        'TRIGGER:-PT2H',
        'ACTION:DISPLAY',
        'DESCRIPTION:LeukQuant Grand Launch in 2 Hours',
        'END:VALARM',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('

');

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
    });
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute('download', 'LeukQuant_Grand_Launch.ics');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('📅 Calendar Event (.ics) Downloaded!');
      spawnConfettiBurst();
    }

    function shareWhatsapp() {
      const text = encodeURIComponent('Official Invitation: LeukQuant Grand Launch Ceremony 2026 & Live AI Demonstration on Thursday, September 10, 2026 at 10:30 AM IST | Innovation Auditorium, JIT Foundation, Chennai Campus.\n\nChief Guest: Dr. N. Marie Wilson (Director, Jeppiaar Institute of Technology)\nSpecial Guest: Soundarraj Kannan (Director @ KRP Tech Solutions)\n\nView Digital Invitation: ' + window.location.href);
      window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
    }

    function copyInviteLink() {
      navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('🔗 Invite Link Copied to Clipboard!');
      }).catch(() => {
        showToast('🔗 Link: ' + window.location.href);
      });
      spawnConfettiBurst();
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      if (t) {
        t.innerText = msg;
        t.classList.add('show');
        setTimeout(() => t.classList.remove('show'), 3200);
      }
    }

    // 9. Gold Particles Canvas
    (function initGoldParticles() {
      const canvas = document.getElementById('gold-particles-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;
      let isRunning = !isReducedMotion;

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      document.addEventListener('visibilitychange', () => {
        isRunning = !document.hidden && !isReducedMotion;
      });

      const goldParticles = Array.from({ length: 32 }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        radius: Math.random() * 2 + 1,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        alpha: Math.random() * 0.5 + 0.2
      }));

      function render() {
        if (!isRunning) return;
        ctx.clearRect(0, 0, w, h);
        ctx.fillStyle = '#D4AF37';
        goldParticles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.globalAlpha = p.alpha;
          ctx.fill();
        });
        requestAnimationFrame(render);
      }
      if (isRunning) render();
    })();

    // 10. Custom Gold Cursor
    (function initCustomCursor() {
      const cursor = document.getElementById('custom-cursor');
      if (!cursor || window.matchMedia('(pointer: coarse)').matches) return;

      document.addEventListener('mousemove', (e) => {
        cursor.classList.add('active');
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
      });

      document.addEventListener('mouseleave', () => {
        cursor.classList.remove('active');
      });

      const hoverTargets = document.querySelectorAll('a, button, .btn-material-primary, .btn-material-outline, .royal-mascot-float-badge, .royal-wax-seal');
      hoverTargets.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
      });
    })();

    // 11. Blue Ambient Particles Canvas
    (function initParticles() {
      const canvas = document.getElementById('particles-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      const particles = Array.from({ length: 24 }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        radius: Math.random() * 2 + 1,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        alpha: Math.random() * 0.3 + 0.1
      }));

      function render() {
        ctx.clearRect(0, 0, w, h);
        ctx.fillStyle = '#0066FF';
        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.globalAlpha = p.alpha;
          ctx.fill();
        });
        requestAnimationFrame(render);
      }
      render();
    })();

    // 12. Confetti Burst Function
    function spawnConfettiBurst() {
      const cCanvas = document.getElementById('confetti-canvas');
      if (!cCanvas) return;
      const cCtx = cCanvas.getContext('2d');
      cCanvas.width = window.innerWidth;
      cCanvas.height = window.innerHeight;

      let confettis = [];
      const colors = ['#D4AF37', '#0066FF', '#00B8D9', '#7C3AED', '#10B981', '#FF5A5F', '#F59E0B'];

      for (let i = 0; i < 75; i++) {
        confettis.push({
          x: cCanvas.width / 2,
          y: cCanvas.height * 0.45,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.8) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rot: Math.random() * 360,
          vrot: (Math.random() - 0.5) * 12,
          alpha: 1
        });
      }

      function renderConfetti() {
        cCtx.clearRect(0, 0, cCanvas.width, cCanvas.height);
        let active = false;
        confettis.forEach(c => {
          c.x += c.vx;
          c.y += c.vy;
          c.vy += 0.38;
          c.rot += c.vrot;
          c.alpha -= 0.016;
          if (c.alpha > 0) {
            active = true;
            cCtx.save();
            cCtx.translate(c.x, c.y);
            cCtx.rotate((c.rot * Math.PI) / 180);
            cCtx.fillStyle = c.color;
            cCtx.globalAlpha = Math.max(0, c.alpha);
            cCtx.fillRect(-c.size/2, -c.size/2, c.size, c.size * 0.65);
            cCtx.restore();
          }
        });

        if (active) {
          requestAnimationFrame(renderConfetti);
        } else {
          cCtx.clearRect(0, 0, cCanvas.width, cCanvas.height);
        }
      }
      renderConfetti();
    }

    window.addEventListener('orientationchange', () => {
      setTimeout(() => ScrollTrigger.refresh(), 200);
    });
  