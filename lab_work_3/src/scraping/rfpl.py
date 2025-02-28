from selenium.webdriver.common.by import By
from lab_work_3.src.scraping.browser import BrowserConnection
from schemas import *


main_page_rfpl = 'https://www.championat.com/football/_russiapl/tournament/5980/'


def get_href_seasons() -> list['SeasonPostDTO']:
    with BrowserConnection() as br:
        br.get(main_page_rfpl)
        year_select_el = br.find_element(By.NAME, "year")
        year_oprion_el = year_select_el.find_elements(By.TAG_NAME, "option")
        tournir_select_el = br.find_element(By.NAME, "tournir_id")
        tournir_option_el = tournir_select_el.find_elements(By.NAME, "option")
        