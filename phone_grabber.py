from selenium import webdriver
from PIL import Image
from io import BytesIO
import base64
import pytesseract
#from time import sleep

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


class Grabber:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe')
        self.navigate()
        self.phone_number = self.get_tel_from_image()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_test_screen.png')

    def navigate(self):
        self.driver.get(self.base_url)
        button = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()
        self.take_screenshot()
        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]')
        image_png = Image.open(BytesIO(base64.b64decode(image.screenshot_as_base64)))
        image_png.save('phone_number.png')

    def get_tel_from_image(self):
        image = Image.open('phone_number.png')
        return pytesseract.image_to_string(image)


#base_url = 'https://www.avito.ru/volgograd/odezhda_obuv_aksessuary/puhovik_elisabetta_franchi_1054095044'
#grabber = Grabber(base_url)
#print("Voula! {}".format(grabber.phone_number))