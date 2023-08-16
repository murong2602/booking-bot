from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time 
from datetime import datetime as dt
import pytz

singaporeTz = pytz.timezone("Asia/Singapore")
sgt = dt.now(singaporeTz)
current_sgt_datetime = dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day, dt.now(singaporeTz).hour, dt.now(singaporeTz).minute, dt.now(singaporeTz).second)



PATH = "YOUR_CHROMEDRIVER_PATH"
driver_service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=driver_service)

driver.get("https://wis.ntu.edu.sg/webexe88/owa/srce_smain_s.SRC_GenEntry?p_closewind=N")

undergrad = driver.find_element(By.CSS_SELECTOR, "#top > div > section:nth-child(2) > div > div > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > li > a > font > font" )
undergrad.click()


# enter booking page 
DD = input("Please enter DD: ")
MM = input("Please enter month (eg. Dec, Jan): ")
YYYY = input("Please enter YYYY: ")
day = input("Please enter day (eg. Thu): ")


print("1. 0800-0930\n2. 0930-1100\n3. 1100-1230\n4. 1230-1400\n5. 1400-1530\n6. 1530-1700\n7. 1700-1830\n8. 1830-2000\n9. 2000-2130")
session = input("Please select session: ")


# 0800-0930 : 2-8
# 0930-1000 : 8-14
# 1100-1230 : 14-20
# 1230-1400 : 20-26
# 1400-1530 : 26-32
# 1530-1700 : 32-38
# 1700-1830 : 38-44
# 1830-2000 : 44-50
# 2000-2130 : 50-56

if session == "1": 
    start = 2
    end = 8
elif session == "2":
    start = 8 
    end=14
elif session == "3":
    start = 14 
    end=20
elif session == "4":
    start = 20
    end=26
elif session == "5":
    start = 26
    end=32
elif session == "6":
    start = 32
    end=38
elif session == "7":
    start = 38
    end=44
elif session == "8":
    start = 44
    end=50
elif session == "9":
    start = 50
    end=56



loginID = WebDriverWait(driver, 5).until(
    lambda x: x.find_element(By.NAME, "UserName")
)
loginID.clear()
loginID.send_keys("YOUR_NTU_USERNAME")

ok = driver.find_element(By.NAME, "bOption")
ok.click()

password = WebDriverWait(driver, 5).until(
    lambda x: x.find_element(By.NAME, "PIN")
)
password.send_keys("YOUR_NTU_PASSWORD")

ok = driver.find_element(By.NAME, "bOption")
ok.click()

if(dt.now()< dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day,23,58)):
    print("Still a long way to go, come back at 11.58pm")
    quit()

else:
    while(dt.now() <= dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day+1,0,5)):
        print(dt.now())

        if(dt.now() >= dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day+1)):

            bball = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(By.CSS_SELECTOR, "#top > div > section:nth-child(2) > div > div > p > table > tbody > tr > td:nth-child(2) > form > ul > li:nth-child(4) > table:nth-child(4) > tbody > tr:nth-child(14) > td > input[type=radio]")
            )
            bball.click()


            # to get the column that we want (aka the date that we want)
            test = WebDriverWait(driver, 5).until(
                lambda x: x.find_element(By.XPATH, "//*[@id=\"top\"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[1]")
            )
            count = 0
            for date in test.find_elements(By.TAG_NAME, "td"):
                if date.text == DD+"\n"+MM+" "+ YYYY+"\n("+ day +")":
                    count += 1
                    break
                else: 
                    count += 1

            strcount = str(count)
            print(count)

            for i in range(start, end):
                if i==start: 
                    strcount = str(count)
                else: 
                    strcount = str(count-1)
                stri = str(i)
                string = "//*[@id=\"top\"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[" + stri +"]/td[" + strcount+ "]"
                try:
                    cell = driver.find_element(By.XPATH, string)
                    print(cell.text) 
                    input = cell.find_element(By.TAG_NAME, "input")
                    input.click()
                    submit = WebDriverWait(driver, 5).until(
                        lambda x: x.find_element(By.XPATH, "//*[@id=\"top\"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")
                    )
                    submit.click()
                    print("booked")
                    break
                except:
                    print("not available")
            break

        elif(dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day,23,59,58)<=dt.now() <= dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day,23,59,59)):
            print("Less than 1 second to go")
            time.sleep(0.5)
        elif(dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day,23,59,59)<dt.now()):
            print("Almost there")
            time.sleep(0.05)     
        elif(dt(dt.now(singaporeTz).year, dt.now(singaporeTz).month, dt.now(singaporeTz).day,23,59,15)<dt.now()):
            print("15 more seconds")
            time.sleep(1)
        else: 
            print("Not 12am yet..")
            time.sleep(5)

                



time.sleep(5)
