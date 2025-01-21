
from selenium import webdriver
from LoginPageObject import LoginPage
from selenium.webdriver.common.by import By
class TestLogin:
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.sendUsername("gautam@gmail.com")
        lp.sendPassword("gautam4846")
        lp.buttonclick()
        text = driver.find_element(By.XPATH, "//*[@id='center_column']/h1").text
        assert text == "MY ACCOUNT"