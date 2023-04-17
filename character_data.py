import colors as Colors
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def data(driver):
    try:
        char_name = driver.find_element(By.CLASS_NAME, 'char_name').text
        energy_bar = driver.find_element(By.CLASS_NAME, 'energy_bar').text
        health_bar = driver.find_element(By.CLASS_NAME, 'health_bar').text
        level = driver.find_element(By.CLASS_NAME, 'level').text
        money = driver.find_element(By.ID, 'money').text
        bank = driver.find_element(By.ID, 'deposit').text
        nuggets = driver.find_element(By.ID, 'nuggets').text
        bonds = driver.find_element(By.CLASS_NAME, 'bond_value').text
        server_time = driver.find_element(By.ID, 'servertime').text
    except NoSuchElementException:
        print("Can't collect all data")
        return
    char_data = (f'{Colors.white}[{server_time[13:]}] '
                 f'{Colors.magenta}{char_name}{Colors.default} | {Colors.red}{health_bar}{Colors.default} |'
                 f' {Colors.blue}{energy_bar}{Colors.default} | {Colors.yellow}{level} LVL{Colors.default} |'
                 f' {Colors.orange}{money}${Colors.default} | {Colors.white}{bank}${Colors.default} | '
                 f'{Colors.white}{bonds}/3,000{Colors.default} | {Colors.yellow}{nuggets} nuggets{Colors.default} |')

    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'custom_unit_counter')))
    except TimeoutException:
        print(char_data)
        return
    event = driver.find_element(By.XPATH, '//*[@id="user-interface"]/div[16]/span[1]')
    event_counter = driver.find_element(By.CLASS_NAME, 'custom_unit_counter')
    attribute = event_counter.get_attribute("class")
    classes = attribute.split()
    print(f'{char_data} {Colors.red}{event.text} {classes[1]}{Colors.default} |')
