from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from PIL import Image
import pyautogui
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException, NoAlertPresentException
#extra imports
import argparse
import json
import os
import traceback
import builtins
import platform
import random
import subprocess
import sys
import time
import urllib.parse
from argparse import ArgumentParser
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Union, List, Literal
import copy
from functools import wraps
from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException, NoAlertPresentException,
                                        NoSuchElementException, SessionNotCreatedException, TimeoutException,
                                        UnexpectedAlertPresentException, JavascriptException,
                                        ElementNotVisibleException, ElementClickInterceptedException)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import tkinter as tk
from tkinter import messagebox, ttk
from math import ceil
#\\CONFIG\\
POINTS_COUNTER = 0

# Global variables
# added accounts when finished or those have same date as today date in LOGS at beginning.
FINISHED_ACCOUNTS = []
ERROR = True  # A flag for when error occurred.
# A flag for when the account has mobile bing search, it is useful for accounts level 1 to pass mobile.
MOBILE = True
CURRENT_ACCOUNT = None  # save current account into this variable when farming.
LOGS = {}  # Dictionary of accounts to write in 'logs_accounts.txt'.
FAST = False  # When this variable set True then all possible delays reduced.
SUPER_FAST = False  # fast but super
BASE_URL = "https://rewards.bing.com/"

#beta v1.2.0

#dm a person#2664 if something doesnt work

#chromedriver path
dpath ='C:\\Users\\Administrator\\Desktop\\ABS-X 1\\chromedriver.exe'

#extensions path
ABS = 'C:\\Users\\Administrator\\Desktop\\ABS-X 1\\ABS.zip'
MS = 'C:\\Users\\Administrator\\Desktop\\ABS-X 1\\MS.zip'
urban= 'C:\\Users\\Administrator\\Desktop\\ABS-X 1\\Urbanvpn.zip'

#accounts:
account1 = 'rajbirkaurbhinder03@gmail.com'
account2 = 'gurjot9929@gmail.com'
account3 = 'harshbajwa9398@gmail.com'
account4 = 'rewardsmicrosoft9385@gmail.com'
account5 = 'sukhmanmicrosoft1@gmail.com'
account6 = 'dhaliwaln721@gmail.com'

#passwords:
password1 = 'bhinder1'
password2 = 'bhinder1'
password3 = 'bhinder1'
password4 = 'bhinder1'
password5 = 'bhinder1'
password6 = 'bhinder1'

#servers
server1 = 'USA'
server2 = 'JAPAN'

#no need to worry about the code below but u can read it if u like its not organized at all, i will do it later

#\\END OF CONFIG\\
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account1)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password1)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password1)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('connecting to usa server')
driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(1)
window_before = driver.window_handles[0]

time.sleep(7)
print('connected to usa server')
print('completing tasks')

ARGS = ArgumentParser()

driver.get('https://rewards.bing.com')
time.sleep(5)

