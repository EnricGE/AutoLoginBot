import logging
import argparse
from config import CONFIGS
from bots.github_bot import GitHubBot
from bots.quotes_bot import QuotesBot

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BOT_CLASSES = {
    "github": GitHubBot,
    "quotes": QuotesBot, 
}

def main(selected_bots, headless):
    for bot_name in selected_bots:
        if bot_name not in CONFIGS:
            logging.error(f"[{bot_name}] ❌ Missing credentials in config.")
            continue
        if bot_name not in BOT_CLASSES:
            logging.error(f"[{bot_name}] ❌ No bot implementation found.")
            continue

        creds = CONFIGS[bot_name]
        if not all(creds.values()):
            logging.error(f"[{bot_name}] ❌ Missing credentials: {creds}")
            continue

        bot_cls = BOT_CLASSES[bot_name]
        bot = bot_cls(site_name=bot_name, headless=headless)
        bot.run(creds["username"], creds["password"], creds["url"], close_browser=CLOSE_BROWSER)


if __name__ == "__main__":
    SELECTED_BOTS = ["github", "quotes"] # github, quotes
    HEADLESS_MODE = False # Set to True for headless mode (no browser UI)
    CLOSE_BROWSER = False # For testing purposes, you can add more bots here

    main(SELECTED_BOTS, HEADLESS_MODE)
