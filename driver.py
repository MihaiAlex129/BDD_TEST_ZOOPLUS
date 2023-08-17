from selenium import webdriver


class Driver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def close_pyta(self):
        self.driver.quit()
