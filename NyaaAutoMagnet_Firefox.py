from selenium import webdriver
#Use FIREFOX webdriver to auto click on magenet link on Nyaa and download animes on utorrent, profile is needed to avoid the "Launch Application" popup for auto download

firefoxpath = "C:\\Users\\quitl\\Documents\\Selenium\\geckodriver26.exe"
fp = r"C:\Users\quitl\AppData\Roaming\Mozilla\Firefox\Profiles\iqpfoaf3.autoutorrent"
driver = webdriver.Firefox(executable_path=firefoxpath, firefox_profile=fp)
driver.set_page_load_timeout(30)
websiteurl = input("What is the Nyaa website :")
driver.get(websiteurl)

xpath = "/html/body/div/div[1]/table/tbody/tr["
xpath2 = "]/td[3]/a[2]"
count = 50
i = 1
for i in range(1, count+1):
    print(i)

    elem1 = driver.find_element_by_xpath(xpath + str(i) + xpath2)
    elem1.click()

    # driver.execute_script("window.confirm = function(msg) { return true; }")
