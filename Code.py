# -*- coding: utf-8 -*-
"""Code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ytoafPlnv4kuNfbRLXygDDxKzK2TxZF4
"""

browser=webdriver.Chrome("chromedriver yolu") 
browser.get("https://www.instagram.com/")
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
.send_keys("Mail or ID")
browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")\
.send_keys("Şifre")
time.sleep(1)
browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")\
.click()
time.sleep(4)
tıkla=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
tıkla.click()
time.sleep(2)
tıkla2=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
tıkla2.click()
time.sleep(2)
tıkla3=browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")
tıkla3.click()
time.sleep(2)
d=1
while d<20:
    c=4
    while c<50:

        tıkla4=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div["+str(c)+"]/div[3]/button")
        tıkla4.click()
        time.sleep(0.3)
        c+=1
    browser.refresh()  
    time.sleep(4)
    d+=1