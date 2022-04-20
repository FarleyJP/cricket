from selenium import webdriver
import requests
from bs4 import BeautifulSoup


class GetURLS:
    def _create_webdriver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def _get_all_href_tags(self):
        driver = self._create_webdriver()
        driver.get("https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-results")
        lnks= self.driver.find_elements_by_tag_name("a")
        hrefs = []
        for lnk in lnks:
            hrefs.append((lnk.get_attribute('href')))
        driver.quit()
        return hrefs

    def get_hrefs(self):
        hrefs = self._get_all_href_tags()
        filtered_list = []
        for href in hrefs:
            if "/series/indian-premier-league-2022-1298423/" in href:
                if "full-scorecard" in href:
                    filtered_list.append(href)
        return filtered_list

class Beautiful:    
    def get_beautiful_soup_object(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup    