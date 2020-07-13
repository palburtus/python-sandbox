import re 
from team_draft import TeamDraft
from player import Player

team_abbreviation = ['Dal', 'Was', 'NYG', 'Phi', 'NE', 'NYJ', 'Mia', 'Buf', 'TB', 'Atl', 'NO', 'Car', 'Ind', 'Hou', 'Jac', "Ten", 'GB', 'Det', 'Min', 'Chi', 'Cin', 'Pit', 'Bal', 'Cle', 'LAR', 'Ari', 'Sea','SF', 'LAC', 'Den', 'Oak', 'KC']

draftedTeams = list()
draftedPlayers = list()
allPlayers = dict()

teamNameSpillter = ",,"
with open(r"C:\Users\patri\Google Drive\CBML\2020\2019-Draft.csv") as f:
    lines = f.readlines()
    team_name = ''
    for l in lines:
        
        if(teamNameSpillter in l):
            team_name = re.sub(teamNameSpillter, '', l)
            team_name = team_name.replace('\n', '')
            team_name = team_name.strip()
        else:
            csvs = l.split(',')
            if len(csvs) > 3:
                name = csvs[1].replace('"', '')
                if any(name[-3] in t for t in team_abbreviation):
                    team = name[-4:]
                if any(name[-2] in t for t in team_abbreviation):
                    team = name[-3:]
                team = team.replace(' ', '')
                name = name.replace(team, '')
                name = name.strip()
                position = csvs[2].replace('"', '')
                position = position.replace(' ', '')
                cost = csvs[3].replace('$', '')
                cost = cost.replace('\n', '')
                
                position = position.replace('"', '')
                draftee = Player(name, position, team, int(cost), team_name)
                draftedPlayers.append(draftee)
                allPlayers[name] = draftee

        team = TeamDraft(team_name, draftedPlayers)
        draftedTeams.append(team)
        draftedPlayers = list()

with open(r"C:\Users\patri\Google Drive\CBML\2020\airyards_2019.csv") as f:
    lines = f.readlines()
    team_name = ''
    for l in lines:
        if("full_name" not in l):
            csvs = l.split(',')
            player_name = csvs[1].replace('"', '')
            player_position = csvs[2].replace('"', '')
            player_team = csvs[3].replace('"', '')
            player_air_yards = csvs[7].replace('"', '')
            player_wopr = csvs[14].replace('"', '')
            p = allPlayers.get(player_name)
            if p is not None:
                airYards_player = allPlayers[player_name]
                airYards_player.set_ay(player_air_yards, player_wopr)
                allPlayers[player_name] = airYards_player
            else:
                airYards_player = Player(player_name, player_position, player_team)
                airYards_player.set_ay(player_air_yards, player_wopr)
                allPlayers[player_name] = airYards_player



for k,v in allPlayers.items():
    p = allPlayers[k]
    print("%s - NFL Team: %s Position: %s Cost: $%d Drafted by: %s Air Yards: %s WOPR: %s" % (p.player_name, p.team, p.position, p.cost, p.drafted_team, p.ay, p.wopr))