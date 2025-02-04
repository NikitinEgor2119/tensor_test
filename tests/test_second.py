from pages.contacts_page import SbisContactsPage
from pages.main_page import SbisMainPage


def test_second_scenario(driver):
    main_page = SbisMainPage(driver)
    contacts_page = SbisContactsPage(driver)

    main_page.open()
    main_page.go_to_contacts()

    initial_region = contacts_page.get_current_region()
    assert "Вологодская" in initial_region, f"Ожидали 'Вологодская', получили '{initial_region}'"

    initial_partners = contacts_page.get_partners_list()
    contacts_page.change_region("41 Камчатский край")

    contacts_page.wait_for_partners_update(initial_partners)

    new_region = contacts_page.get_current_region()
    assert "Камчатский" in new_region, f"Ожидали 'Камчатский', получили '{new_region}'"

    new_partners = contacts_page.get_partners_list()

    assert len(new_partners) > 0, "Новый список партнеров пуст!"
    assert set(initial_partners) != set(new_partners), " Список партнеров не изменился!"

    assert "Камчатский край" in driver.title, f"Title не содержит 'Камчатский край'! Полученный Title: {driver.title}"
    assert "41-kamchatskij-kraj" in driver.current_url, f"URL не содержит '41-kamchatskij-kraj'! Полученный URL: " \
                                                        f"{driver.current_url}"

