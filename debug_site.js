const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log(`[CONSOLE] ${msg.type()}: ${msg.text()}`));
  page.on('pageerror', error => console.log(`[ERROR] ${error.message}`));
  
  const fileUrl = 'file://' + path.resolve('index.html');
  console.log('Navigating to', fileUrl);
  await page.goto(fileUrl);
  
  // Wait a bit for JS to execute
  await page.waitForTimeout(2000);
  
  await browser.close();
})();
