import os
import time
from pages.main_page import SbisMainPage
from pages.download_page import SbisDownloadPage


def test_download_sbis_plugin(driver):
    sbis_main_page = SbisMainPage(driver)
    sbis_main_page.open()

    sbis_main_page.go_to_download_page()

    sbis_download_page = SbisDownloadPage(driver)
    sbis_download_page.download_plugin()

    file_path = os.path.expanduser("~/Downloads/sbisplugin-setup-web.exe")
    timeout = 30

    for _ in range(timeout):
        if os.path.exists(file_path):
            break
        time.sleep(1)
    else:
        assert False, "Файл не скачался!"

    file_size = os.path.getsize(file_path) / (1024 * 1024)
    expected_size = 10.42
    assert abs(file_size - expected_size) < 0.1, f"Размер файла {file_size:.2f} МБ не совпадает с ожидаемым " \
                                                 f"{expected_size} МБ"



