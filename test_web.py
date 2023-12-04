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

def test_form(selenium):
    # run web server
    webserver = subprocess.Popen(['flask', '--app', 'hello', 'run'])
    time.sleep(1)

    try:
        # carreguem la pàgina del formulari
        selenium.get('http://localhost:5000/formulari')

        # busquem el quadre de text i hi escrivim un nom
        elem = selenium.find_element(By.TAG_NAME,"input")
        # nom aleatori
        nom = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        elem.send_keys(nom)

        # cerquem el botó de submit i el cliquem
        submit = selenium.find_element(By.XPATH,"//input[@type='submit']")
        submit.click()

        # comprovem que el missatge de salutació contingui
        # el nom introduit prèviament al formulari
        assert "Salut i força, {}".format(nom) in selenium.page_source

    finally:
        # finish web server
        webserver.kill()
