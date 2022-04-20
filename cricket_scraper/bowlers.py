from get_urls import Beautiful
import requests
from bs4 import BeautifulSoup

class BowlerScorecard:


    def return_header(self):
        header = ["Bowler", "Overs", "Maidens", "Runs", "Wickets", "Run_Economy", "No_Runs", "Fours", "Sixes", "Wides", "No_Balls"]
        return header

    def single_scorecard(self,url):
            soup = self.get_beautiful_soup_object(url)
            bowler_tables = soup.find_all("table", {"class" : "ds-w-full ds-table ds-table-xs ds-table-fixed"}, recursive=True)
            final_list = []
            current_bowler = []
            for table in bowler_tables:
                bowlers = table.find_all('tr', {'class' : "ds-border-b ds-border-line ds-text-tight-s"}, recursive=True)
                bowlers.pop(0)
                for bowler in bowlers:
                    name = bowler.find('span', {'class' : "ds-text-tight-s ds-font-medium"}).text
                    current_bowler.append(name)
                    stats = bowler.find_all('td', {'class' : "ds-min-w-max ds-text-right"}, recursive=True)
                    for stat in stats:
                        current_bowler.append(stat.text)
                    final_list.append(current_bowler)
                    current_bowler = []
            return final_list

    def get_beautiful_soup_object(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup