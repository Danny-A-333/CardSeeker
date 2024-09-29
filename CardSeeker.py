import chromedriver_autoinstaller
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Decklog to TCGPlayer Mass Entry")
root.geometry("1200x800")
input = tk.StringVar()

def addExtra():
    pass

def getCode():

    code = input.get()

    chromedriver_autoinstaller.install()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.implicitly_wait(5)

    URL = 'https://decklog-en.bushiroad.com/view/' + code

    driver.get(URL)

    time.sleep(5)


    driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonDecline"]').click()

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    cards = soup.find_all('div', 'card-controller-inner')

    card_list = ""

    for card in cards:
        name = card.find('span', 'card-ctrl card-detail')
        namestr = str(name)
        namestr = namestr.split("\"")[3]
        set = namestr.split("/")[0]
        cardnum = namestr.split("/")[1].split()[0]
        cardname = namestr.split(":")[1]
        number = card.find('span', 'num').text

        card_list += number + cardname + " [" +set+"] " + set+"/"+cardnum+"\n"
    L1.delete("1.0", tk.END)
    L1.insert(tk.END, card_list)

def makeTTS():
    pass

title = tk.Label(text = "Welcome to CardSeeker!")
instructions = tk.Label(text = "Instructions: \n\n1. Enter a DeckLog code into the first entry box.\n2.Click the Load Entry button.\n3. Wait a few seconds.\n4. Copy the list of cards that appears\n5. Go to https://www.tcgplayer.com/massentry.\n6. Set the Product Line to \"Cardfight Vanguard\".\n7. Paste in the list of cards.\n8. Click \"Add to Cart\".\n9. If there are errors, remove the set codes from specific cards and try again.\nWARNING: This means that the cards added to cart might not match the set of the cards in the Deck Log.\n10. Optimize your cart.\n(I recommend using \"Keep Current Printings\" and \"Keep Current Set/Series\")")

code_entry = tk.Entry(root,textvariable = input, font=('calibre',10,'normal'))
load_entry=tk.Button(root,text = 'Load Entry', command = getCode)

L1 = Text(root, height = 40, width = 80)
L1.insert(tk.END, " ")

title.pack()
instructions.pack()
code_entry.pack()
load_entry.pack()
L1.pack()

root.mainloop()

