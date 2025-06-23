# parsers/hackernews.py

from bs4 import BeautifulSoup
from utils.limiter import get_limiter
from utils.ban_detector import is_banned
from utils.user_agent import get_random_user_agent
from urllib.parse import urlparse
from playwright.async_api import async_playwright
import asyncio

async def scrape_hackernews(urls: list, download_images=False):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=get_random_user_agent())
        page = await context.new_page()

        for url in urls:
            domain = urlparse(url).netloc
            limiter = get_limiter(domain)
            async with limiter:
                response = await page.goto(url)
                content = await page.content()
                status = response.status if response else 0

                if is_banned(content, status):
                    results.append({"url": url, "error": "Banned or blocked"})
                    continue

                soup = BeautifulSoup(content, "html.parser")

                title = soup.find("title").get_text(strip=True) if soup.find("title") else "N/A"
                points = soup.select_one(".score")
                author = soup.select_one(".hnuser")
                comments = soup.select(".subtext a")[-1] if soup.select(".subtext a") else None

                results.append({
                    "url": url,
                    "title": title,
                    "points": points.get_text(strip=True) if points else "N/A",
                    "author": author.get_text(strip=True) if author else "N/A",
                    "comments": comments.get_text(strip=True) if comments else "N/A"
                })

        await browser.close()
        return results
