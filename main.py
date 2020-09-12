# Global Libraries
import random
import time
from selenium import webdriver

# Chrome Libraries
from selenium.webdriver.chrome.options import Options

# Firefox Libraries
from selenium.webdriver.firefox.options import Options as foptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities
#Selenium Libraries
from selenium.webdriver.common.keys import Keys                         
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class pokebot:
    
    def __init__(self, url):
        self.url = 'https://www.pokemoncenter.com/product/290-80319/pokemon-tcg-shining-legends-elite-trainer-box'

    def rand_proxy(self):
        #rand = random.randint(1, 514)
        lines = open('./proxies.txt').read().splitlines()
        line = random.choice(lines)
        line = line.rstrip()
        print(line)
        return line

    def rand_user(self):
        lines = open('./user_agents.txt').read().splitlines()
        line = random.choice(lines)
        line = line.rstrip()
        print(line)
        return line
    
    def return_length(self):
        return random.randint(0, 2000)
    
    def return_width(self):
        return random.randint(0, 2000)

    def create_headless_chrome (self):
        try:
            chrome_options = Options()
            
            # chrome_options.add_experimental_option("excludeSwitches", ["test-type"])
            chrome_options.arguments[:] = []
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--enable-automation")
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
            # chrome_options.add_argument("--headless")
            chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            chrome_options.add_argument('--proxy-server=%s' % self.rand_proxy()+":8080")
            chrome_options.add_argument('user-agent=%s' % self.rand_user())
            chrome_options.add_argument("disable-infobars")
            driver = webdriver.Chrome(executable_path = './chromedriver-new' , options = chrome_options)
            driver.set_page_load_timeout(10)
            driver.maximize_window()
            driver.get('https://www.google.com/')
            print('Header Created')
            driver.get(self.url)
            time.sleep(20)
            # driver.close()
            #return driver
        except Exception as e:
            # driver.quit()
            print('create Headless')
            print(str(e))


    def create_headless_firefox(self):
        try:
            proxy = self.rand_proxy() + ":8080"
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            # firefox_capabilities['proxy'] = {
            #     "proxyType": "MANUAL",
            #     "httpProxy": proxy,
            #     "ftpProxy": proxy,
            #     "sslProxy": proxy
            # }
            driver = webdriver.Firefox(executable_path= './geckodriver', capabilities=firefox_capabilities)
            driver.get('https://www.adidas.com/us/pulseboost-hd-summer.rdy-shoes/EF0702.html')
            search_form = driver.find_element_by_name('q')
            driver.find_element_by_name('q').send_keys('pokemon center')
            driver.find_element_by_name('q').send_keys(Keys.ENTER)
            time.sleep(9 )
            driver.get(self.url)


        except Exception as e:
            print('create Headless')
            print(str(e))

    def switch(self, driver):
        new_uri = driver.window_handles[0]
        print(new_uri)
        return driver.switch_to.window(new_uri)




if __name__ == "__main__":
    p = pokebot('https://www.pokemoncenter.com/product/290-80319/pokemon-tcg-shining-legends-elite-trainer-box')
    # driver = p.create_headless_chrome()
    driver = p.create_headless_firefox()



