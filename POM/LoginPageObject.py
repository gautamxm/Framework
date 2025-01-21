
from selenium.webdriver.common.by import By

class LoginPage:
    emailID = "email"
    psswdID = "passwd"
    btnsignID = "SubmitLogin"

    # constructors
    def __init__(self,driver):
        self.driver = driver

    #Actions
    def sendUsername(self,username):
        usertext = self.driver.find_element(By.ID,self.emailID)
        usertext.send_keys(username)

    def sendPassword(self,password):
        usertext = self.driver.find_element(By.ID,self.psswdID)
        usertext.send_keys(password)

    def buttonclick(self):
        btn = self.driver.find_element(By.ID,self.btnsignID)
        btn.click()