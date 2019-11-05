from selenium import webdriver
from time import sleep




#browser.get("chrome://settings")
#browser.find_element_by_css_selector(#advanced-settings-expander")
#browser.find_element_by_css_selector()
#browser.find_element_by_css_selector()
#browser.find_element_by_css_selector()
# browser = webdriver.Chrome()
# browser.execute_script("window.confirm = function(msg) { return true; }")
#
# prefs = {"protocol_handler.excluded_schemes":{"afp":True,"data":True,"disk":True,"disks":True,"file":True,"hcp":True,"intent":True, "itms-appss":True, "itms-apps":True,"itms":True,"market":True,"javascript":True,"mailto":True,"ms-help":True,"news":True,"nntp":True,"shell":True,"sip":True,"snews":False,"vbscript":True,"view-source":True,"vnd":{"ms":{"radio":True}}}}
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs",prefs)

options = webdriver.ChromeOptions()

prefs = {"protocol_handler.excluded_schemes":{"mailto": False,"afp":True,"data":True,"disk":True,"disks":True,"file":True,"hcp":True,"intent":True, "itms-appss":True, "itms-apps":True,"itms":True,"market":True,"javascript":True,"mailto":True,"ms-help":True,"news":True,"nntp":True,"shell":True,"sip":True,"snews":False,"vbscript":True,"view-source":True,"vnd":{"ms":{"radio":True}}}}
options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(options=options)




# browser = webdriver.Chrome()

# browser.get("chrome://settings")
# ee = browser.find_element_by_css_selector("#advancedToggle > span")
# ee.click()
# ee = browser.find_element_by_css_selector("#privacyContentSettingsButton")
# ee.click()
# ee = browser.find_element_by_css_selector("#handlers-section input[value=block]")
# ee.click()
# ee = browser.find_element_by_css_selector("#content-settings-overlay-confirm")
# ee.click()





browser.get('https://nyaa.si/?f=0&c=0_0&q=%5BHorribleSubs%5D+Fruits+Basket+720p')
style = """-webkit-tap-highlight-color: rgba(0,0,0,0);
font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
font-size: 14px;
border-spacing: 0;
border-collapse: collapse;
text-align: center;
line-height: 1.42857143;
white-space: nowrap;
box-sizing: border-box;
background-color: transparent;
color: #247fcc;
text-decoration: none;
display: block;"""

xpath = "/html/body/div/div[1]/table/tbody/tr["
xpath2 = "]/td[3]/a[1]"
classname = "success"
count = 25

#elem1 = browser.find_element_by_tag_name(classname)
#elem1 = browser.find_element_by_id("tr")
#elem1 = browser.find_elements_by_xpath(xpath)
#elem1 = browser.find_elements_by_class_name(classname).s;
#elem1 = browser.find_element_by_css_selector("body > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(3) > a:nth-child(2)")

i = 1
for i in range(1, count+1):
    print(i)
    elem1 = browser.find_element_by_xpath(xpath + str(i) + xpath2)
    elem1.click()
    #sleep(5)
    browser.execute_script("window.confirm = function(msg) { return true; }")




#size = elem1.__sizeof__()

#elem1.click()