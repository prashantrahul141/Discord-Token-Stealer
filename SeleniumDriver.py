from logger import logger
try:
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    logger.debug("imported selenium.")
except:
    logger.error("could not import selenium, exiting.")
    exit()

from time import sleep
from constants import LOGIN_DISCORD_URL, QR_ELEMENT_SELECTOR, IMAGE_LOCATION, TOKEN_GRABBER_JS, DISCORD_HOME_TITLE


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

    def waitForScan(self):
        try:
            logger.info("waiting for qr scan.")
            logger.debug("searching for 'check your phone h2 element'")
            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Check your phone!']")))
        except:
            logger.info("could not found element.")
            element = None

        if element:
            logger.info("element found. user scanned qr.")
            return True

        return False

    def waitForLogin(self):
        try:
            logger.info("waiting for login")
            WebDriverWait(self.driver, 30).until(EC.title_contains(title=DISCORD_HOME_TITLE))
            logger.info("detected login.")
            return True

        except:
            logger.info("could not detect login.")
            return False

    def getToken(self):
        logger.info("trying to retrieve token.")
        try:
            logger.info("executing grabber js")
            logger.info("executing token grabber js")
            token = self.driver.execute_script(TOKEN_GRABBER_JS)
            return token
        except:
            logger.info("failed to get token")
            return False
