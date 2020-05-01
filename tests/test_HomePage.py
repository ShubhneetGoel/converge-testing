import pytest
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
from pageObjects.HomePage import HomePage

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_HomePage(self):
        log = self.get_logger()
        HPage = HomePage(self.driver)
        enSoup = HPage.returnEnPageSoup()
        esSoup = HPage.returnEsPageSoup()
        log.info(HPage.returnInternshipText(enSoup))
        log.info(HPage.returnInternshipText(esSoup))
        assert HPage.returnInternshipText(enSoup) !=  HPage.returnInternshipText(esSoup)
        assert HPage.returnApplyText(enSoup) !=  HPage.returnApplyText(esSoup)
        assert HPage.returnDonateText(enSoup) != HPage.returnDonateText(esSoup)
        assert HPage.returnLoginText(enSoup) != HPage.returnLoginText(esSoup)