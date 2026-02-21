const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const SCREENSHOTS_DIR = path.join(__dirname, 'screenshots');

async function checkTables() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  // Login first
  await page.goto('http://localhost:3001', { waitUntil: 'networkidle' });
  await page.locator('input[type="email"]').first().fill('avinash@example.com');
  await page.locator('input[type="password"]').first().fill('Test');
  await page.locator('button[type="submit"]').first().click();
  await page.waitForTimeout(2000);

  // Go directly to lesson 14
  await page.goto('http://localhost:3001/learning/lesson/14', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  // Get full page screenshot at top
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, 'lesson14-full-top.png'), fullPage: false });

  // Check for tables in the DOM
  const tableCount = await page.locator('table').count();
  const codeCount = await page.locator('pre, code').count();
  const preCount = await page.locator('pre').count();

  console.log('Table count:', tableCount);
  console.log('Code block count:', codeCount);
  console.log('Pre count:', preCount);

  // Get the markdown content
  const rawContent = await page.evaluate(() => {
    const els = document.querySelectorAll('[class*="glass-card"] p, [class*="glass-card"] h1, [class*="glass-card"] h2');
    return Array.from(els).slice(0, 5).map(el => el.textContent.trim());
  });
  console.log('Content samples:', rawContent);

  // Check if table is in the DOM at all
  const tableHTML = await page.evaluate(() => {
    const tables = document.querySelectorAll('table');
    return Array.from(tables).map(t => t.outerHTML.slice(0, 200));
  });
  console.log('Tables HTML:', tableHTML);

  // Check code blocks
  const codeHTML = await page.evaluate(() => {
    const pres = document.querySelectorAll('pre');
    return Array.from(pres).slice(0, 3).map(p => ({
      text: p.textContent.slice(0, 100),
      bg: window.getComputedStyle(p).backgroundColor,
      className: p.className
    }));
  });
  console.log('Code blocks:', JSON.stringify(codeHTML, null, 2));

  // Scroll to find tables
  await page.evaluate(() => window.scrollTo(0, 800));
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, 'lesson14-scroll-800.png') });

  await page.evaluate(() => window.scrollTo(0, 1600));
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, 'lesson14-scroll-1600.png') });

  await page.evaluate(() => window.scrollTo(0, 2400));
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, 'lesson14-scroll-2400.png') });

  await page.evaluate(() => window.scrollTo(0, 3200));
  await page.waitForTimeout(1000);
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, 'lesson14-scroll-3200.png') });

  // Check heading styles
  const h1s = await page.evaluate(() => {
    const h1s = document.querySelectorAll('h1');
    return Array.from(h1s).map(h => ({
      text: h.textContent.trim().slice(0, 50),
      fontSize: window.getComputedStyle(h).fontSize,
      fontWeight: window.getComputedStyle(h).fontWeight,
      color: window.getComputedStyle(h).color,
      borderBottom: window.getComputedStyle(h).borderBottomWidth
    }));
  });
  console.log('H1 headings:', JSON.stringify(h1s, null, 2));

  const h2s = await page.evaluate(() => {
    const h2s = document.querySelectorAll('h2');
    return Array.from(h2s).slice(0, 3).map(h => ({
      text: h.textContent.trim().slice(0, 50),
      fontSize: window.getComputedStyle(h).fontSize,
      fontWeight: window.getComputedStyle(h).fontWeight,
      color: window.getComputedStyle(h).color
    }));
  });
  console.log('H2 headings:', JSON.stringify(h2s, null, 2));

  // Check progress bar
  const progressBarInfo = await page.evaluate(() => {
    const fixed = document.querySelector('.fixed');
    const allFixed = document.querySelectorAll('.fixed, [style*="position: fixed"]');
    return {
      firstFixed: fixed ? { className: fixed.className, style: fixed.getAttribute('style') } : null,
      allFixedCount: allFixed.length,
      allFixed: Array.from(allFixed).slice(0, 5).map(el => ({
        tag: el.tagName,
        className: el.className.slice(0, 100),
        style: el.getAttribute('style')
      }))
    };
  });
  console.log('Progress bar / fixed elements:', JSON.stringify(progressBarInfo, null, 2));

  // Check sidebar visibility
  const sidebarInfo = await page.evaluate(() => {
    const aside = document.querySelector('aside');
    const lgCol1 = document.querySelector('.lg\:col-span-1');
    const stickyEl = document.querySelector('.lg\:sticky');
    return {
      hasAside: !!aside,
      hasLgCol1: !!lgCol1,
      hasStickyEl: !!stickyEl,
      lgCol1Content: lgCol1 ? lgCol1.textContent.slice(0, 100) : null,
      stickyElContent: stickyEl ? stickyEl.textContent.slice(0, 100) : null,
      stickyElVisible: stickyEl ? window.getComputedStyle(stickyEl).display : null
    };
  });
  console.log('Sidebar info:', JSON.stringify(sidebarInfo, null, 2));

  await browser.close();
  console.log('Done!');
}

checkTables().catch(console.error);
