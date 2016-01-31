import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
myname = "yourname@yourcompany.com"
mypass = "yourpassword"

# File output
fo = open("appledev.csv", "wb")

# Code
driver = webdriver.Firefox()
driver.get("http://developer.apple.com")
assert "Apple Developer" in driver.title
elem = driver.find_element_by_class_name("gh-nav-membercenter")
elem.click()
assert "Sign in with your Apple ID - Apple Developer" in driver.title
name = driver.find_element_by_id("accountname")
passwd = driver.find_element_by_id("accountpassword")
signin = driver.find_element_by_id("submitButton2")
name.send_keys(myname)
passwd.send_keys(mypass)
signin.click()
assert "Member Center - Apple Developer" in driver.title
people = driver.find_element_by_id("adpDevli")
people.click()
# I need an assert here
driver.implicitly_wait(10)
links = driver.find_elements_by_id("persondetails")
names = driver.find_elements_by_class_name("x-grid3-col-name")
for n in names:
   print n.text

print len(links)
for l in links:
   print l.get_attribute("href")
   driver.get(l.get_attribute("href"))
   driver.implicitly_wait(10)
   time.sleep(3)
   frm = driver.find_element_by_name("persondetails")
   driver.implicitly_wait(10)
   print frm.get_attribute("action")
   driver.implicitly_wait(10)
   block = frm.find_element_by_class_name("msg")
   driver.implicitly_wait(10)
   anchor = block.find_element_by_tag_name("a")
   driver.implicitly_wait(10)
   email = anchor.get_attribute("href")
   email = email.replace("mailto:", "")
   byid = re.sub("@.+", "", email)
   print email + "," + byid
   fo.write(email + "," + byid + "\n")
driver.close()

# File close
fo.close()
