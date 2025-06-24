import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

class BaseBot:
    def __init__(self, site_name: str, headless: bool = True):
        self.site_name = site_name
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        try:
            self.driver = webdriver.Chrome(options=options)
        except WebDriverException as e:
            logging.error(f"[{site_name}] ❌ WebDriver failed to start: {e}")
            raise
        self.wait = WebDriverWait(self.driver, 10)

    def run(self, username: str, password: str, url: str, close_browser: bool = True):
        try:
            logging.info(f"[{self.site_name}] Logging in at {url}")
            self.login(username, password, url)
        except Exception as e:
            logging.exception(f"[{self.site_name}] ❌ Error during login: {e}")
            self.take_screenshot("error")
        finally:
            logging.debug(f"[{self.site_name}] close_browser={close_browser}")
            if close_browser:
                self.driver.quit()
            else:
                logging.info(f"[{self.site_name}] Browser left open for inspection.")
                input("🧪 Press ENTER to close the browser...")
                self.driver.quit()  # Optional, in case you want to clean up after inspection

    def take_screenshot(self, reason: str):
        ts = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{self.site_name}_{reason}_{ts}.png"
        path = os.path.join("screenshots", filename)
        os.makedirs("screenshots", exist_ok=True)
        try:
            self.driver.save_screenshot(path)
            logging.info(f"[{self.site_name}] 📸 Screenshot saved to {path}")
        except Exception as e:
            logging.warning(f"[{self.site_name}] Could not save screenshot: {e}")

    def login(self, username: str, password: str, url: str):
        raise NotImplementedError("Each bot must implement its own login method.")
