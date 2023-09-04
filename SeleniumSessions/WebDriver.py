import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Firefoxservice
from selenium.webdriver.edge.service import Service as Edgeservice
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#os.environ['PATH'] += r'C:\Users\abc\Desktop\Rome\Driver\chrome-win32\chrome.exe'
#Auto browser check/install
browsername = 'firefox'

if browsername == 'chrome':
    driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
elif browsername == 'firefox':
    driver = webdriver.Firefox(service=Firefoxservice(GeckoDriverManager().install()))
elif browsername == 'edge':
    driver = webdriver.Edge(service=Edgeservice(EdgeChromiumDriverManager().install()))
else:
    print('Pass correct browsername'+browsername)

driver.implicitly_wait(5)
driver.get('https://scribie.com/account/sign-in')
driver.find_element(By.ID, 'signinSrEmail').send_keys('fridakimani56@gmail.com')
driver.find_element(By.ID, 'signinSrPassword').send_keys('frida@123')

driver.implicitly_wait(100)