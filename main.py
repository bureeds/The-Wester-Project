# import time
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser

from configuration import config_stt, driver_settings
from addons import addons
from loginmode import login, login_menu
from registermode import register, register_menu
from afterlogin import after_login_check
from inventory import equipment
from tutorial import tutorial
from character_data import data
ver = "0.01"


def main_menu():
    print(f"*** T H E - W E S T E R - v{ver} ***")
    print("1 - Login")
    print("2 - Register")
    print("3 - Settings")
    main_menu_mode = input("Enter number: ")
    match main_menu_mode:
        case "1":
            return "login"
        case "2":
            return "register"
        case "3":
            config_stt()
            main_menu()


def game_menu():
    data(driver)
    print("*** MENU ***")
    print("1 - Inventory")
    print("2 - Auto Tutorial")
    game_menu_mode = input("Enter number: ")
    match game_menu_mode:
        case "1":
            equipment(driver)
            game_menu()
        case "2":
            tutorial(driver, username)
            game_menu()


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
        after_login_check(driver)
    else:
        username, password, email = register_menu()
        register(driver, username, password, email)
    game_menu()
    print("END")
    time.sleep(30)
