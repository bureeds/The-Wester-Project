import colors as Colors
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configparser import ConfigParser


def after_login_check(driver):
    def daily_rewards():
        print(f'{Colors.blue}[INFO]{Colors.white}[DAILY REWARDS] {Colors.blue}CHECKING DAILY REWARDS{Colors.default}')
        try:
            collect_btn = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'collect-btn'))
            )
        except TimeoutException:
            print(
                f'{Colors.blue}[INFO]{Colors.white}[DAILY REWARDS]'
                f' {Colors.blue}NO DAILY REWARDS - SKIPPING{Colors.default}')
            return

        print(
            f'{Colors.blue}[INFO]{Colors.white}[DAILY REWARDS]'
            f' {Colors.blue}REWARDS AVAILABLE - COLLECTING{Colors.default}')
        collect_btn.click()

        try:
            reward_btn = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'quest_reward_button'))
            )
        except TimeoutException:
            print(f'{Colors.orange}[WARNING] CANT READ REWARD VALUE{Colors.default}')
            return

        reward_exp = driver.find_element(By.XPATH, '/html/body/div[10]/div[3]/div/span/p').text
        time.sleep(1)
        reward_btn.click()
        print(f'{Colors.blue}[INFO]{Colors.white}[DAILY REWARDS] {Colors.blue}DAILY REWARDS CHECK COMPLETED'
              f' - COLLECTED REWARDS:{Colors.green}[{reward_exp} exp/bonds/nuggets]{Colors.default}')

    def email_validation():
        print(f'{Colors.blue}[INFO]{Colors.white}[EMAIL] {Colors.blue}CHECKING EMAIL VALIDATION{Colors.default}')
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, 'ui_email_validation')))
        except TimeoutException:
            print(f'{Colors.blue}[INFO]{Colors.white}[EMAIL] {Colors.blue}EMAIL VALIDATED{Colors.default}')
            return
        print(f'{Colors.orange}[WARNING] EMAIL NOT VALIDATED{Colors.default}')

    def announcement():
        print(f'{Colors.blue}[INFO]{Colors.white}[ANNOUNCEMENT] {Colors.blue}CHECKING...{Colors.default}')
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_tab_id_announcements')))
        except TimeoutException:
            print(f'{Colors.blue}[INFO]{Colors.white}[ANNOUNCEMENT] {Colors.blue}NO FOUND{Colors.default}')
            return
        print(f'{Colors.blue}[INFO]{Colors.white}[ANNOUNCEMENT] {Colors.blue}FOUND{Colors.default}')
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="windows"]/div[2]/div[12]/div[1]/div[2]/div')))
        except TimeoutException:
            driver.find_element(By.XPATH, '//*[@id="windows"]/div[2]/div[16]/div[4]').click()
            print(
                f'{Colors.blue}[INFO]{Colors.white}[ANNOUNCEMENT]'
                f' {Colors.blue}NUGGETS SALE INFO CLOSED{Colors.default}')
            return
        driver.find_element(By.XPATH, '//*[@id="windows"]/div[2]/div[12]/div[1]/div[2]/div').click()
        print(
            f'{Colors.blue}[INFO]{Colors.white}[ANNOUNCEMENT] {Colors.blue}ANNOUNCEMENT MARKED AS READ{Colors.default}')
    config = ConfigParser()
    config.read('config.ini')
    daily = config.getboolean('game', 'login_bonus')
    email = config.getboolean('game', 'email_verification')
    announcements = config.getboolean('game', 'announcements')
    if daily:
        daily_rewards()
    if email:
        email_validation()
    if announcements:
        announcement()
