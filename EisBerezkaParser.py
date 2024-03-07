import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
import undetected_chromedriver as uc 
from seleniumbase import Driver
import requests
from requests.auth import HTTPBasicAuth
import json

def Parser(date_from, date_to, org):
    #service = Service(executable_path="chromedriver.exe")
    #service = Service(executable_path="yandexdriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\ufk\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # ua = UserAgent()
    # user_agent = ua.random
    # #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    # print(user_agent)
    # options.add_argument(f'--user-agent={user_agent}')

    #driver = webdriver.Chrome(options=options)
    #driver = Driver(uc=True)
    driver = uc.Chrome(driver_executable_path=r'chromedriver.exe')
    list_out = False

    #driver.set_window_size(1020,945)
    driver.set_window_size(945,1020)

    #driver1.quit
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get('https://agregatoreat.ru/purchases-registry/all')
    time.sleep(15)

    driver.find_element(by=By.XPATH, value='//*[@id="filterField-7-dateRange-from"]').send_keys(date_from)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="filterField-7-dateRange-to"]').send_keys(date_to)
    time.sleep(1)

    inn_input = driver.find_element(by=By.XPATH, value='//*[@id="filterField-13-autocomplete"]')
    driver.execute_script("arguments[0].scrollIntoView();", inn_input)
    driver.find_element(by=By.XPATH, value='//*[@id="filterField-13-autocomplete"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="filterField-13-autocomplete"]').send_keys(org)
    list_out = True
    time.sleep(5)

    while list_out == True:
        time.sleep(3)
        #ng-trigger ng-trigger-overlayAnimation ng-tns-c99-14 p-autocomplete-panel p-component ng-star-inserted
        if  driver.find_elements(By.CLASS_NAME, 'p-autocomplete-panel') == []:
            list_out = False

    driver.find_element(by=By.XPATH, value='//*[@id="exportButton"]').click()
    time.sleep(3)

# # #     url = "https://tender-cache-api.agregatoreat.ru/api/TradeRegistry/list-trade-lots"
# # #     apiuser = 'user'
# # #     apipass = 'userpass'
# # #     headers = {
# # #         "Accept": "application/json, text/plain, */*",
# # #         "Accept-Encoding": "gzip, deflate, br",
# # #         "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
# # #         "Authorization": "Bearer null",
# # #         "Cache-Control": "no-cache",
# # #         "Connection": "keep-alive",
# # #         "Content-Length": "730",
# # #         "Content-Type": "application/json",
# # #         "Host": "tender-cache-api.agregatoreat.ru",
# # #         "Origin":"https://agregatoreat.ru",
# # #         "Pragma": "no-cache",
# # #         "Referer": "https://agregatoreat.ru/",
# # #         "Sec-Fetch-Dest": "empty",
# # #         "Sec-Fetch-Mode": "cors",
# # #         "Sec-Fetch-Site": "same-site",
# # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
# # #         'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
# # #         "sec-ch-ua-mobile": "?0",
# # #         'sec-ch-ua-platform': '"Windows"',
# # #         "sec-fetch-dest": "empty",
# # #         "sec-fetch-mode": "cors",
# # #         "sec-fetch-site": "same-site",
# # #         'Accept-Encoding':'gzip, deflate, br',
# # #         'Content-Length': '730',
# # #         'Host': 'tender-cache-api.agregatoreat.ru',
# # #   }
# # #     # data = {
# # #     #         "referrer": "https://agregatoreat.ru/",
# # #     #         "referrerPolicy": "strict-origin-when-cross-origin",
# # #     #         "body": "{\"page\":1,\"size\":10,\"searchText\":null,\"purchaseNumber\":null,\"ktruCodes\":[],\"customerNameOrInn\":null,\"customerInn\":null,\"customerKpp\":null,\"customerId\":null,\"supplierNameOrInn\":null,\"supplierInn\":null,\"supplierKpp\":null,\"supplierId\":null,\"purchaseTypeIds\":[],\"types\":[],\"purchaseMethods\":[],\"executionDateStart\":null,\"executionDateEnd\":null,\"dateAddedStart\":null,\"dateAddedEnd\":null,\"webEatCode\":null,\"isContractSignedWithDelay\":false,\"isContractCompletedWithDelay\":false,\"isNoFailedPurchase\":false,\"isPriceExcess\":false,\"customerContractNumber\":null,\"isSpecificSupplier\":null,\"isRussianItemsPurchase\":null,\"lotStates\":[],\"tradeRegistryEatEnum\":0,\"organizerRegions\":[],\"sort\":[{\"fieldName\":\"contractConclusionDate\",\"direction\":2}]}",
# # #     #         "method": "POST",
# # #     #         "mode": "cors",
# # #     #         "credentials": "include"
# # #     # }
# # #     json_data = {
# # #         'page': 1,
# # #         'size': 10000,
# # #         'searchText': None,
# # #         'purchaseNumber': None,
# # #         'ktruCodes': [],
# # #         'customerNameOrInn': None,
# # #         'customerInn': '7702151927',
# # #         'customerKpp': None,
# # #         'customerId': None,
# # #         'supplierNameOrInn': None,
# # #         'supplierInn': None,
# # #         'supplierKpp': None,
# # #         'supplierId': None,
# # #         'purchaseTypeIds': [],
# # #         'types': [],
# # #         'purchaseMethods': [],
# # #         'executionDateStart': None,
# # #         'executionDateEnd': None,
# # #         'dateAddedStart': "2024-02-01",
# # #         'dateAddedEnd': "2024-02-21",
# # #         'webEatCode': None,
# # #         'isContractSignedWithDelay': False,
# # #         'isContractCompletedWithDelay': False,
# # #         'isNoFailedPurchase': False,
# # #         'isPriceExcess': False,
# # #         'customerContractNumber': None,
# # #         'isSpecificSupplier': None,
# # #         'isRussianItemsPurchase': None,
# # #         'lotStates': [],
# # #         'tradeRegistryEatEnum': 0,
# # #         'organizerRegions': [],
# # #         'sort': [
# # #             {
# # #                 'fieldName': 'contractConclusionDate',
# # #                 'direction': 2,
# # #             },
# # #         ],
# # #     }

