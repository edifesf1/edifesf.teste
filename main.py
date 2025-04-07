from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.common import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headlines")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service(ChromeDriverManager().install()),options=chrome_options)
    driver.ger("https://google.com")
    title = driver.title