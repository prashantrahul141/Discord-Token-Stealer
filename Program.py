from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from constants import LOGIN_DISCORD_URL, QR_SVG_ELEMENT_SELECTOR, IMAGE_LOCATION


class Program:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def start(self):
        self.driver.get(LOGIN_DISCORD_URL)
        self.getQRCodeElement()

    def getQRCodeElement(self):
        sleep(5)
        self.svg_element = self.driver.find_element(
            By.CSS_SELECTOR, QR_SVG_ELEMENT_SELECTOR)
        self.saveQR()

    def saveQR(self):
        self.svg_element.screenshot(IMAGE_LOCATION)
