"""
    Main file to run the rpa challenge automation
"""
from classes import ChallengeController

if __name__ == "__main__":
    app = ChallengeController("https://rpachallenge.com/")
    app.launch()
    app.donwload_file()
    app.read_file()
    app.fullfilling_form()
