from selenium import webdriver
#Use FIREFOX webdriver to auto click on magenet link on Nyaa and download animes on utorrent, profile is needed to avoid the "Launch Application" popup for auto download

firefoxpath = "C:\\Users\\quitl\\Documents\\Selenium\\geckodriver26.exe"
fp = r"C:\Users\quitl\AppData\Roaming\Mozilla\Firefox\Profiles\iqpfoaf3.autoutorrent"
driver = webdriver.Firefox(executable_path=firefoxpath, firefox_profile=fp)

driver.set_page_load_timeout(30)
#websiteurl = input("What is the Nyaa website :")

#################### testing for now

websiteurl = "https://nyaa.si/?f=0&c=0_0&q=%5BHorribleSubs%5D+%5B720p%5D"
######################

driver.get(websiteurl)
# style = """-webkit-tap-highlight-color: rgba(0,0,0,0);
# font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
# font-size: 14px;
# border-spacing: 0;
# border-collapse: collapse;
# text-align: center;
# line-height: 1.42857143;
# white-space: nowrap;
# box-sizing: border-box;
# background-color: transparent;
# color: #247fcc;
# text-decoration: none;
# display: block;"""
xpath = "/html/body/div/div[1]/table/tbody/tr["
xpath2 = "]/td[3]/a[2]"
count = 50
i = 1
for i in range(1, count+1):
    print(i)

    elem1 = driver.find_element_by_xpath(xpath + str(i) + xpath2)
    elem1.click()

    # driver.execute_script("window.confirm = function(msg) { return true; }")