def completeMSNShoppingGame(browser: driver) -> bool:
    """Complete MSN Shopping Game, returns True if completed successfully else False"""

    def expandShadowElement(element, index: int = None) -> Union[List[WebElement], WebElement]:
        """Returns childrens of shadow element"""
        if index is not None:
            shadow_root = WebDriverWait(browser, 45).until(
                ec.visibility_of(browser.execute_script(
                    'return arguments[0].shadowRoot.children', element)[index])
            )
        else:
            # wait to visible one element then get the list
            WebDriverWait(browser, 45).until(
                ec.visibility_of(browser.execute_script(
                    'return arguments[0].shadowRoot.children', element)[0])
            )
            shadow_root = browser.execute_script(
                'return arguments[0].shadowRoot.children', element)
        return shadow_root

    def getChildren(element) -> List[WebElement]:
        """get children"""
        children = browser.execute_script(
            'return arguments[0].children', element)
        return children

    def getSignInButton() -> WebElement:
        """check whether user is signed in or not and return the button to sign in"""
        script_to_user_pref_container = 'document.getElementsByTagName("shopping-page-base")[0]\
            .shadowRoot.children[0].children[1].children[0]\
            .shadowRoot.children[0].shadowRoot.children[0]\
            .getElementsByClassName("user-pref-container")[0]'
        WebDriverWait(browser, 60).until(ec.visibility_of(
            browser.execute_script(f'return {script_to_user_pref_container}')
        )
        )
        button = WebDriverWait(browser, 60).until(ec.visibility_of(
            browser.execute_script(
                f'return {script_to_user_pref_container}.\
                    children[0].children[0].shadowRoot.children[0].\
                    getElementsByClassName("me-control")[0]'
            )
        )
        )
        return button

    def signIn() -> None:
        """sign in"""
        sign_in_button = getSignInButton()
        sign_in_button.click()
        print("[MSN GAME] Signing in...")
        time.sleep(5)
        waitUntilVisible(browser, By.ID, 'newSessionLink', 10)
        browser.find_element(By.ID, 'newSessionLink').click()
        waitUntilVisible(browser, By.TAG_NAME, 'shopping-page-base', 60)
        expandShadowElement(browser.find_element(
            By.TAG_NAME, 'shopping-page-base'), 0)
        getSignInButton()

    def getGamingCard() -> Union[WebElement, Literal[False]]:
        """get gaming card"""
        shopping_page_base_childs = expandShadowElement(
            browser.find_element(By.TAG_NAME, 'shopping-page-base'), 0)
        shopping_homepage = shopping_page_base_childs.find_element(
            By.TAG_NAME, 'shopping-homepage')
        msft_feed_layout = expandShadowElement(
            shopping_homepage, 0).find_element(By.TAG_NAME, 'msft-feed-layout')
        msn_shopping_game_pane = expandShadowElement(msft_feed_layout)
        for element in msn_shopping_game_pane:
            if element.get_attribute("gamestate") == "active":
                return element
        else:
            return False

    def clickCorrectAnswer() -> None:
        """click correct answer"""
        options_container = expandShadowElement(gaming_card, 1)
        options_elements = getChildren(getChildren(options_container)[1])
        # click on the correct answer in options_elements
        correct_answer = options_elements[int(
            gaming_card.get_attribute("_correctAnswerIndex"))]
        # hover to show the select button
        correct_answer.click()
        time.sleep(1)
        # click 'select' button
        select_button = correct_answer.find_element(
            By.CLASS_NAME, 'shopping-select-overlay-button')
        WebDriverWait(browser, 5).until(
            ec.element_to_be_clickable(select_button))
        select_button.click()

    def clickPlayAgain() -> None:
        """click play again"""
        time.sleep(random.randint(4, 6))
        options_container = expandShadowElement(gaming_card)[1]
        getChildren(options_container)[0].find_element(
            By.TAG_NAME, 'button').click()

    try:
        if (ARGS.headless or ARGS.virtual_display) and platform.system() == "Linux":
            browser.set_window_size(1920, 1080)
        tries = 0
        print("[MSN GAME] Trying to complete MSN shopping game...")
        print("[MSN GAME] Checking if user is signed in ...")
        while tries <= 4:
            tries += 1
            goToURL(browser, "https://www.msn.com/en-us/shopping")
            waitUntilVisible(browser, By.TAG_NAME, 'shopping-page-base', 45)
            time.sleep(calculateSleep(15))
            try:
                sign_in_button = getSignInButton()
            except:
                if tries == 4:
                    raise ElementNotVisibleException(
                        "Sign in button did not show up")
            else:
                break
        time.sleep(5)
        if "Sign in" in sign_in_button.text:
            signIn()
        gaming_card = getGamingCard()
        scrolls = 0
        while not gaming_card and scrolls <= 5:
            scrolls += 1
            print(f"Locating gaming card - scrolling ({scrolls}/5)")
            browser.execute_script("window.scrollBy(0, 300);")
            time.sleep(calculateSleep(10))
            gaming_card = getGamingCard()
            if gaming_card:
                browser.execute_script(
                    "arguments[0].scrollIntoView();", gaming_card)
                print("[MSN GAME] Gaming card found")
                time.sleep(calculateSleep(10))
            if scrolls == 5 and not gaming_card:
                raise NoSuchElementException("Gaming card not found")
        print("[MSN GAME] Answering questions ...")
        for _ in range(10):
            try:
                clickCorrectAnswer()
                clickPlayAgain()
                time.sleep(calculateSleep(10))
            except (NoSuchElementException, JavascriptException):
                break
    except NoSuchElementException:
        prYellow("[MSN GAME] Failed to locate MSN shopping game !")
        finished = False
    except Exception as exc:  # skipcq
        displayError(exc)
        prYellow("[MSN GAME] Failed to complete MSN shopping game !")
        finished = False
    else:
        prGreen("[MSN GAME] Completed MSN shopping game successfully !")
        finished = True
    finally:
        goToURL(browser, BASE_URL)
        LOGS[CURRENT_ACCOUNT]["MSN shopping game"] = True
        updateLogs()
        return finished


driver.execute_script('''document.body.style.zoom = "100%";''')

try:
    reward1 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward1.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')


driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

try:
    reward2 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[2]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward2.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')

driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

try:
    reward3 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[3]/span')
    reward3.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')

driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

try:
    reward4 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[1]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward4.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')

driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

try:
    reward412 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[4]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward412.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')

driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

