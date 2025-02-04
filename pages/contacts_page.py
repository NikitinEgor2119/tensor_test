from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time


class SbisContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.tensor_banner = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")
        self.region_selector = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
        self.partners_list_vologda = (By.CSS_SELECTOR, '.sbisru-Contacts-List__col')
        self.partners_list_kamchatka = (By.CSS_SELECTOR, '.sbisru-Contacts-List__item')

    def click_tensor_banner(self):
        banner = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.tensor_banner))
        banner.click()

    def get_current_region(self):
        print(self.driver.find_element(*self.region_selector).text)
        return self.driver.find_element(*self.region_selector).text

    def get_partners_list(self):

        selectors = [
            ".sbisru-Contacts-List__col",
            ".sbisru-Contacts-List__item",
        ]

        for selector in selectors:
            partners_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            if partners_elements:
                break

        if not partners_elements:
            return []

        partners_text = [element.text.strip() for element in partners_elements]
        return partners_text

    def wait_for_partners_update(self, old_partners):

        for _ in range(15):
            new_partners = self.get_partners_list()
            if new_partners != old_partners:
                return

            time.sleep(1)
        raise TimeoutException("Список партнеров не изменился после смены региона.")

    def change_region(self, region_name):
        self.driver.find_element(*self.region_selector).click()

        region_list_locator = (By.CLASS_NAME, "sbis_ru-Region-Panel__list-l")
        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(region_list_locator))

        region_items = self.driver.find_elements(By.CLASS_NAME, "sbis_ru-Region-Panel__item")
        for region in region_items:
            region_text = region.text.strip()

            if region_name in region_text:
                self.driver.execute_script("arguments[0].scrollIntoView();", region)

                try:
                    region.click()
                except:
                    self.driver.execute_script("arguments[0].click();", region)

                time.sleep(2)
                self.driver.find_element(*self.region_selector).click()


                time.sleep(2)
                self.driver.refresh()
                updated_region = self.driver.find_element(*self.region_selector).text
                return
