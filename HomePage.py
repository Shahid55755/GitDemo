from selenium.webdriver.common.by import By


class HomePage:
    def __def__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[normalize-space()='Shop'])[1]")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def printing(self):
        print("using page Object project maxremind guy")

    def printings(self):
        print("using page Object project maxremind guy")
