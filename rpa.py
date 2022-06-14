from mimetypes import init
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

SALES_OPTIONS = Options()
SALES_OPTIONS.add_argument("--start-maximized")

PATH_CHROME = "C:/Users/Svelez/Desktop/rpa/chromedriver.exe"
INIT = webdriver.Chrome(PATH_CHROME,chrome_options=SALES_OPTIONS)


#iniciamos apliacion y esperamos 1 segundos
INIT.get("https://google.com")

time.sleep(1)

search = WebDriverWait(INIT, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))

time.sleep(1)

search.send_keys("python")
search.send_keys(Keys.ENTER)

result = INIT.find_element_by_xpath('/html/body/div[7]/div/div[7]/div[1]/div/div/div/div').text


print(result)