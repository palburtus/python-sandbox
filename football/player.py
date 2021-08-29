class Player:
    
    def __init__(self, player_name, position, team):
        self.player_name = player_name
        self.position = position
        self.team = team
        self.cost = 0
        self.drafted_team = ''
        self.is_rookie = False
        self.ay = 0.0
        self.wopr = 0.0
        self.rush_attempts = 0
        self.ypa_rush = 0.0
        self.is_2019_keeper = False
        self.is_2020_keeper = False
        self.adp = 1.0
        self.tds = 0
        self.note = ''

    def set_ay(self, ay, wopr):
        self.ay = ay
        self.wopr = wopr

    def set_rush_yards(self, attempts, ypa):
        self.rush_attempts = attempts
        self.ypa_rush = ypa

    def set_is_rookie(self, is_rookie):
        self.is_rookie = is_rookie

    def set_2019_draft(self, cost, drafted_team, is_keeper):
        self.cost = cost
        self.drafted_team = drafted_team
        self.is_2019_keeper = is_keeper

    def set_2020_is_keeper(self, is_keeper):
        self.is_2020_keeper = is_keeper

    def set_adp(self, adp):
        self.adp = adp

    def set_tds(self, tds):
        self.tds = tds

    def set_note(self, note):
        self.note = note

    def add_tds(self, tds):
        self.tds += tds
        