from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

username = "uguraytekn"
password = "P_K:c$N)Cy7vY?X"


class Instagram:
    def __init__(self,username,password):
        # WebDriverManager'ı kullanarak ChromeDriver'ı otomatik yüklemesi için
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.username = username
        self.password = password
        
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        # Email ve şifre alanlarını bekle
        usernameInput = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")))
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        # E-posta ve şifreyi tek tek gir
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        # Şifreyi göndermek için ENTER tuşuna bas
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # Hata olup olmadığını görmek için ekran görüntüsü al
        self.browser.save_screenshot("login_attempt.png")

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")

        # profil butonuna tıkla
        profile_button = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Profile']")))
        profile_button.click()
        
        # takipçiler butonuna tıkla
        followersLink = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='mount_0_0_TW']/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")))
        followersLink.click()
        



    def close(self):
        self.browser.quit()


instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()
instgrm.close()
    