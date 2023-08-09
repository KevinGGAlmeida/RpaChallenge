import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyscreenshot



def DownloadFile(driver):
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")))
    driver.execute_script('document.querySelector(`[href="./assets/downloadFiles/challenge.xlsx"]`).click()')


def ReadFile():
    return pd.read_excel("challenge.xlsx")


def PressStart(driver):
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")))
    driver.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

def InsertingValues(driver,LabelName,Value):
    driver.execute_script(f'document.querySelector(`[ng-reflect-name="{LabelName}"]`).value = "{Value}"')

def Submit(driver):
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")))
    driver.execute_script('document.querySelector(`[value="Submit"]`).click()')

def Screenshot():
    pyscreenshot.grab().save("finish.png")

