# import time
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser

from configuration import config_stt, driver_settings
from addons import addons
from loginmode import login, login_menu

ver = "0.01"


def main_menu():
    print(f"*** T H E - W E S T E R v{ver} ***")
    print("1 - Login")
    print("2 - Register")
    print("3 - Settings")
    main_menu_mode = input("Enter number:")
    match main_menu_mode:
        case "1":
            return "login"
        case "2":
            return "register"
        case "3":
            config_stt()
            main_menu()


if __name__ == '__main__':
    mode = main_menu()
    print(mode)
    options = driver_settings()
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    config = ConfigParser()
    config.read('config.ini')
    addons_cfg = config.getboolean('driver', 'addons')
    if addons_cfg:
        addons(driver)
    server_cfg = config.get('game', 'server')
    driver.get(server_cfg)
    if mode == "login":
        username, password = login_menu()
        login(driver, username, password)
    time.sleep(30)
