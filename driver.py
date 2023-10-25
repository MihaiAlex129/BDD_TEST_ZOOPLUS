from selenium import webdriver

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def close_pyta(self):
        self.driver.quit()