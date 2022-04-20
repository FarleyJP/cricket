from get_urls import GetURLS
from bowlers import BowlerScorecard
from batsmen import BatsmanScorecard

class Master_Scraper:
    
    def __init__(self,urls,player_type):
        self.urls = urls()
        self.player_type = player_type()
        self.header = self.player_type.return_header()

    def get_all_players_records(self):

        players = []
        players_flattened = []
        players_flattened.append(self.header) 
        all_urls = self.urls.get_hrefs()
        for url in all_urls:
            players.append(self.player_type.single_scorecard(url))   
        for player_records in players:
            for record in player_records:
                players_flattened.append(record)   
        return players_flattened 

    def write_all(list,url):
        with open(url, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(list)    

#bowler_scorecards = Master_Scraper(GetURLS,BowlerScorecard)
batsmen_scorecards = Master_Scraper(GetURLS,BatsmanScorecard)
#print(bowler_scorecards.get_all_players_records())
print(batsmen_scorecards.get_all_players_records())