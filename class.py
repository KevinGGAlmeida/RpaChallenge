"""
    Simple Challenge Automation
"""

from time import sleep
from pathlib import Path
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class Locators:
    """
    Class that contains the XPATHS
    """

    # pylint: disable=R0902
    # pylint: disable=R0903
    def __init__(self):
        """
        Site XPATH Locators
        """
        # Btn
        self.btn_file_download = '//*[@href="./assets/downloadFiles/challenge.xlsx"]'
        self.btn_start_challenge = '//button[contains(text(),"Start")]'
        self.btn_submit = '//*[@value="Submit"]'
        # Input
        self.input_phone = '//*[@ng-reflect-name="labelPhone"]'
        self.input_email = '//*[@ng-reflect-name="labelEmail"]'
        self.input_address = '//*[@ng-reflect-name="labelAddress"]'
        self.input_last_name = '//*[@ng-reflect-name="labelLastName"]'
        self.input_role = '//*[@ng-reflect-name="labelRole"]'
        self.input_first_name = '//*[@ng-reflect-name="labelFirstName"]'
        self.input_company_name = '//*[@ng-reflect-name="labelCompanyName"]'
        # Text
        self.text_congratulations = '//*[contains(text(),"Congratulations!")]'


class ChallengeController:
    """
    Class to controll the page
    """

    def __init__(self, url):
        """
        Initial parameters
        """
        self.url = url
        self.driver = webdriver.Chrome()
        self.locators = Locators()
        self.df = None

    def launch(self):
        """
        Method to get the URL
        """
        self.driver.get(self.url)

    def donwload_file(self):
        """
        Method to downlaod the file
        """
        #Wait for button to exist, then, click on it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.btn_file_download))
        )
        self.driver.find_element(By.XPATH, self.locators.btn_file_download).send_keys(
            Keys.ENTER
        )

    def read_file(self):
        """
        Method to read the file
        """
        for _ in range(0, 30):
            for files in os.listdir(Path.home() / "Downloads"):
                if files.startswith("challenge") and files.endswith(".xlsx"):
                    self.df = pd.read_excel(Path.home() / f"Downloads/{files}")
                    os.remove(Path.home() / f"Downloads/{files}")
                    return True

                elif files.startswith("challenge"):
                    print("Waiting 10 seconds...")
                    sleep(10)
                    break

                else:
                    print("Waiting 10 seconds...")
                    sleep(10)
                    break

    def fullfilling_form(self):
        """
        Method to fullfill the form
        """
        # Click on Start
        self.driver.find_element(By.XPATH, self.locators.btn_start_challenge).click()
        for index in self.df.index:
            # Insert Address
            self.driver.find_element(By.XPATH, self.locators.input_address).send_keys(
                str(self.df["Address"].loc[index])
            )
            # Insert Company Name
            self.driver.find_element(
                By.XPATH, self.locators.input_company_name
            ).send_keys(str(self.df["Company Name"].loc[index]))
            # Insert First Name
            self.driver.find_element(
                By.XPATH, self.locators.input_first_name
            ).send_keys(str(self.df["First Name"].loc[index]))
            # Insert Last Name
            self.driver.find_element(By.XPATH, self.locators.input_last_name).send_keys(
                str(self.df["Last Name "].loc[index])
            )
            # Insert Role
            self.driver.find_element(By.XPATH, self.locators.input_role).send_keys(
                str(self.df["Role in Company"].loc[index])
            )
            # Insert Email
            self.driver.find_element(By.XPATH, self.locators.input_email).send_keys(
                str(self.df["Email"].loc[index])
            )
            # Insert phone number
            self.driver.find_element(By.XPATH, self.locators.input_phone).send_keys(
                str(self.df["Phone Number"].loc[index])
            )
            # Click on submit
            self.driver.find_element(By.XPATH, self.locators.btn_submit).click()

        # Wait for the text congratulations appears
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.text_congratulations))
        )

        # Takes screenshot
        self.driver.save_screenshot("finished.png")


app = ChallengeController("https://rpachallenge.com/")
app.launch()
app.donwload_file()
app.read_file()
app.fullfilling_form()
