from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield
    driver.close()

def test_random_website_chrome(test_setup):

    class AssertionFailure(Exception):
        pass

    driver.get('https://nitratine.net/blog/post/how-to-detect-key-presses-in-python/')
    element = driver.find_element(By.XPATH, "//*[@title='Emotionify']")
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="root"]/section[3]/div/button')

    try:
        assert 'Emotionify' == driver.title, f"Unexpected page title: {driver.title}"
    except AssertionError as e:
        print(e)
        # pytest.fail("Page name has not the right value")
        # raise AssertionFailure("Wrong Title")
        
    try:
        assert 'Compare Myl Playlists →' == element.text, f"Unexpected element text: {element.text}"
    except AssertionError as e:
        print(e)
        # pytest.fail("Text of the 'Compare my Playlist' is not correct")
        # raise AssertionFailure("Text of the 'Compare my Playlist' is not correct")

    try:
        assert 'https://emotionify.nitratine.net/11' == driver.current_url, f"Unexpected page url: {driver.current_url}"
    except AssertionError as e:
        print(e)
        # pytest.fail("Url of webpage is not correct")
        # raise AssertionFailure("Wrong url address")
