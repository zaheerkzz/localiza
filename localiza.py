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


class Hermes:
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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath))).click()

    def get_page_source(self):
        # try:
        tv_Url = 'https://www.localiza.com/brasil/pt-br'
        self.driver.get(tv_Url)

        time.sleep(5)

        # FROM SET
        # select from enter button
        self.btn_clicks('//*[@id="mat-input-1"]')
        # # enter origin in text field
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys("brasil")
        # # select first in search
        try:
            self.btn_clicks('//*[@id="cdk-overlay-9"]/div/div[1]/ds-place-select-list/div/ul/li[2]')
        except:
            self.btn_clicks('//*[@id="cdk-overlay-0"]/div/div[1]/ds-place-select-list/div/ul/li[2]')

        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cdk-overlay-1"]'))):
            # select date
            date_element = self.driver.find_elements(By.CLASS_NAME, 'mat-calendar-body-cell mat-focus-indicator ng-star-inserted')
            for el in date_element:
                el_ = el.get_attribute('innerHTML')
                print(el_)
                if el_ == '23':
                    el.click()
                    

        # 'mat-calendar-body-cell-content'

        # # DESTINATION SET
        # # select going to button
        # WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[1]/div[1]/button'))).click()
        # # enter destination
        # self.driver.find_element_by_id("location-field-leg1-destination").send_keys(DESTINATION_CODE)
        # time.sleep(3)
        # # enter first in search
        # WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[2]/div[2]/ul/li[1]'))).click()

        # # SET DATE

        # date_click = ActionChains(self.driver)
        # # print('click search... :D')
        # date_click.click(
        #     self.driver.find_element_by_xpath('//*[@id="d1-btn"]')).perform()
        # time.sleep(1)
        # date_element = self.driver.find_elements_by_class_name('mat-calendar-table')
        # for el in date_element:
        #     el_ = el.get_attribute('innerHTML')
        #     # try:
        #     # btn_date = el_.split('aria-label="')[1].split('"')[0].replace(', date disabled', '')
        #     # btn_date = btn_date.replace('selected, current check in date.', '')
        #     # btn_date_ = el_.text

        #     # time.sleep(0.1)
        #     cr_date = datetime.strptime(flight_date, '%Y-%m-%d')
        #     today_date = str(cr_date.strftime("%b %d, %Y"))
        #     print("Expedia_date:  " + today_date)
        #     if today_date[4] == '0':
        #         i = 4
        #         today_date = today_date[:i] + today_date[i + 1:]

        #     if today_date in el_:
        #         # print("today_date : " + str(today_date))
        #         el.click()
        #         time.sleep(1)
        #         self.driver.find_element_by_xpath(
        #             '//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
        #         break
        #     # except IndexError as ex:
        #     #     pass

        # # SEARCH BUTTON
        # # click on search button
        # search_click = ActionChains(self.driver)
        # # print('click search... :D')
        # search_click.click(
        #     # self.driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div/button')).perform()
        #     self.driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[4]/div/button')).perform()
        # time.sleep(1)
        # self.press_button()
        # self.driver.quit()
        # data_ = str(self.all_data_expedia).replace("'{", '{').replace("}'", '}').replace('type_', 'type')
        # return data_
        # # except Exception as ex:
        # #     print(f"exception in expedia... {ex}")
        # #     pass
        # #     return '[]'


if __name__ == '__main__':

   h = Hermes()
   h.get_page_source()