# # #     response = requests.post(url=url, headers=headers, json=json_data, auth=HTTPBasicAuth(apiuser, apipass))

# # #     if response.ok:
# # #         json_data = response.json()
# # #         print("ZXC\n", response)
# # #         for num, item in enumerate(response.json()['items']):
# # #             # for i, j in enumerate(response.json()['items'][num]):
# # #             #     print(i, ' - ', j, ' - ', response.json()['items'][num][j])
# # #             print(response.json()['items'][num]['contractConclusionDate'], ' ', response.json()['items'][num]['tradeNumber'], ' ', response.json()['items'][num]['totalPrice'], ' ', response.json()['items'][num]['organizerInfo']['fullName'])
# # #     else:
# # #         print("Ошибка HTTP ZXC:", response.status_code)

    driver.get('https://zakupki.gov.ru/')
    time.sleep(3)

    try:
        # Перейти в раздел закупок
        time.sleep(3)
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="modal-region"]/div/div[4]/div/div[2]/div/button').click()
            time.sleep(1)
        except: pass
        
        driver.find_element(by=By.XPATH, value='/html/body/header[3]/div/div/div/ul/ul/li[3]/a').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='/html/body/header[3]/div/div/div/ul/ul/li[3]/ul/li/ul/li[1]/a').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="quickSearchForm_header"]/section[2]/div/div/div[2]/div[2]/div[1]/div/div/a').click()
        time.sleep(2)

        driver.find_element(by=By.XPATH, value='//*[@id="searchOptionsEditContainer"]/div/div[7]/div[1]').click()
        time.sleep(1)

        dates = driver.find_element(by=By.XPATH, value='//*[@id="contractDateTag"]/div/div/button').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="calendarDays"]/div[1]/button[2]').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="contractDateTag"]/div/div/div/div[1]/input').send_keys(date_from)
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="contractDateTag"]/div/div/div/div[2]/input').send_keys(date_to)
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='/html/body/div[3]').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="searchOptionsEditContainer"]/div/div[5]/div[1]').click()
        time.sleep(1)

        driver.find_element(by=By.XPATH, value='//*[@id="customerAnchor"]').click()
        time.sleep(5)


        driver.find_element(by=By.XPATH, value='//*[@id="customerInputDialog"]').send_keys(org)
        list_out = True
        time.sleep(3)

        while list_out == True:
            time.sleep(3)
            # if  driver.find_elements(By.CLASS_NAME, 'choiceTableSelectedRow') == []:
            #     list_out = False
            # if  driver.find_elements(By.CLASS_NAME, 'p-autocomplete-panel') == []:
            #     print(driver.find_elements(By.CLASS_NAME, 'p-autocomplete-panel') == [])
            #     list_out = False
            #ng-trigger ng-trigger-overlayAnimation ng-tns-c99-20 p-autocomplete-panel p-component ng-star-inserted
            # if driver.find_elements(By.XPATH, '/html/body/app-root/div/main/app-purchases-registry/app-registry-page-layout/div[2]/div[2]/div/div[1]/app-filter/section/form/app-filter-field[14]/div/div/p-autocomplete/span/div') == []:
            #     list_out = False
            if driver.find_elements(By.CLASS_NAME, 'choiceTableSelectedRow') != []:
                list_out = False


        driver.find_element(by=By.XPATH, value='//*[@id="modal-customer"]/div/div[4]/div/div/button[2]').click()
        time.sleep(3)

        driver.find_element(by=By.XPATH, value='//*[@id="btn-floating"]/button').click()
        time.sleep(3)
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="quickSearchForm_header"]/section[2]/div/div/div[1]/div[2]/div[1]/div[2]/a[2]').click()
            time.sleep(3)
        
            driver.find_element(by=By.XPATH, value='//*[@id="mCSB_2_container"]/ul/li/span/span[1]').click()
            time.sleep(3)

            driver.find_element(by=By.XPATH, value='//*[@id="modal-load-properties"]/div/div[4]/div/div/button[2]').click()
            time.sleep(3)

            for but in driver.find_elements(by=By.XPATH, value="//div[@class='col-3 link csvDownload cursorPointer']"):
                but.click()
                time.sleep(3)

            driver.close()
            
        except:
            driver.close()

    except Exception as ex:
        print(ex)
        driver.close()

#Parser('12.02.2024', '18.02.2024', '7702151927')