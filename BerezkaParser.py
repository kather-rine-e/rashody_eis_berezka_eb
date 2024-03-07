import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
#from libs.resoursers import resource_path
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BerezkParsers(QThread):

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
        root_form.resume_berezka.connect(self.resume)

        self.work = True


    def run(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://agregatoreat.ru/')
        time.sleep(3)

        try:
            driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/app-menu/div[2]').click()
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/app-menu/div[2]/div[2]/p-panelmenu/div/div[4]/div[1]/a/span[2]').click()
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='/html/body/app-root/div/div/app-menu/div[2]/div[2]/p-panelmenu/div/div[4]/div[2]/div/p-panelmenusub/ul/li[1]/a').click()
            time.sleep(3)
            
            driver.find_element(by=By.XPATH, value='//*[@id="filterField-7-dateRange-from"]').send_keys(self.date_from)
            time.sleep(1)
            driver.find_element(by=By.XPATH, value='//*[@id="filterField-7-dateRange-to"]').send_keys(self.date_to)
            time.sleep(1)

            driver.find_element(by=By.XPATH, value='//*[@id="filterField-14-autocomplete"]').send_keys(self.org_creditionals)
            time.sleep(3)

            self.work = False
            self.pause_parser.emit()

            while self.work is False:
                time.sleep(1)

            driver.find_element(by=By.XPATH, value='//*[@id="applyFilterButton"]').click()
            time.sleep(3)

            driver.find_element(by=By.XPATH, value='//*[@id="exportButton"]').click()
            time.sleep(3)

            driver.close()

        except Exception as ex:
            print(ex)
            driver.close()

    @QtCore.pyqtSlot()
    def resume(self):
        self.work = True

#//*[@id="filter_sidebar"]/form/app-filter-field[14]/div/div/p-autocomplete/span/div