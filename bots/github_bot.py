import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bots.base import BaseBot

class GitHubBot(BaseBot):
    def login(self, username: str, password: str, url: str):
        self.driver.get(url)

        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "login")))
            password_field = self.driver.find_element(By.NAME, "password")
            username_field.send_keys(username)
            password_field.send_keys(password)
            self.driver.find_element(By.NAME, "commit").click()

            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            if "Sign out" in self.driver.page_source or "Your profile" in self.driver.page_source:
                logging.info(f"[GitHub] ✅ Login successful.")
            else:
                logging.warning(f"[GitHub] ❌ Login failed or unclear result.")
                self.take_screenshot("failed")
        except TimeoutException:
            logging.error(f"[GitHub] ❌ Timeout during login.")
            self.take_screenshot("timeout")
