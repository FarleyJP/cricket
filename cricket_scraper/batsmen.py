from http.client import REQUEST_URI_TOO_LONG
import requests
from bs4 import BeautifulSoup
import unicodedata


batting_table_identifier = "ds-w-full ds-table ds-table-xs ds-table-fixed ci-scorecard-table"
row_identifier = "ds-border-b ds-border-line ds-text-tight-s"

class BatsmanScorecard:

    def return_header(self):
        header = ["Batsman","Is_Out","Runs","Balls","Maidens","Fours","Sixes","Scoring_Rate"]
        return header

    def get_batsmen(self,input):
        batsmen = []
        for item in input:
            for other in (item.find_all(class_ = "ds-inline-flex ds-items-center ds-leading-none")):
                for this in other:
                    batsmen.append(unicodedata.normalize("NFKD", this.find(class_ = "ds-text-tight-s ds-font-medium").text))
        return batsmen

    def is_out(self,input):
        still_in = []
        for item in input:
            if item.find_all(class_ = "icon-keyboard_arrow_down-outlined ds-text-icon-primary ds-inline-flex ds-items-center") == []:
                still_in.append("0")
            else:
                still_in.append("1") 
        return still_in

    def get_stats(self,mine):
        stats = []
        for item in mine:
            temp_list = []
            for other in (item.find_all(class_ = "ds-min-w-max ds-text-right")):
                temp_list.append(other.text)
            stats.append(temp_list)
            temp_list = []
        return stats

    def single_scorecard(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        final_list = []
        batting_innings = []
        results = soup.find_all(class_= batting_table_identifier)
        for item in results:
            thus = item.find_all(class_ = row_identifier)
            thus.pop(0)
            thus.pop(-1)
            a = self.get_batsmen(thus)
            b = self.is_out(thus)
            c = self.get_stats(thus)
            for num in range(len(a)):
                batting_innings.append(a[num])
                batting_innings.append(b[num])
                for elt in c[num]:
                    batting_innings.append(elt)
                final_list.append(batting_innings)
                batting_innings = []
                print(final_list)
        return final_list   