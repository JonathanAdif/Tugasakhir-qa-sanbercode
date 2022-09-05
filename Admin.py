from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_keyword_filter(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Cassidy.Hope") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() 
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() 
        time.sleep(5)

    def test_a_success_keyword_filter(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() 
        time.sleep(1)
        browser.find_element(By.XPATH, 
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()
        time.sleep(1) 	
    
    def tearDown(self): 
            self.browser.close()

if __name__ == "__main__": 
    unittest.main()