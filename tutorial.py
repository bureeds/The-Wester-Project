from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import colors as Colors
import time

from configparser import ConfigParser


def tutorial(driver, username):
    config = ConfigParser()
    config.read('config.ini')
    server = config.get('game', 'server')
    a = None
    if server == "https://www.the-west.net/":
        a = 7
        server = "NET"
    if server == "https://www.the-west.pl/":
        a = 8
        server = "PL"

    total_steps = 64

    for step in range(1, total_steps + 1):
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' TUTORIAL START')
        step += 1
        im_ready = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[10]/div/div[4]/div[1]'))
        )
        time.sleep(1)
        driver.execute_script("arguments[0].click();", im_ready)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' RANDOMIZE AVATAR')
        step += 1
        random_dice = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'randomize'))
        )
        random_dice.click()
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CONFIRM AVATAR')
        step += 1
        accept_avatar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[3]/div[12]/div[3]/div[13]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_avatar)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT TUTORIAL')
        step += 1
        accept_tut = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_tut)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' DUEL BEN')
        step += 1
        duell_ben = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", duell_ben)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE DUEL WINDOW')
        step += 1
        duell_ben_close = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[3]/div[16]/div[4]'))
        )
        driver.execute_script("arguments[0].click();", duell_ben_close)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT TUTORIAL STEP')
        step += 1
        next_tut = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_tut)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT BANDIT QUEST')
        step += 1
        accept_bandit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_bandit)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' OPEN DUEL TAB')
        step += 1
        duels = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[6]/div[3]/div/div[4]'))
        )
        driver.execute_script("arguments[0].click();", duels)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' DUEL FIRST BANDIT')
        step += 1
        duel_first = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[3]/div[12]/div[1]/div[1]/div[1]/div[1]/div[2]'))
        )
        driver.execute_script("arguments[0].click();", duel_first)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE DUEL RAPORT')
        step += 1
        exit_bandit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[2]/div[16]/div[4]'))
        )
        driver.execute_script("arguments[0].click();", exit_bandit)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH DUEL QUEST')
        step += 1
        finish_bandit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_1"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finish_bandit)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT TUTORIAL STEP - SKILLS')
        step += 1
        next_tut_skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_1"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_tut_skills)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT SKILLS QUEST')
        step += 1
        accept_tut_skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_2"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_tut_skills)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' OPEN SKILL TAB ')
        step += 1
        skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//*[@id="ui_character_container"]/div[{a}]'))  # net div 7 pl 8
        )
        driver.execute_script("arguments[0].click();", skills)
        time.sleep(2)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ADD SKILPOINT HEALTH')
        step += 1
        add_health = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="pmbut_skill_health"]/span[4]'))
        )
        driver.execute_script("arguments[0].click();", add_health)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CONFIRM SKILLS')
        step += 1
        confirm_skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[2]/div[12]/div[1]/div[1]/div[3]/div[1]'))
        )
        driver.execute_script("arguments[0].click();", confirm_skills)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE SKILLS TAB')
        step += 1
        close_skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[3]/div[16]/div[4]'))
        )
        driver.execute_script("arguments[0].click();", close_skills)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH SKILLS QUEST')
        step += 1
        finish_tut_skills = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_2"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finish_tut_skills)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT TUTORIAL STEP - CHASING BANDITS')
        step += 1
        next_tut_hiv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_2"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_tut_hiv)
        time.sleep(1)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT CHASE QUEST')
        step += 1
        accept_tut_hiv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_3"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_tut_hiv)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOUDS WAIT TIME')
        step += 1
        time.sleep(3)
        time.sleep(3)
        testingone = '"#map > div.image.x-173.y-69.posx-44419.posy-17873.jobgroup.jobgroup-7"'
        testing = '"#map > div.job.job-128.hasMousePopup > img"'
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' OPEN JOB GROUP')
        step += 1
        driver.execute_script(f'document.querySelector({testingone}).click()')
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' SELECT CHASE BANDITS')
        step += 1
        driver.execute_script(f'document.querySelector({testing}).click()')
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' START CHASE BANDITS')
        step += 1
        startpole = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[3]/div[12]/div[3]/div[2]/div[2]/div[1]'))
        )
        driver.execute_script("arguments[0].click();", startpole)
        time.sleep(24)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH CHASE BANDITS QUEST')
        step += 1
        fino_tut_hiv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_3"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", fino_tut_hiv)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT TUTORIAL STEP - LAMBS')
        step += 1
        next_nest = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_3"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_nest)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' START LAMB QUEST')
        step += 1
        start_lamb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_4"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", start_lamb)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' QUENE FIRST LAMB')
        step += 1
        driver.execute_script("JobWindow.startJob(130,44169,17887,15)")
        time.sleep(14)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' QUENE SECOND LAMB')
        step += 1
        driver.execute_script("JobWindow.startJob(130,44169,17887,15)")
        time.sleep(24)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH LAMB QUEST')
        step += 1
        end_lamb = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_4"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", end_lamb)
        time.sleep(13)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT TUTORIAL STEP - STRENGTH')
        step += 1
        strength_js = '"#linear_quest_1_4 > div.linear_quest_footer > div:nth-child(1) > div"'
        driver.execute_script(f'document.querySelector({strength_js}).click()')
        time.sleep(3)
        driver.execute_script(f'document.querySelector({strength_js}).click()')
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT STRENGHT QUEST')
        step += 1
        strong_start = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_5"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", strong_start)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' OPEN SKILLS TAB')
        step += 1
        skills_strong = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//*[@id="ui_character_container"]/div[{a}]'))
        )
        driver.execute_script("arguments[0].click();", skills_strong)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ADD SKILLPOINT TO STRENGHT')
        step += 1
        skills_strong_plus = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="pmbut_attr_strength"]/span[4]'))
        )
        driver.execute_script("arguments[0].click();", skills_strong_plus)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CONFIRM SKILLS')
        step += 1
        confirm_strong = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[2]/div[12]/div[1]/div[1]/div[3]/div[1]'))
        )
        driver.execute_script("arguments[0].click();", confirm_strong)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE SKILL TAB')
        step += 1
        close_skills_strong = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[2]/div[16]/div[4]'))
        )
        driver.execute_script("arguments[0].click();", close_skills_strong)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH STRENGHT QUEST')
        step += 1
        strong_finish = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_5"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", strong_finish)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - FISHING')
        step += 1
        next_astrong = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_5"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_astrong)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT QUEST FISHING')
        step += 1
        start_fishing = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_6"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", start_fishing)
        time.sleep(7)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' QUENE FISHING')
        step += 1
        driver.execute_script("JobWindow.startJob(127,43879,17869,15)")
        time.sleep(24)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH QUEST FISHING')
        step += 1
        finish_fishing = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_6"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finish_fishing)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - HEADGEAR')
        step += 1
        next_afish = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_6"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_afish)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - HEADGEAR SECOND')
        step += 1
        headgear_js = '"#linear_quest_1_6 > div.linear_quest_footer > div:nth-child(1) > div"'
        driver.execute_script(f'document.querySelector({headgear_js}).click()')
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT HEADGEAR QUEST')
        step += 1
        accept_headgear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_7"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", accept_headgear)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH HEADGEAR QUEST')
        step += 1
        finish_headgear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_7"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finish_headgear)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - EQUIP HEADGEAR')
        step += 1
        next_aheadgear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_7"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_aheadgear)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT EQUIP HEADGEAR QUEST')
        step += 1
        acc_equip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_8"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", acc_equip)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' OPEN INVENTORY')
        step += 1
        open_eq = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="ui_bottombar"]/div/div[1]'))
        )
        driver.execute_script("arguments[0].click();", open_eq)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' HEADGEAR SORTING')
        step += 1
        headgear_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[4]/div[12]/div[1]/div[6]'))
        )
        driver.execute_script("arguments[0].click();", headgear_tab)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' EQUIP STARING BANDANA')
        step += 1
        click_on_wraist = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bag"]/div/img'))
        )
        driver.execute_script("arguments[0].click();", click_on_wraist)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE INVENTORY')
        step += 1
        close_eq = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="windows"]/div[3]/div[16]/div[2]'))
        )
        driver.execute_script("arguments[0].click();", close_eq)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH EQUIP HEADGEAR QUEST')
        step += 1
        end_eq_quest = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_8"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", end_eq_quest)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - COFFE')
        step += 1
        next_aeq = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_8"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", next_aeq)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT COFFEE QUEST')
        step += 1
        acc_coffe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_9"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", acc_coffe)
        time.sleep(7)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' QUENE COFFEE')
        step += 1
        driver.execute_script("JobWindow.startJob(129,43638,17956,15)")
        time.sleep(24)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH COFFEE QUEST')
        step += 1
        finnish_coffe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_9"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finnish_coffe)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - ENDING')
        step += 1
        almost_end = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_9"]/div[2]/div[1]/div'))
        )
        time.sleep(3)
        js_route = '"#linear_quest_1_9 > div.linear_quest_footer > div:nth-child(1) > div"'
        driver.execute_script(f'document.querySelector({js_route}).click()')
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - ENDING SECOND')
        step += 1
        driver.execute_script("arguments[0].click();", almost_end)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' ACCEPT BAG QUEST')
        step += 1
        acc_bag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_10"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", acc_bag)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' FINISH BAG QUEST')
        step += 1
        finnish_bag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_10"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", finnish_bag)
        time.sleep(3)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' NEXT STEP - ENDING TUTORIAL')
        step += 1
        nexta_bag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="linear_quest_1_10"]/div[2]/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", nexta_bag)
        time.sleep(10)
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' CLOSE ALERT')
        step += 1
        finish_js = f'"body > div.tw2gui_dialog_framefix > div > div.tw2gui_dialog_content' \
                    f' > div.tw2gui_dialog_text > div > div.button_area > div.tw2gui_button"'
        driver.execute_script(f'document.querySelector({finish_js}).click()')
        percent_complete = (step / total_steps) * 100
        step_notification = f'TutWester: {Colors.magenta} {username} {Colors.default} ({server}) |' \
                            f' {Colors.orange} STEP: {step}/{total_steps} {Colors.default} |' \
                            f' {Colors.orange} {percent_complete:.2f}% {Colors.default} | {Colors.green}'
        print(step_notification + f' TUTORIAL FINISHED')
        step += 1
        time.sleep(3)
        break
