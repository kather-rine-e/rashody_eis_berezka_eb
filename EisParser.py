import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
#from libs.resoursers import resource_path
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class EisParser(QThread):

    pause_parser = QtCore.pyqtSignal()

    def __init__(self, date_from, date_to, org_creditionals, root_form):
        QThread.__init__(self)
        # self.year = year
        # if f'{month}'.__len__() == 1:
        #     self.month = f'0{month}'
        # else:
        #     self.month = month
        # self.last_day = last_day
        self.date_from = date_from
        self.date_to = date_to
        self.org_creditionals = org_creditionals
        root_form.resume_eis.connect(self.resume)

        self.work = True

    def run(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://zakupki.gov.ru/')
        time.sleep(3)

        try:
            # Выбрать автоматически
            driver.find_element(by=By.XPATH, value='//*[@id="detect-automatically"]').click()
            time.sleep(1)
            # Принять
            driver.find_element(by=By.XPATH, value='//*[@id="modal-region"]/div/div[4]/div/div[2]/div/button').click()
            time.sleep(1)
            # Перейти в раздел закупок
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

            driver.find_element(by=By.XPATH, value='//*[@id="contractDateTag"]/div/div/div/div[1]/input').send_keys(self.date_from)
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='//*[@id="contractDateTag"]/div/div/div/div[2]/input').send_keys(self.date_to)
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='/html/body/div[3]').click()
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='//*[@id="searchOptionsEditContainer"]/div/div[5]/div[1]').click()
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='//*[@id="customerAnchor"]').click()
            time.sleep(1)


            driver.find_element(by=By.XPATH, value='//*[@id="customerInputDialog"]').send_keys(self.org_creditionals)
            time.sleep(5)
            
            self.work = False
            self.pause_parser.emit()

            while self.work is False:
                time.sleep(1)


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

            
    @QtCore.pyqtSlot()
    def resume(self):
        self.work = True