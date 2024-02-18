from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("C:/Users/Alonzo/Desktop/Alon/DevopsExpert/tip_calc/index.html")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("1000")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "450.00"
assert expected == actual








# if expected == actual:
#     print("all good")
# else:
#     print("you have ruined the tip")
# sleep(1000)
