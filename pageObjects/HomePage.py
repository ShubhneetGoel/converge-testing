from time import sleep

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    def returnEsPageSoup(self):
        self.driver.get("https://glenis.ywamconverge.org/es/")
        sleep(5)
        esPageSource = self.driver.page_source
        esSoup = BeautifulSoup(esPageSource, 'html.parser')
        return esSoup

    def returnEnPageSoup(self):
        self.driver.get("https://glenis.ywamconverge.org/en/")
        sleep(5)
        enPageSource = self.driver.page_source
        enSoup = BeautifulSoup(enPageSource, 'html.parser')
        return enSoup

    def returnInternshipText(self,soup):
        internshipText = soup.body.div.div.li.a.text
        return internshipText

    def returnApplyText(self,soup):
        applyText = soup.body.div.div.li.next_sibling.next_sibling.a.text
        return applyText

    def returnDonateText(self,soup):
        donateText = soup.body.div.div.li.next_sibling.next_sibling.next_sibling.next_sibling.a.text
        return donateText

    def returnLoginText(self,soup):
        loginText = soup.body.div.div.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.a.text
        return loginText