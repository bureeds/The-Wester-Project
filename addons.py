import colors as Colors
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def addons(driver):
    print(f'{Colors.blue}[INFO]{Colors.white}[DRIVERS] {Colors.blue}DRIVERS INSTALLATION COMPLETE{Colors.default}')
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.blue}INSTALLING ADDONS...{Colors.default}')
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.yellow}DOBBY 0%{Colors.default}')
    driver.get("https://greasyfork.org/pl/scripts/444958-dobby2")
    wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    driver.close()
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.yellow}DOBBY 25%{Colors.default}')
    driver.switch_to.window(original_window)
    install_btn_site = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'install-link'))
    )
    install_btn_site.click()
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.yellow}DOBBY 50%{Colors.default}')
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.yellow}DOBBY 75%{Colors.default}')
    install_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'install'))
    )
    install_btn.click()
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.yellow}DOBBY 100%{Colors.default}')
    driver.switch_to.window(original_window)
    print(f'{Colors.blue}[INFO]{Colors.white}[ADDONS] {Colors.blue}ADDONS INSTALLATION COMPLETE{Colors.default}')