class Player:
    def __init__(self, player_name, position, team, cost = 0, drafted_team = '', is_rookie = False):
        self.player_name = player_name
        self.position = position
        self.team = team
        self.cost = cost
        self.drafted_team = drafted_team
        self.is_rookie = is_rookie 
        