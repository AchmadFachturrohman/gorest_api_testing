import os
import time
from dotenv import set_key, load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_manager import LoginManager

class GoRESTTokenScraper:
    def __init__(self, env_path=".env", dotenv_src=".env"):
        self.env_path = Path(env_path)
        dotenv_full_path = Path(__file__).parent / dotenv_src
        load_dotenv(dotenv_path=dotenv_full_path)
        self.github_email = os.getenv("GITHUB_EMAIL")
        self.github_password = os.getenv("GITHUB_PASSWORD")

    def _setup_driver(self):
        try:
            options = Options()
            options.add_argument("--incognito")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280x1200")
            # optional: options.add_argument("--headless")

            # hindari deteksi automation
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            driver = webdriver.Chrome(options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            return driver
        except Exception as e:
            print("Gagal membuat driver Chrome:", str(e))
            return None

    def _extract_token(self, driver):
        xpath = "//td[@class='user-select-all']"
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        token = driver.find_element(By.XPATH, xpath).text.strip()
        print("Token terambil dari <td>:", token)
        return token

    def fetch_token(self):
        driver = self._setup_driver()
        if driver is None:
            raise Exception("WebDriver tidak berhasil dibuat. Cek konfigurasi ChromeDriver.")
        login = LoginManager(driver, self.github_email, self.github_password)
        
        try:
            login.login_with_github()
        except Exception as e:
            print("Login gagal:", str(e))

            current_url = driver.current_url
            print("URL setelah gagal login:", current_url)

            if "access-tokens" in current_url or "my-account" in current_url:
                print("Redirect langsung ke token page, lanjut scraping...")
            else:
                # driver.save_screenshot("fallback_login_error.png")
                driver.quit()
                raise

        try:
            token = self._extract_token(driver)
        except Exception as e:
            # driver.save_screenshot("token_scrape_error.png")
            driver.quit()
            raise Exception(f"Gagal scraping token: {str(e)}")

        driver.quit()

        if not self.env_path.exists():
            self.env_path.touch()

        set_key(self.env_path, "GOREST_TOKEN", f"Bearer {token}")
        print(f"Token berhasil disimpan: {token}")

        return token
    
class TokenManager:
    def __init__(self, env_path=".env", dotenv_src=".env"):
        self.scraper = GoRESTTokenScraper(env_path=env_path, dotenv_src=dotenv_src)

    def get_token(self):
        return self.scraper.fetch_token()

    def inject_headers(self):
        token = self.get_token()
        return {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }