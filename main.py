from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 1000
PROMISED_UP = 1000

CHROME_DRIVE_PATH = "/Applications/Development/chromedriver"
# service = Service(CHROME_DRIVE_PATH)
# driver = webdriver.Chrome(service=service)

TWITTER_EMAIL = "" #your email
TWITTER_PASSWORD = "" #Your pass
TWITTER_MSG = "                                                 "
INTERNET_PROV = '' #your internet provider

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVE_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()

        time.sleep(8)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(60)

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div').text
        # print(self.up)
        # print(self.down)

        time.sleep(5)

    def tweet_at_provider(self):
        time.sleep(5)
        self.driver.get('https://twitter.com/')

        time.sleep(5)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]')
        login_button.click()

# My internet speed is DOWNLOAD Mbps
        # 556.22 UP, UPLOAD Mbps
        # 495.18 DOWN, instead of 1000 UP, 1000.
        # @DigiRomania
        #  is awesome!

        time.sleep(5)

        not_now = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]')
        not_now.click()

        time.sleep(5)

        email_field = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        email_field.send_keys(TWITTER_EMAIL)

        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()

        # time.sleep()

        # username = self.driver.find_element(By.XPATH, '')

        time.sleep(5)
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(8)
        TWITTER_MSG = f'My internet speed is {self.up}, {self.down}, instead of {PROMISED_UP} UP, {PROMISED_DOWN} DOWN. {INTERNET_PROV} is awesome!'
        tweet_msg = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        tweet_msg.click()
        tweet_msg.send_keys(TWITTER_MSG)

        time.sleep(5)

        posting = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        posting.click()

        time.sleep(6)





bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()




