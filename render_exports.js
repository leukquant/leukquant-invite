const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

async function render() {
  const htmlPath = path.resolve(__dirname, 'invitation.html');
  const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');

  const browserPath = fs.existsSync('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
    ? 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    : 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

  console.log('Using browser:', browserPath);

  // 1. Export 2x PNG (2160 x 3072)
  {
    const browser = await puppeteer.launch({
      executablePath: browserPath,
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=max']
    });
    const page = await browser.newPage();
    await page.setViewport({
      width: 1080,
      height: 1536,
      deviceScaleFactor: 2
    });

    await page.goto(fileUrl, { waitUntil: 'networkidle0' });
    await page.evaluateHandle('document.fonts.ready');
    // slight delay for rendering
    await new Promise(r => setTimeout(r, 800));

    const card = await page.$('#card');
    const pngPath = path.resolve(__dirname, 'invitation_2x.png');
    await card.screenshot({
      path: pngPath,
      type: 'png'
    });
    console.log('Exported 2x PNG:', pngPath);
    await browser.close();
  }

  // 2. Export 1x JPG (1080 x 1536, < 300KB)
  {
    const browser = await puppeteer.launch({
      executablePath: browserPath,
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setViewport({
      width: 1080,
      height: 1536,
      deviceScaleFactor: 1
    });

    await page.goto(fileUrl, { waitUntil: 'networkidle0' });
    await page.evaluateHandle('document.fonts.ready');
    await new Promise(r => setTimeout(r, 800));

    const card = await page.$('#card');
    const jpgPath = path.resolve(__dirname, 'invitation.jpg');
    await card.screenshot({
      path: jpgPath,
      type: 'jpeg',
      quality: 88
    });

    const stats = fs.statSync(jpgPath);
    console.log('Exported JPG:', jpgPath, `(${Math.round(stats.size / 1024)} KB)`);
    await browser.close();
  }
}

render().catch(err => {
  console.error(err);
  process.exit(1);
});
