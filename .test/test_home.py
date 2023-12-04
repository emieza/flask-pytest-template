import pytest
import subprocess, time, random, string
from selenium.webdriver.common.by import By

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('-headless')
    return firefox_options

# TESTS
#############################################

def test_home(selenium):
    # run web server
    webserver = subprocess.Popen(['flask', '--app', 'hello', 'run'])
    time.sleep(1)

    # do test
    try:
        selenium.get('http://localhost:5000')
        assert "Pràctica Flask" in selenium.page_source
    finally:
        # finish web server
        webserver.kill()
