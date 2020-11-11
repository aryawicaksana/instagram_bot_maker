from time import sleep
from selenium import webdriver
import names
import clipboard
import random
from selenium.webdriver.support.ui import Select
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@$"
num = "123456789"
for p in range(1):
    password = ''
    for c in range(8):
        password += random.choice(chars)
browser = webdriver.Chrome("./chromedriver")
browser.implicitly_wait(5)
mail ='https://generator.email/'
browser.get(mail)
emailgen = browser.find_element_by_id("copbtn")
emailgen.click()
name = names.get_full_name()
email_str = clipboard.paste()
print(email_str,name,password)
browser.execute_script("window.open()")
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.instagram.com/')
sleep(5)
browser.refresh()
login_link = browser.find_element_by_link_text("Sign up")
login_link.click()
emailorphone = browser.find_element_by_name('emailOrPhone')
f_name = browser.find_element_by_name('fullName')
pass_word = browser.find_element_by_name('password')

emailorphone.send_keys(email_str)
f_name.send_keys(name)
pass_word.send_keys(password)
sleep(2)
username = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button')
username.click()
signup = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')
signup.click()
month = Select(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select') )
month.select_by_index(random.choice(num))
days = Select (browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
days.select_by_index(random.choice(num))
year = Select (browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select') )
year.select_by_value('1998')
next = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
next.click()
browser.switch_to.window(browser.window_handles[0])
sleep(25)
code = browser.find_element_by_css_selector('#email-table > div.e7m.list-group-item.list-group-item-info > div.e7m.subj_div_45g45gg')
fixcode = code.text.split()
print(fixcode[0])
browser.switch_to.window(browser.window_handles[1])
enter_code = browser.find_element_by_name('email_confirmation_code')
enter_code.send_keys(fixcode[0])
verify = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
verify.click()
