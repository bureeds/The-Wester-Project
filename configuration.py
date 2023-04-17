from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options


def config_stt():
    print('SETTINGS')
    config = ConfigParser()
    config.read('config.ini')
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
        print()
    change = input("1 - Change settings / 2 - Back to main menu")
    if change == "1":
        server_option = input("Enter server link ex. 'https://www.the-west.net/': ")
        world_option = input("Enter world: ")
        headless_option = input("Would you like to run the program headless? (1 - Yes, 2 - No): ")
        addons_option = input("Would you like to install the addons? (1 - Yes, 2 - No): ")
        login_bonus_option = input("[After Login]Check for daily login bonus and collect? (1 - Yes, 2 - No): ")
        email_verification_option = input("[After Login]Check if email is confirmed? (1 - Yes, 2 - No): ")
        announcements_option = input("[After Login]Close announcements ex. nuggets sale (1 - Yes, 2 - No): ")

        if addons_option == "1":
            config['driver']['headless'] = 'true'

        if login_bonus_option == "1":
            config['game']['login_bonus'] = 'true'

        if email_verification_option == "1":
            config['game']['email_verification'] = 'true'

        if announcements_option == "1":
            config['game']['announcements'] = 'true'

        if headless_option == "1":
            config['driver']['addons'] = 'true'

        config.set('game', 'world', world_option)

        config.set('game', 'server', server_option)

        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def driver_settings():
    def headless_mode():
        # Code to run program in headless mode
        print("Running program in headless mode...")
        options.add_argument("--headless=new")

    def install_addon():
        # Code to install addon
        print("Installing addon...")
        options.add_extension('tampermonkey.crx')

    options = Options()
    config = ConfigParser()
    config.read('config.ini')
    headless = config.getboolean('driver', 'headless')
    addons = config.getboolean('driver', 'addons')
    if headless:
        headless_mode()
    if addons:
        install_addon()
    return options