try:
    reward5 = driver.find_element("xpath", '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-more-activities-card/mee-card-group/div/mee-card[2]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[3]/span')
    reward5.click()
    driver.execute_script('''document.querySelector('#modal-host > div:nth-child(2) > button').click();''')
except (NoSuchElementException, ElementNotInteractableException) as e:
    pass

time.sleep(7)

try:
    handles = driver.window_handles
    if len(handles) < 2:
        raise IndexError('No second window found')
    driver.switch_to.window(handles[1])
    last_page_change_time = time.time()
    last_url = driver.current_url
    last_title = driver.title
    while True:
        current_url = driver.current_url
        current_title = driver.title
        if current_url != last_url or current_title != last_title:
            last_page_change_time = time.time()
            last_url = current_url
            last_title = current_title
        else:
            if time.time() - last_page_change_time > 10:
                driver.get('https://rewards.bing.com')
                break
        time.sleep(1)
except IndexError:
    print('weather button has not been found')

driver.close()
driver.switch_to.window(window_before)
time.sleep(1.9)

print('tasks completed')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 1 farming completed')
driver.quit()
#end of account #1
print('started account 2')
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account2)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password2)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password2)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('starting searches')

# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed')
print('verifying searches')
time.sleep(1)

# Load the image
image = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\mobilesearchescheck.png')

# Get the dimensions of the image
width, height = image.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1)
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")
  
print('mobile searches completed')
print('verifying pc searches')

time.sleep(1)
# Load the image
image2 = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\pcsearchescheck.png')

# Get the dimensions of the image
width, height = image2.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image2)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified", location)
    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com/welcome')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searches completed')
print('connecting to usa server')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(7)
print('connected to usa server')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 2 farming completed')
driver.quit()
#end of account #2
print('started account 3')
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account3)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password3)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password3)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('starting searches')

# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed')
print('verifying searches')
time.sleep(1)

# Load the image
image = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\mobilesearchescheck.png')

# Get the dimensions of the image
width, height = image.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1)
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")
  
print('mobile searches completed')
print('verifying pc searches')

time.sleep(1)
# Load the image
image2 = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\pcsearchescheck.png')

# Get the dimensions of the image
width, height = image2.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image2)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified", location)
    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com/welcome')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searches completed')
print('connecting to usa server')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break


wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(7)
print('connected to usa server')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 3 farming completed')
driver.quit()
#end of account #3
print('started account 4')
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account4)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password4)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password4)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('starting searches')

# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed')
print('verifying searches')
time.sleep(1)

# Load the image
image = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\mobilesearchescheck.png')

# Get the dimensions of the image
width, height = image.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1)
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")
  
print('mobile searches completed')
print('verifying pc searches')

time.sleep(1)
# Load the image
image2 = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\pcsearchescheck.png')

# Get the dimensions of the image
width, height = image2.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image2)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified", location)
    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com/welcome')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searches completed')
print('connecting to usa server')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(7)
print('connected to usa server')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 4 farming completed')
driver.quit()
#end of account #4
print('started account 5')
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account5)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password5)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password5)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('starting searches')

# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed')
print('verifying searches')
time.sleep(1)

# Load the image
image = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\mobilesearchescheck.png')

# Get the dimensions of the image
width, height = image.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1)
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")
  
print('mobile searches completed')
print('verifying pc searches')

time.sleep(1)
# Load the image
image2 = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\pcsearchescheck.png')

# Get the dimensions of the image
width, height = image2.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image2)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified", location)
    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com/welcome')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searches completed')
print('connecting to usa server')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(7)
print('connected to usa server')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 5 farming completed')
driver.quit()
#end of account #5
print('started account 6')
#object of Options class
op = Options()

#set .zip file path of extension
op.add_extension(ABS)
op.add_extension(MS)
op.add_extension(urban)
op.add_argument("--enable-webgl-developer-extensions")
op.add_argument("--enable-webgl-draft-extensions")

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path=dpath,options=op)
driver.maximize_window()
#launch browser
#1
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop-iterations"]')))
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)

#close the third tab
max_wait_time = 25
start_time = time.time()

while True:
    if len(driver.window_handles) == 3:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        break
    elif time.time() - start_time > max_wait_time:
        break
    else:
        time.sleep(0.5)

# Close the second tab
driver.close()

# Switch back to the first window
driver.switch_to.window(driver.window_handles[0])
time.sleep(1.5)

print('signing in')

driver.get('https://www.microsoft.com/rpsauth/v1/account/SignIn?ru=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2F%3Fql%3D4')

# enter email
wait = WebDriverWait(driver, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
element.send_keys(account6)
mssbutton = driver.find_element("xpath", '//*[@id="idSIButton9"]')
mssbutton.click()
# enter password
wait = WebDriverWait(driver, 1000)
try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password6)
except StaleElementReferenceException:
    # Locate the element again before sending keys
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password6)

