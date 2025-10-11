import type { APIRoute } from 'astro';
import puppeteer from 'puppeteer';

export const prerender = false;

export const GET: APIRoute = async ({ site }) => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();
    
    // Use the site URL or fallback to localhost for development
    const baseUrl = site?.toString() || 'http://localhost:4321';
    await page.goto(`${baseUrl}/cv-print`, {
      waitUntil: 'networkidle0'
    });

    const pdf = await page.pdf({
      format: 'A4',
      printBackground: true,
      margin: {
        top: '1.5cm',
        right: '1.5cm',
        bottom: '1.5cm',
        left: '1.5cm'
      }
    });

    await browser.close();

    return new Response(pdf, {
      status: 200,
      headers: {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'attachment; filename="Firdaus_Nuur_Rhamadhan_CV.pdf"'
      }
    });
  } catch (error) {
    await browser.close();
    return new Response(JSON.stringify({ error: 'Failed to generate PDF' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json'
      }
    });
  }
};
