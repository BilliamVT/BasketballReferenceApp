# teams, players, seasons, box scores, play by play, shot chart, injuries from basketball reference
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.pbp import get_pbp
from basketball_reference_scraper.shot_charts import get_shot_chart
from basketball_reference_scraper.injury_report import get_injury_report

# imports
from tabulate import tabulate

# roster = get_roster('BOS', 2020)
#
# print(roster)

def main():
    roster = get_roster('BOS', 2008)

    print(tabulate(roster, headers='keys', tablefmt='psql'))

main()