# selenium imports
from selenium import webdriver
# from seleniumwire import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions

# BS4 import
from bs4 import BeautifulSoup as Soup
import time
import jsons
import csv

from datetime import datetime

# selenium setings
class Arguments:
    DRIVER_PATH = 'driver/chromedriver'

    options = ChromeOptions()
    # headless is set TRUE, it will stop browser from opening
    # selenium settings
    options.headless = False 
    options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--lang=en_US')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--enable-features=NetworkService,NetworkServiceInProcess')
    options.add_argument('--force-color-profile=srgb')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # disable all the options listed, for fast run
    prefs = {'profile.managed_default_content_settings': {
                                                          'images': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                          'notifications': 2, 'auto_select_certificate': 2,
                                                          'fullscreen': 2, 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                          'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                                          'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                          'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                          'metro_switch_to_desktop': 2,
                                                          'protected_media_identifier': 2, 'app_banner': 2,
                                                          'site_engagement': 2,
                                                          'durable_storage': 2
                                                          }
             }
    options.add_experimental_option('prefs', prefs)


class Localiza:
    origin = 'brasilia'
    destination = ''
    date_ = ''
    date2_ = ''
    time_1 = ''
    time_2 = ''

    domain = 'https://www.hermes.com'

    # change your category URL here...
    categoryURL = f"https://www.hermes.com/hk/en/category/women/shoes/"

    def __init__(self):
        arguments = Arguments()
        self.driver = webdriver.Chrome(options=arguments.options, executable_path=arguments.DRIVER_PATH)

    def btn_clicks(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, xpath))).click()
        except:
            time.sleep(2)
            try:
                WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, xpath))).click()
            except:
                pass
    
    def select_date(self, top_id):
        # select date
        try:
            if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="{top_id}"]'))):
                date_element = self.driver.find_elements(By.CLASS_NAME, 'mat-calendar-body-cell')
                for el in date_element:
                    el_ = Soup(el.get_attribute('innerHTML'), 'html.parser')
                    if el_.text.strip() == '27':
                        el.click()
        except:
            pass

    def select_time(self, top_id, time_slection):
        try:
            # select time
            if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="{top_id}"]'))):
                time_element = self.driver.find_elements(By.CLASS_NAME, 'mat-focus-indicator')
                for el in time_element:
                    el_ = Soup(el.get_attribute('innerHTML'), 'html.parser')
                    if el_.text.strip() == time_slection:
                        el.click()
        except:
            pass

    def get_page_source(self):
        # try:
        tv_Url = 'https://www.localiza.com/brasil/pt-br'
        self.driver.get(tv_Url)

        time.sleep(5)

        # FROM SET (ORIGIN SELECTION)
        # select from enter button
        self.btn_clicks('//*[@id="mat-input-1"]')
        # # enter origin in text field
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys("brasil")
        # # select first in search
        try:
            self.btn_clicks('//*[@id="cdk-overlay-9"]/div/div[1]/ds-place-select-list/div/ul/li[2]')
        except:
            self.btn_clicks('//*[@id="cdk-overlay-0"]/div/div[1]/ds-place-select-list/div/ul/li[2]')
        # select origin date
        self.select_date('cdk-overlay-1')
        #select origin time
        self.select_time('mat-select-0-panel', '19:30')

        # DROP SET (DESTINATION SELECTION)
        
        # select destination date
        self.select_date('cdk-overlay-3')
        # # select destination time
        self.select_time('cdk-overlay-4', '22:00')

        time.sleep(5)
        # select from enter button
        self.btn_clicks('//*[@id="mat-input-3"]')

        # enter destination in text field
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-3"]').send_keys("brasil")
        # select first in search
        try:
            self.btn_clicks('//*[@id="cdk-overlay-4"]/div/div[1]/ds-place-select-list/div/ul/li[2]')
        except:
            self.btn_clicks('//*[@id="cdk-overlay-5"]/div/div[1]/ds-place-select-list/div/ul/li[2]')

        time.sleep(5)
        ## CLICK search button
        try:
            self.btn_clicks('/html/body/app-root/app-header/header/div/app-topbar-first-step/div/div/div/div/div[2]/div[5]/ds-button/button')  
            time.sleep(3)
            self.parse_page()
        except:
            print('except btn')
            self.btn_clicks('//*[@class="ds-button ds-button--primary"]')
            time.sleep(3)
            self.parse_page()

    def parse_page(self):

        time.sleep(15)
        parsed_data = Soup(self.driver.page_source, 'html.parser')
        cars = parsed_data.find('ds-car-group-offers-list')
        for car in cars.findAll('section', class_='list-card ng-star-inserted'):
            car_name = car.find('div', class_='ds-car-group-text__group-name').text.strip()
            car_image = car.find('img', class_='car-group-carousel__image ng-star-inserted')['src']
            car_details = car.fin('img', class_='ds-car-group-text__model-name').text
            offer_list = car.find('ds-offer-list')
            print(len(offer_list.findAll('button')) )
            if len(offer_list.findAll('button')) > 1:
                promo_offer = offer_list.findAll('button')[0]
                promo_price = promo_offer.find('p', class_='tarifas__preco').text

                standard_offer = offer_list.findAll('button')[0]
                standard_price = standard_offer.find('p', class_='tarifas__preco').text
                print(promo_price)
                print(standard_price)

            print(car_name)
            print(car_image)
            print(car_details)

        # filename = 'localiza.csv'
        # header = ['name', 'address', 'price']
        # data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

        # with open(filename, 'w', newline="") as file:
        #     csvwriter = csv.writer(file) # 2. create a csvwriter object
        #     csvwriter.writerow(header) # 4. write the header
        #     csvwriter.writerows(data) # 5. write the rest of the data



if __name__ == '__main__':

   h = Localiza()
   h.get_page_source()
