PASSWORD = "#pandian01"


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time


SIMILAR_ACCOUNT = "sh18iva"
USERNAME = "_barkfortreats"


class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        
    def login(self):
        self.user_id = self.driver.find_element(by= By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.user_password = self.driver.find_element(by= By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.log_in =  self.driver.find_element(by= By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        self.user_id.send_keys(USERNAME)
        self.user_password.send_keys(PASSWORD)
        self.log_in.click()
        time.sleep(2)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(2)
        #account you want there followers
        self.account = self.driver.get(url= f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")  
        time.sleep(8.2)
        # The xpath of the modal will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


#the bot can't click the followers button there is an issue in this code
 