driver.find_element(By.ID, "idSIButton9").click()

print('signed in successfully')
print('signing in on webpage')

time.sleep(0.9)
driver.get('https://www.bing.com/search?q=Jonny+Depp&form=QBLH&sp=-1&ghc=1&lq=0&pq=jonny+depp&sc=10-10&qs=n&sk=&cvid=DBA4784E791C4D3B9187C4BD880BAE17&ghsh=0&ghacc=0&ghpl=')

time.sleep(4)

while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_a'))
        )
        element.click()
        time.sleep(1)
    except:
        break

time.sleep(10)
print('successfull')
print('starting searches')

# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed')
print('verifying searches')
time.sleep(1)

# Load the image
image = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\mobilesearchescheck.png')

# Get the dimensions of the image
width, height = image.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1)
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")
  
print('mobile searches completed')
print('verifying pc searches')

time.sleep(1)
# Load the image
image2 = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\pcsearchescheck.png')

# Get the dimensions of the image
width, height = image2.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(image2)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified", location)
    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com/welcome')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('chrome-extension://oioepdjiiododacbmpoieeacfgjchffn/popup/index.html')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searches completed')
print('connecting to usa server')
#1st server
while True:
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button_pink"))
        )
        element.click()
        time.sleep(0.5)
    except:
        break

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select_location__input')))
if element.is_enabled():
    element.click()
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(server1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'location')))
if element.is_enabled():
    element.click()

time.sleep(7)
print('connected to usa server')
print('starting searches in usa server')
# Start the web driver and load the page
driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
abs1text.clear()
abs1text.send_keys(40) 
abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
abs2text.clear()
abs2text.send_keys(30) 
abs3text = driver.find_element("xpath", '//*[@id="delay"]')
abs3text.clear()
abs3text.send_keys(2000)
startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
startsearch.click()
last_page_change_time = time.time()
last_url = driver.current_url
last_title = driver.title
while True:
    current_url = driver.current_url
    current_title = driver.title
    if current_url != last_url or current_title != last_title:
        last_page_change_time = time.time()
        last_url = current_url
        last_title = current_title
    else:
        if time.time() - last_page_change_time > 10:
            driver.get('https://rewards.bing.com/pointsbreakdown')
            break
    time.sleep(1)

print('searches completed in usa server')
print('verifying pc searches in usa server')

time.sleep(1)
# Load the image
uspcsearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\uspcsearches.png')

# Get the dimensions of the image
width, height = uspcsearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(uspcsearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("pc searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("pc searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(15) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(1)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('pc searched completed')

print('verifying mobile searches in usa server')
# Start the web driver and load the page
time.sleep(1)
# Load the image
usmobilesearch = Image.open('C:\\Users\\Administrator\\Desktop\\ABS-X 1\\images\\usmobilesearches.png')

# Get the dimensions of the image
width, height = usmobilesearch.size

# Search for the image on the screen
location = pyautogui.locateOnScreen(usmobilesearch)

# If the image is found, location will be a tuple with the coordinates
# of the upper-left corner of the image on the screen
if location is not None:
    print("mobile searches verified in usa server", location)
    driver.get('https://rewards.bing.com/pointsbreakdown')
    # Do not run the code
else:
    print("mobile searches not completed, completing them...")
    # Run the code
    driver.get('https://rewards.bing.com')
    try:
        driver.get('chrome-extension://ipbgaooglppjombmbgebgmaehjkfabme/popup.html')
        abs1text = driver.find_element("xpath", '//*[@id="desktop-iterations"]')
        abs1text.clear()
        abs1text.send_keys(1) 
        abs2text = driver.find_element("xpath", '//*[@id="mobile-iterations"]')
        abs2text.clear()
        abs2text.send_keys(10)
        abs3text = driver.find_element("xpath", '//*[@id="delay"]')
        abs3text.clear()
        abs3text.send_keys(2000)
        startsearch = driver.find_element("xpath", '/html/body/div[5]/input[1]')
        startsearch.click()
        last_page_change_time = time.time()
        last_url = driver.current_url
        last_title = driver.title
        while True:
            current_url = driver.current_url
            current_title = driver.title
            if current_url != last_url or current_title != last_title:
                last_page_change_time = time.time()
                last_url = current_url
                last_title = current_title
            else:
                if time.time() - last_page_change_time > 10:
                    driver.get('https://rewards.bing.com/pointsbreakdown')
                    break
            time.sleep(1)
    except:
        print("An error occurred while running the code")

print('mobile searches completed')
print('account 6 farming completed')
driver.quit()
#end of account #6