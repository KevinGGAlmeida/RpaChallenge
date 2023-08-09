from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Functions import DownloadFile,ReadFile,InsertingValues,PressStart,Screenshot,Submit


class RpaChallenge:

    def __init__(self,site):
        self.site = site
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

    def Launch(self):
        self.driver = webdriver.Chrome(service=Service("/app/chromedriver"),options=self.chrome_options)
        self.driver.get(self.site)

    def Download(self):
        DownloadFile(self.driver)

    def Data(self):
        self.data = ReadFile()
    def FillingOutForms(self):
        PressStart(self.driver)
        for line in self.data.index:
            InsertingValues(self.driver,"labelCompanyName",self.data["Company Name"][line])
            InsertingValues(self.driver,"labelAddress",self.data["Address"][line])
            InsertingValues(self.driver,"labelFirstName",self.data["First Name"][line])
            InsertingValues(self.driver,"labelRole",self.data["Role in Company"][line])
            InsertingValues(self.driver,"labelEmail",self.data["Email"][line])
            InsertingValues(self.driver,"labelPhone",self.data["Phone Number"][line])
            InsertingValues(self.driver,"labelLastName",self.data["Last Name "][line])
            Submit(self.driver)
            print(f"Line: {line} Done")
            
        self.driver.save_screenshot("finished.png")


Run = RpaChallenge("https://rpachallenge.com/")
Run.Launch()
Run.Download()
Run.Data()
Run.FillingOutForms()
print("Process Finished")
