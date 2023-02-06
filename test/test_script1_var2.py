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

def test_website_title(test_setup):

    class AssertionFailure(Exception):
        pass

    driver.get('https://nitratine.net/blog/post/how-to-detect-key-presses-in-python/')
    element = driver.find_element(By.XPATH, "//*[@title='Emotionify']")
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="root"]/section[3]/div/button')

    if not 'Emotionify' == driver.title:
        # pytest.fail("Page name has not the right value")
        raise Exception("Wrong Title")

@pytest.mark.xfail
def test_elements_text(test_setup):

    class AssertionFailure(Exception):
        pass

    driver.get('https://nitratine.net/blog/post/how-to-detect-key-presses-in-python/')
    element = driver.find_element(By.XPATH, "//*[@title='Emotionify']")
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="root"]/section[3]/div/button')

    if not 'Compare My Playlists →' == element.text:
        pytest.fail("Text of the 'Compare my Playlist' is not correct")
        # raise Exception("Text of the 'Compare my Playlist' is not correct")

@pytest.mark.xfail
def test_webpage_url(test_setup):

    class AssertionFailure(Exception):
        pass

    driver.get('https://nitratine.net/blog/post/how-to-detect-key-presses-in-python/')
    element = driver.find_element(By.XPATH, "//*[@title='Emotionify']")
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="root"]/section[3]/div/button')

    if not 'https://emotionify.nitratine.net/' == driver.current_url:
        pytest.fail("Url of webpage is not correct")
        # raise Exception("Wrong url address")

