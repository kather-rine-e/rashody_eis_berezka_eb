import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def eb_parser(date_from, date_to, org):
    service = Service(executable_path="yandexdriver.exe")
    #service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    def click1(xp): # ждем прогрузку нужного элемента и делаем клик
        try:
            WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, xp)))
            driver.find_element(By.XPATH, xp).click()
        except:
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, xp))
            WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, xp)))
            driver.find_element(By.XPATH, xp).click()

    def click2(xp): # то же самое, но через js (не все кликается нормально)
        try:
            WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, xp)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, xp))
        except:
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, xp))
            WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, xp)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, xp))

    driver.get('https://eb.cert.roskazna.ru')
    driver.maximize_window() 
    click1("//li[@title='Избранное']//a[1]")
    # #НСИ
    click1("//span[text()='Подсистема нормативно-справочной информации']")
    click1("(//span[text()='Справочники, реестры, классификаторы'])[2]")
    click1("(//span[text()='Сводный реестр'])[3]")
    click1("(//span[text()='Сводный реестр'])[3]")
    WebDriverWait(driver, 50).until(ec.element_to_be_clickable(driver.find_elements(By.XPATH, "(//span[text()='Сводный реестр'])")[0]))
    driver.find_elements(By.XPATH, "(//span[text()='Сводный реестр'])")[0].click()

    try: 
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@title='Скрыть навигацию']//span").click()
    except: pass
    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.CLASS_NAME, 'undefined')))
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'undefined'))
    try:
        while len(driver.find_elements(By.XPATH, "//button[@class='filter-button filter-plank-cancel-button z-button']")) != 0:
            click1("//button[@class='filter-button filter-plank-cancel-button z-button']")
    except: pass
    time.sleep(3)
    print(driver.find_element(By.CLASS_NAME, 'z-textbox').is_displayed())

    # click1("//img[@title='Видимость фильтров']")
    # time.sleep(1)
    # click1("//img[@title='Видимость фильтров']")
    # time.sleep(1)
    # click1("//img[@title='Видимость фильтров']")
    # time.sleep(1)
    # click1("//img[@title='Видимость фильтров']")

    if driver.find_element(By.CLASS_NAME, 'z-textbox').is_displayed() == False:
        click1("//img[@title='Видимость фильтров']")
        time.sleep(1)
        # click1("//img[@title='Видимость фильтров']")
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//input[@filter-for='ORGINN']"))
    driver.find_element(By.XPATH, "//input[@filter-for='ORGINN']").send_keys(org)
    driver.find_element(By.XPATH, "//input[@filter-for='ORGINN']").send_keys(Keys.ENTER)
    time.sleep(5)
    orgs_found_by_id = driver.find_elements(By.CLASS_NAME, 'z-listitem')
    headers_SR = driver.find_elements(By.CLASS_NAME, 'z-listheader')
    num_column = -1
    code_org = '_____'
    for num, i in enumerate(headers_SR):
        if i.get_attribute('title') == 'Код организации':
            num_column = num+1
    for i in orgs_found_by_id:
        if i.get_attribute('innerText').find('\n4800\n') != -1:
            for numero, j in enumerate(i.find_elements(By.TAG_NAME, 'td')):
                if numero == num_column:
                    code_org = j.get_attribute('innerText')
    print(code_org)
    time.sleep(5)

    driver.get('https://eb.cert.roskazna.ru')
    #начинаем на главной странице ЭБ
    click1("//span[text()='Управление расходами: средства ФБ']")
    click1("(//span[text()='Все сервисы'])[2]")
    click1("(//span[text()='Управление расходами'])[2]")
    click1("(//span[text()='Компонент ведения бюджетных обязательств'])[2]")
    click1("(//span[text()='Сведения о бюджетном обязательстве'])[3]")
    #click1("//span[text()='Все документы (ТОФК)']")
    for i in driver.find_elements(By.XPATH, "//span[text()='Все документы (ТОФК)']"):
        if i.get_attribute('class') == 'ng-binding':
            try:i.click()
            except Exception:print(Exception)

    time.sleep(5)

    # try: driver.find_element(By.XPATH, "//input[@checked='checked']/following-sibling::div[1]").click()
    # except Exception:print(Exception)

    try: 
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@title='Скрыть навигацию']//span").click()
    except: pass
    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.CLASS_NAME, 'undefined')))
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'undefined'))

    for i in driver.find_elements(By.TAG_NAME, "div"):
        #print(i.get_attribute('id'))
        if i.get_attribute('id').find('Checkbox') != -1:
            try:
                i.click()
            except Exception:print(Exception)
            break
    
    # for i in driver.find_elements(By.TAG_NAME, "input"):
    #     print(i.get_attribute('id'))
    #     if i.get_attribute('id').find('Checkbox') != -1:
    #         try:
    #             i.click()
    #         except Exception:print(Exception)

    # for i in driver.find_elements(By.TAG_NAME, "label"):
    #     print(i.get_attribute('class'))
    #     if i.get_attribute('class') == 'z-checkbox-content':
    #         try:
    #             i.click()
    #         except Exception:print(Exception)

    try:
        while len(driver.find_elements(By.XPATH, "//button[@class='filter-button filter-plank-cancel-button z-button']")) != 0:
            click1("//button[@class='filter-button filter-plank-cancel-button z-button']")
    except: pass

    #click1('//*[@title="Сбросить фильтр"]')
    while driver.find_elements(By.CLASS_NAME, 'z-loading-indicator') != []:
        time.sleep(3)

    bo_search = 0
    try:
        date_search = driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]")
        driver.execute_script("arguments[0].scrollIntoView();", date_search)
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]").click()
        driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]").clear()
        bo_search = driver.find_element(By.XPATH, "//input[@filter-for='RB_UNICCODEORG']")
        driver.execute_script("arguments[0].scrollIntoView();", bo_search)
    except Exception as EX:
        print(EX)
        click1("//img[@title='Видимость фильтров']")
        time.sleep(3)
        date_search = driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]")
        driver.execute_script("arguments[0].scrollIntoView();", date_search)
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]").click()
        driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input[1]").clear()
        bo_search = driver.find_element(By.XPATH, "//input[@filter-for='RB_UNICCODEORG']")
        driver.execute_script("arguments[0].scrollIntoView();", bo_search)
    time.sleep(5)
    bo_search.clear()
    bo_search.send_keys(code_org)
    bo_search.send_keys(Keys.ENTER)
    actionChains = ActionChains(driver)
    actionChains.context_click(date_search).perform()
    click1("//span[text()='между']")
    WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, "(//span[@filter-for='IDB_DATECONTRACT']//input)[2]")))
    driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input").clear()
    driver.find_element(By.XPATH, "//span[@filter-for='IDB_DATECONTRACT']//input").send_keys(date_from)
    driver.find_element(By.XPATH, "(//span[@filter-for='IDB_DATECONTRACT']//input)[2]").clear()
    driver.find_element(By.XPATH, "(//span[@filter-for='IDB_DATECONTRACT']//input)[2]").send_keys(date_to)
    driver.find_element(By.XPATH, "(//span[@filter-for='IDB_DATECONTRACT']//input)[2]").send_keys(Keys.ENTER)

    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//button[@title=' Печать списка']//img[1]")))
    print_button = driver.find_element(By.XPATH, "//button[@title=' Печать списка']//img[1]")
    driver.execute_script("arguments[0].scrollIntoView();", print_button)
    print_button.click()

    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//button[text()='OK']")))
    ok_button = driver.find_element(By.XPATH, "//button[text()='OK']")
    driver.execute_script("arguments[0].scrollIntoView();", ok_button)
    ok_button.click()

    try:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//p[text()='Успешно завершена, для просмотра результатов выберите соответствующую строку в \"Диспетчере задач\" либо нажмите на это сообщение']")))
        time.sleep(10)
    except: 
        #//*[@id="d_15327_z9852_Label"]
        #Не удалось выполнить подсчет количества выводимых на печать документов.
        # WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//span[text()='Не удалось выполнить подсчет количества выводимых на печать документов']")))
        pass
        #driver.get('https://eb.cert.roskazna.ru')
        #mb.showerror("Ошибка","Что-то пошло не так при печати")

    driver.get('https://eb.cert.roskazna.ru')
    #начинаем на главной странице ЭБ
    click1("//span[text()='Управление расходами: средства ФБ']")
    click1("(//span[text()='Все сервисы'])[2]")
    click1("(//span[text()='Управление расходами'])[2]")
    click1("(//span[text()='Компонент ведения денежных обязательств'])[2]")
    click1("(//span[text()='Сведения о денежных обязательствах'])[2]")
    # click1("//span[text()='Все документы (ТОФК)'][2]")
    for i in driver.find_elements(By.XPATH, "//span[text()='Все документы (ТОФК)']"):
        if i.get_attribute('class') == 'ng-binding' or i.get_attribute('id').find('Checkbox-real') != -1:
            try:i.click()
            except Exception:print(Exception)

    try: driver.find_element(By.XPATH, "//div[contains(@class,'advcheckbox-default advcheckbox-checked')]").click()
    except Exception:print(Exception)

    try: 
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@title='Скрыть навигацию']//span").click()
    except: pass
    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.CLASS_NAME, 'undefined')))
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'undefined'))

    for i in driver.find_elements(By.TAG_NAME, "div"):
        #print(i.get_attribute('id'))
        if i.get_attribute('id').find('Checkbox') != -1:
            try:
                i.click()
            except Exception:print(Exception)
            break

    try:
        while len(driver.find_elements(By.XPATH, "//button[@class='filter-button filter-plank-cancel-button z-button']")) != 0:
            click1("//button[@class='filter-button filter-plank-cancel-button z-button']")
    except: pass

    #click1('//*[@title="Сбросить фильтр"]')
    while driver.find_elements(By.CLASS_NAME, 'z-loading-indicator') != []:
        time.sleep(3)

    try:
        date_search = driver.find_element(By.XPATH, "//span[@filter-for='RCD_DATECONTRACTCD']//input[1]")
        driver.execute_script("arguments[0].scrollIntoView();", date_search)
        date_search.clear()
        bo_search = driver.find_element(By.XPATH, "//input[@filter-for='RB_CODEGRBS']")
        driver.execute_script("arguments[0].scrollIntoView();", bo_search)
    except Exception as EX:
        print(EX)
        click1("//img[@title='Видимость фильтров']")
        time.sleep(3)
        date_search = driver.find_element(By.XPATH, "//span[@filter-for='RCD_DATECONTRACTCD']//input[1]")
        driver.execute_script("arguments[0].scrollIntoView();", date_search)
        date_search.clear()
        bo_search = driver.find_element(By.XPATH, "//input[@filter-for='RB_CODEGRBS']")
        driver.execute_script("arguments[0].scrollIntoView();", bo_search)
    bo_search.clear()
    bo_search.send_keys('%'+code_org)
    bo_search.send_keys(Keys.ENTER)
    actionChains = ActionChains(driver)
    actionChains.context_click(date_search).perform()
    click1("//span[text()='между']")
    WebDriverWait(driver, 100).until(ec.element_to_be_clickable((By.XPATH, "(//span[@filter-for='RCD_DATECONTRACTCD']//input)[2]")))
    driver.find_element(By.XPATH, "//span[@filter-for='RCD_DATECONTRACTCD']//input").clear()
    driver.find_element(By.XPATH, "//span[@filter-for='RCD_DATECONTRACTCD']//input").send_keys(date_from)
    driver.find_element(By.XPATH, "(//span[@filter-for='RCD_DATECONTRACTCD']//input)[2]").clear()
    driver.find_element(By.XPATH, "(//span[@filter-for='RCD_DATECONTRACTCD']//input)[2]").send_keys(date_to)
    driver.find_element(By.XPATH, "(//span[@filter-for='RCD_DATECONTRACTCD']//input)[2]").send_keys(Keys.ENTER)

    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//button[@title=' Печать списка']//img[1]")))
    print_button = driver.find_element(By.XPATH, "//button[@title=' Печать списка']//img[1]")
    driver.execute_script("arguments[0].scrollIntoView();", print_button)
    print_button.click()

    WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//button[text()='OK']")))
    ok_button = driver.find_element(By.XPATH, "//button[text()='OK']")
    driver.execute_script("arguments[0].scrollIntoView();", ok_button)
    ok_button.click()

    try:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//p[text()='Успешно завершена, для просмотра результатов выберите соответствующую строку в \"Диспетчере задач\" либо нажмите на это сообщение']")))
        time.sleep(10)
    except: 
        pass
        #//*[@id="d_15327_z9852_Label"]
        #Не удалось выполнить подсчет количества выводимых на печать документов.
        #/html/body/div[2]/section/div[2]/div/div[2]/app-frame/div/div/iframe
        # WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.CLASS_NAME, 'undefined')))
        # driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'undefined'))
        # WebDriverWait(driver, 100).until(ec.presence_of_element_located((By.XPATH, "//span[text()='Не удалось выполнить подсчет количества выводимых на печать документов']")))
        # pass
        # driver.get('https://eb.cert.roskazna.ru')
        # mb.showerror("Ошибка","Что-то пошло не так при печати")
    driver.quit

#eb_parser('01.02.2024', '05.02.2024', '7702151927')
