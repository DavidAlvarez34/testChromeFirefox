#Import webdriver selenium for my browser
import pytest
from selenium import webdriver

#chrome browser
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager

#firefox browser
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#options for headlees mode
from selenium.webdriver.chrome.options import Options #manejar navegadores

#pasar diferentes valores de prueba dependiendo de la linea de comados
def pytest_addoption(parser):
    #default execute chrome
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' or 'firefox' as parameter for execution"
    )

@pytest.fixture() #funcion de las pruebas de que se utiliza de forma automatica
def driver(request):
    browser = request.config.getoption("--browser")
    #Default driver value
    driver=""
    # Option setup to run in headlees mode (in order to run this in ghup actions)
    options = Options()
    # add new argument ,--headlees: open instace the chrome
    options.add_argument("--headlees")
    #setup
    print(f"\n Setting up: {browser} driver")
    if browser == "chrome": #Compara que es lo que llego en consola para open browser
        driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    elif browser == "firefox":
        driver =webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    #experar 10 segundos
    driver.implicitly_wait(10)

    yield driver #return driver using in test

    #Tear down
    print(f"\nTear down:{browser} driver")

    driver.quit() #cerrar el driver