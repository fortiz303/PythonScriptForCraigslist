from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t

desc = '''Hello!

Want your own place without roommates at a roommate cost in the heart of the city? If so, I am renting a tiny house on my property. I have hot water hooked up as well as an Incinolet toilet that incinerates waste. This is perfect for a single person as the space is too small for a couple. Perfectly situated in North Denver, 10 minutes away from downtown Denver, 3 minutes away from Regis University. There is a private entrance and street parking.

I will be asking for proof of income or proof of funds (if student). First month and deposit needed at signing.

Please send a short message telling me a little about you (email or text is fine). Thanks for your time!'''

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://denver.craigslist.org")
t.sleep(2)
driver.find_element_by_id('post').click()
t.sleep(1)
driver.find_element(By.XPATH, '//aside[@id=\'loginWidget\']//a').click()
t.sleep(3)
driver.find_element(By.XPATH, '//div[@class=\'accountform-field\']//input').send_keys('francisco_ortiz1@yahoo.com')
t.sleep(3)
with open('/craigslist_bot/password.txt', 'r') as pass_file:
    password = pass_file.readline()
    driver.find_element(By.XPATH, '//input[@type=\'password\']').send_keys(password)
    t.sleep(3)
#    driver.find_element(By.XPATH, '//button[@id=\'login\']').click()
#t.sleep(1)
driver.find_element(By.XPATH, '/html[1]/body[1]/article[1]/section[1]/form[1]/ul[1]/li[4]/label[1]/span[1]/input[1]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@value=\'1\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@id=\'PostingTitle\']').send_keys('Unique Tiny House for rent!')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@id=\'geographic_area\']').send_keys('Denver')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@id=\'postal_code\']').send_keys('80221')
t.sleep(1)
driver.find_element(By.XPATH, '//textarea[@id=\'PostingBody\']').send_keys(desc)
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'price\']').send_keys('750')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'surface_area\']').clear()
t.sleep(0.3)
driver.find_element(By.XPATH, '//input[@name=\'surface_area\']').send_keys('96')
t.sleep(1)
driver.find_element(By.XPATH, '(//span[@class=\'ui-icon ui-icon-triangle-1-s\'])[2]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//li[text()=\'no laundry on site\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//span[@id=\'ui-id-3-button\']/span[1]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//li[text()=\'street parking\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//span[@id=\'ui-id-4-button\']/span[1]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//li[text()=\'1\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//span[@id=\'ui-id-5-button\']/span[1]').click()
t.sleep(1)
driver.find_element(By.XPATH, '(//li[text()=\'1\'])[2]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@placeholder=\'select date\']').send_keys('Mon, 1 Feb 2021')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'show_phone_ok\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'contact_phone_ok\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'contact_text_ok\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'contact_phone\']').send_keys('3032190856')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'contact_name\']').send_keys('Francisco')
t.sleep(1)
driver.find_element(By.XPATH, '//button[@name=\'go\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '(//form[@method=\'post\']//button)[2]').click()
t.sleep(1)
try:
    driver.find_element(By.XPATH, '//a[@class=\'newupl\']').click()
except:
    pass
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'file\']').send_keys('/craigslist_bot/image3.jpg')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'file\']').send_keys('/craigslist_bot/image3.jpg')
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name=\'file\']').send_keys('/craigslist_bot/image3.jpg')
t.sleep(1)
driver.find_element(By.XPATH, '//button[@class=\'done bigbutton\']').click()
t.sleep(1)
driver.find_element(By.XPATH, '(//form[@method=\'post\']//button)[2]').click()
