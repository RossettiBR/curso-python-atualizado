# type: ignore
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC)
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    options = ()
    browser = make_chrome_browser(*options)
    browser.get('')

    # search_box_text = WebDriverWait(browser, TIME_TO_WAIT).until(
    #     EC.presence_of_element_located(
    #         (By.NAME, 'cpf'),
    #     )
    # )
    # search_box_text.send_keys('')
    # search_box_text.send_keys(Keys.ENTER)

    var = browser.find_element

    cpf = var(By.NAME, 'cpf')
    cpf.send_keys('123')
    data_nascimento = browser.find_element(By.NAME, 'datanasc')
    data_nascimento.send_keys('123')
    cnpj = browser.find_element(By.NAME, 'cnpj')
    cnpj.send_keys('123')
    nire = browser.find_element(By.NAME, 'nire')
    nire.send_keys('123')
    # avançar = browser.find_element(By.CLASS_NAME, 'button')
    # avançar.click()


    # results = browser.find_element(By.ID, 'search')
    # links = results.find_elements(By.TAG_NAME, 'a')
    # links[0].click()
    sleep(TIME_TO_WAIT)
