from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import SbisMainPage
from pages.contacts_page import SbisContactsPage


def test_first(driver):
    main_page = SbisMainPage(driver)
    main_page.open()

    main_page.go_to_contacts()

    contacts_page = SbisContactsPage(driver)
    contacts_page.click_tensor_banner()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    assert "tensor.ru" in driver.current_url, f"Ожидали 'tensor.ru', но получили {driver.current_url}"
