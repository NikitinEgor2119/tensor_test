from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"
        self.contacts_link = (By.LINK_TEXT, "Контакты")

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def go_to_contacts(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.contacts_link)
        ).click()

    def go_to_download_page(self):
        download_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Скачать локальные версии"))
        )
        download_link.click()