from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginManager:
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def login_with_github(self):
        wait = WebDriverWait(self.driver, 15)

        self.driver.get("https://gorest.co.in/consumer/login")
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'github')]")))
        self.driver.find_element(By.XPATH, "//a[contains(@href, 'github')]").click()

        current_url = self.driver.current_url
        print("URL setelah klik login GitHub:", current_url)

        if "authorize" in current_url or "callback" in current_url or "my-account" in current_url:
            print("Sudah login atau auto-redirect, skip input form.")
        else:
            wait.until(EC.presence_of_element_located((By.ID, "login_field")))
            email_elem = self.driver.find_element(By.ID, "login_field")
            email_elem.clear()
            email_elem.send_keys(self.email)

            password_elem = self.driver.find_element(By.ID, "password")
            password_elem.clear()
            password_elem.send_keys(self.password)

            # Verifikasi sebelum klik
            assert password_elem.get_attribute("value") == self.password
            assert email_elem.get_attribute("value") == self.email

            time.sleep(1)
            self.driver.find_element(By.NAME, "commit").click()
        
        # Setelah klik tombol login GitHub
        wait.until(EC.presence_of_element_located((By.NAME, "commit")))
        self.driver.find_element(By.NAME, "commit").click()
        # self.driver.save_screenshot("login_page_debug.png")

        # Tambahan pengecekan URL via JavaScript
        js_url = self.driver.execute_script("return window.location.href")
        print("URL dari JS:", js_url)

        for _ in range(20):
            current = self.driver.current_url
            print("URL sekarang:", current)
            if "/my-account" in current:
                break
            time.sleep(1)
        else:
            # self.driver.save_screenshot("error_token_page.png")
            raise Exception("Tidak berhasil redirect ke /my-account.")
        
        current_url = self.driver.execute_script("return window.location.href")
        print("URL dari JS:", current_url)
        
        self.driver.get("https://gorest.co.in/my-account/access-tokens")
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".token-box")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'token-box')]//code")))
        print("URL saat ini:", self.driver.current_url)
        # self.driver.save_screenshot("after_github_login.png")