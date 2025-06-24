import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bots.base import BaseBot

class QuotesBot(BaseBot):
    def login(self, username: str, password: str, url: str):
        self.driver.get(url)

        try:
            # Fill in login form
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = self.driver.find_element(By.NAME, "password")
            username_field.send_keys(username)
            password_field.send_keys(password)

            # Submit the form
            self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

            # Confirm login
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
            if "Logout" in self.driver.page_source:
                logging.info(f"[Quotes] ✅ Login successful.")
            else:
                logging.warning(f"[Quotes] ❌ Login failed or unclear result.")
                self.take_screenshot("failed")
        except TimeoutException:
            logging.error(f"[Quotes] ❌ Timeout during login.")
            self.take_screenshot("timeout")
