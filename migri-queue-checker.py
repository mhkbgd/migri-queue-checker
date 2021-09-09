import time
import smtplib  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Chrome options for hidin UI
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

# URL of website
url = "https://enterfinland.fi/eServices/"
driver.get(url)
 
# Crowling website
startbutton = driver.find_element_by_class_name("t2m-trigger")
startbutton.click()
driver.implicitly_wait(20)
placeinQueueButton = driver.find_element_by_css_selector("[title*='Place in queue']")
placeinQueueButton.click()
driver.implicitly_wait(20) 
text_area = driver.find_element_by_class_name("sc-hzNEM")
text_area.send_keys("<your diary number>") #your diary numebr from Finnish immigratoin office
text_area.submit()
response = driver.find_element_by_class_name("sc-iujRgT")
print(response.text)

# Gmail SMTP server                      
smtpServer='smtp.gmail.com'      
fromAddr='<smtp from address>' # SMTP from address        
toAddr= ['<your email one>', '<your email two>'] # you can add all the emails here where you want to send notifications        
text = response.text
subject = "Migri Queue"
message = 'Subject: {}\n\n{}'.format(subject, text)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("<smtp from address>","<password>") # your login info for smtp server 
server.sendmail(fromAddr, toAddr, message) 
server.quit()
