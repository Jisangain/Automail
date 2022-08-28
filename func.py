import undetected_chromedriver.v2 as uc
import random
import tg
import requests
import json
import readchar
from selenium.webdriver.common.by import By
from time import sleep, time
from telegram.ext import Updater

def send(filename):
    updater = Updater("5100946328:AAGB7wKNXFf2ROLNWwo2F9-maQ6SDgkZRbw", use_context=True)
    updater.bot.send_document("847547511,", open(filename, 'rb'))

def find_by_id(driver,text):
    return driver.find_element(By.XPATH,'//*[@id="'+text+'"]')
def find_by_name(driver,text):
    return driver.find_element(By.XPATH,'//*[@name="'+text+'"]')
def find_by_text(driver, text):
    return driver.find_element(By.XPATH,"//*[text()='"+text+"']")
def to_write(filename, text, _type):
    raw_err = open(filename,_type)
    raw_err.write(str(text))
    raw_err.close()