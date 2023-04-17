import colors as Colors
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from configparser import ConfigParser


def login_menu():
    print("1 - Saved accounts")
    print("2 - Login new account")
    login_option = input()
    match login_option:
        case "1":
            print("Saved accounts:")
            with open('accounts.txt', 'r') as file:
                lines = file.readlines()
                counter = 1
                for line in lines:
                    username, password, email = line.strip().split(',')
                    print(f'{counter} - {username}')
                    counter += 1
            print("---------------")
            line_number = input("Enter number:")
            with open('accounts.txt', 'r') as file:
                lines = file.readlines()
                if 1 <= int(line_number) <= len(lines):
                    username, password, email = lines[int(line_number) - 1].strip().split(',')
                    print(f'Login: {username}')
                    print(f'Password: {password}')
            return username, password
        case "2":
            username = input("Enter login: ")
            password = input("Enter password: ")

            print("Want to save account?")
            print("1 - Yes")
            print("2 - No")

            save_acc = input()
            if save_acc == "1":
                email = "ExistedAccount"
                with open('accounts.txt', 'a') as file:
                    file.write(f'{username}, {password}, {email} \n')

            return username, password


def login(driver, username, password):
    print(f'{Colors.blue}[INFO]{Colors.white}[LOGIN] {Colors.blue}STARTING LOGIN PROCES{Colors.default}')
    login_input = driver.find_element(By.NAME, "username")
    login_input.send_keys(username)
    pass_input = driver.find_element(By.NAME, "userpassword")
    pass_input.send_keys(password)
    driver.find_element(By.ID, "loginButton").click()
    print(f'{Colors.blue}[INFO]{Colors.white}[LOGIN] {Colors.blue}SELECTING WORLD{Colors.default}')
    config = ConfigParser()
    config.read('config.ini')
    world = config.get('game', 'world')
    time.sleep(2)
    try:
        driver.find_element(By.LINK_TEXT, world).click()
    except NoSuchElementException:
        print("Wrong Login or Password")
        return
    print(f'{Colors.blue}[INFO]{Colors.white}[LOGIN] {Colors.blue}LOGIN SUCCESSFUL{Colors.default}')
    print(f'{Colors.blue}[INFO]{Colors.white}[LOGIN] {Colors.blue}LOADING GAME...{Colors.default}')
