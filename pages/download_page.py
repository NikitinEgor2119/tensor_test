from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisDownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.download_button = (By.XPATH, "//a[@class='sbis_ru-DownloadNew-loadLink__link js-link']")

    def download_plugin(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            download_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.download_button)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", download_btn)
            self.driver.execute_script("arguments[0].click();", download_btn)

        except Exception as e:
            print(f"Ошибка при скачивании плагина: {e}")
            raise
