import string
import colors as Colors
import time
import random
import randominfo
from random_username.generate import generate_username
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from configparser import ConfigParser


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def register_menu():
    print("1 - Register new account")
    print("2 - Register new demo account")
    register_option = input()
    match register_option:
        case "1":
            username = input("Enter nickname: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            print("Save account?")
            print("1 - Yes")
            print("2 - No")
            save_acc = input()
            if save_acc == "1":
                with open('accounts.txt', 'a') as file:
                    file.write(f'{username},{password},{email} \n')
            return username, password, email
        case "2":
            username = generate_username(1)
            password = randominfo.random_password(length=12, special_chars=False, digits=True)
            email = (random_char(7) + "@gmail.com")
            return username, password, email


def register(driver, username, password, email):
    print(f'{Colors.blue}[INFO]{Colors.white}[REGISTER] {Colors.blue}STARTING REGISTRATION{Colors.default}')
    driver.find_element(By.ID, "playForFree").click()
    time.sleep(3)
    login_input = driver.find_element(By.ID, "registUsername")
    login_input.send_keys(username)
    pass_input = driver.find_element(By.ID, "registPassword")
    pass_input.send_keys(password)
    conf_pass_input = driver.find_element(By.ID, "registRepeatPassword")
    conf_pass_input.send_keys(password)
    email_input = driver.find_element(By.ID, "registEmail")
    email_input.send_keys(email)
    driver.find_element(By.ID, "emailsOptin").click()
    driver.find_element(By.ID, "agbAccept").click()
    time.sleep(1)
    driver.find_element(By.ID, "registrationButton").click()
    print(f'{Colors.blue}[INFO]{Colors.white}[REGISTER] {Colors.blue}SELECTING WORLD{Colors.default}')
    config = ConfigParser()
    config.read('config.ini')
    world = config.get('game', 'world')
    time.sleep(2)
    try:
        driver.find_element(By.LINK_TEXT, world).click()
    except NoSuchElementException:
        print("Wrong Login or Password")
        return
    print(f'{Colors.blue}[INFO]{Colors.white}[REGISTER] {Colors.blue}REGISTRATION COMPLETED{Colors.default}')
    print(f'{Colors.blue}[INFO]{Colors.white}[REGISTER] {Colors.blue}LOADING GAME...{Colors.default}')
