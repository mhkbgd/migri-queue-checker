import time
import smtplib  
from selenium import webdriver
from twilio.rest import Client 
from webdriver_manager.chrome import ChromeDriverManager

# Chrome options for now showing UI
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
 
# Crowling info from Migri
startbutton = driver.find_element_by_class_name("t2m-trigger")
startbutton.click()
driver.implicitly_wait(20)
placeinQueueButton = driver.find_element_by_css_selector("[title*='Place in queue']")
placeinQueueButton.click()
driver.implicitly_wait(20) 
text_area = driver.find_element_by_class_name("sc-hzNEM")
text_area.send_keys("4377/110/2021")
text_area.submit()
response = driver.find_element_by_class_name("sc-iujRgT")
print(response.text)

# Twilio SMS API, add you sid and token from Twillo trail account
account_sid = '<SID>' 
auth_token = '<Toke>' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                               messaging_service_sid='<SID>',
                              body="Hi, RP Application status:"+response.text,      
                              to='+358-XXXXXXX' #your mobile numebr where you want to send notificaiton
                          ) 

print(message.sid)

