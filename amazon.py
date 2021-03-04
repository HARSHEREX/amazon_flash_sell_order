"""
Created on Thu Aug 27 18:20:42 2020
@author: harshit.soni
"""

from selenium import webdriver
import time
import pandas as pd
#####################################id pass
print('\n----  order will be on cash on delivery  ----\n----  please set a default address on amazon before using this automation tool ----')
loginid =input('Enter amazon id with country code (+91) : ')
passs = input('amazon password : ')
pay_selection = 1
url = input("enter product url : ")


option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
chromedriverpath= "c87.exe"  
driver = webdriver.Chrome(executable_path=chromedriverpath, chrome_options=option)


    
def inner1(optt):       
    inputs = optt.find_elements_by_class_name("a-input-text")
    try:
        inputs[0].clear()
    except :
        pass
    inputs[0].send_keys(name_on_card)    
    inputs[1].send_keys(card_no)  
    date_dropdowns = optt.find_elements_by_class_name("a-button-text")
    date_dropdowns[0].click()
    month = driver.find_element_by_class_name("a-nostyle").find_elements_by_tag_name("li")
    month[int(month_selection)-1].click()
    date_dropdowns[1].click()
    year = driver.find_elements_by_class_name("a-nostyle")
    year =  year[1].find_elements_by_tag_name("li")
    for y in year:
        if y.text == year_selection:
            y.click()
    optt.find_element_by_class_name("a-width-small").send_keys(cvv)
    optt.find_element_by_class_name("a-button-input").click()

def inner2():
    try:
        driver.find_element_by_id("prime-interstitial-nothanks-button").click()
    except :
        pass

def del_op(pay,pay_selection):
    if pay_selection ==1:
        for opt in pay:
            if "Pay on Delivery" in opt.text:
                optt = opt
                opt.click()
                final_click = driver.find_elements_by_class_name("a-button-input")
                for f in final_click:
                    try:
                        print("test 3")
                        f.click()
                        print("test 4")
                        inner2()
                        print("inner 2 called")
                        break
                    except :
                        continue
                while True:
                    try:
                        driver.find_element_by_class_name("place-your-order-button").click()
                        print("order is placed")
                        break
                    except :
                        continue
                        
    else:                
        try:
            print("op started")
            print("test 1")
            print("len of pay : ",len(pay))
            for opt in pay:
                if card_no[-4:] in opt.text:
                    optt = opt
                    opt.click()
                    opt.find_element_by_class_name("a-width-small").send_keys(cvv)
                    print("test 2")
                    final_click = driver.find_elements_by_class_name("a-button-input")
                    for f in final_click:
                        try:
                            print("test 3")
                            f.click()
                            print("test 4")
                            inner2()
                            print("inner 2 called")
                            break
                        except :
                            continue
                elif opt.text == "Add Debit/Credit/ATM Card":
                    try:
                        print("elif condition in del op")
                        optt = opt
                        opt.click()
                        inner1(optt)
                    except :
                        pass
        except Exception as e :
            print("exception in del op")
            print(e)
        

def main(n,pay_selection):
    driver.get(url)
    driver.find_element_by_xpath("""//*[@id="nav-link-accountList"]""").click()
    time.sleep(0.01)
    driver.find_element_by_xpath("""//*[@id="ap_email"]""").send_keys(loginid)
    time.sleep(0.01)
    driver.find_element_by_id("continue").click()
    time.sleep(0.01)
    driver.find_element_by_xpath("""//*[@id="ap_password"]""").send_keys(passs)
    time.sleep(0.01)
    driver.find_element_by_id("signInSubmit").click()
    i=0
    while True:
        try:
            print("try : ",i)
            i=i+1
            driver.find_element_by_id("buy-now-button").click()
            time.sleep(1)
            pay = driver.find_elements_by_class_name("pmts-instrument-box")
            print("caling op")
            del_op(pay,pay_selection)
            break
        except :
            while True:
                try:
                    if str(driver.find_element_by_xpath("""/html/body""").text).split("\n")[0]=="Authentication required":    
                        print("auth")
                    else:
                        int("abcd")
                except:
                    break
            continue
                    
                



main(0,pay_selection)

