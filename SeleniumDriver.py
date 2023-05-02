from logger import logger
try:
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    logger.debug("imported selenium.")
except:
    logger.error("could not import selenium, exiting.")
    exit()

from time import sleep
from constants import LOGIN_DISCORD_URL, QR_ELEMENT_SELECTOR, IMAGE_LOCATION


class SeleniumDriver:
    def __init__(self):
        pass

    def start(self):
        logger.debug("Starting firefox.")
        try:
            self.driver = webdriver.Firefox()
        except:
            logger.error("could not start firefox, exiting.")
            exit()
        logger.debug("opening discord log in page.")
        self.driver.get(LOGIN_DISCORD_URL)
        self.getQRCodeElementAndSave()

    def getQRCodeElementAndSave(self, screenshotPath: str = IMAGE_LOCATION) -> bool:
        logger.info("sleeping 5 seconds for qr image to load.")
        sleep(5)
        logger.debug("searching qr html element")
        try:
            self.qr_element = self.driver.find_element(
                By.CSS_SELECTOR, QR_ELEMENT_SELECTOR)
            logger.info("found qr element")
        except:
            logger.error("could not find qr html element on the page, exiting.")
            exit()

        logger.info("saving qr element as png")
        try:
            result = self.qr_element.screenshot(screenshotPath)
            logger.info(f"saved qr element as png at '{screenshotPath}'")
            return result
        except:
            logger.error("could not save image, exiting.")
            exit()
