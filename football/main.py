import re 
from team_draft import TeamDraft
from player import Player

team_abbreviation = ['Dal', 'Was', 'NYG', 'Phi', 'NE', 'NYJ', 'Mia', 'Buf', 'TB', 'Atl', 'NO', 'Car', 'Ind', 'Hou', 'Jac', "Ten", 'GB', 'Det', 'Min', 'Chi', 'Cin', 'Pit', 'Bal', 'Cle', 'LAR', 'Ari', 'Sea','SF', 'LAC', 'Den', 'Oak', 'KC']

draftedTeams = list()
draftedPlayers = list()
allPlayers = list()

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
                allPlayers.append(draftee)

        team = TeamDraft(team_name, draftedPlayers)
        draftedTeams.append(team)
        draftedPlayers = list()
    for t in draftedTeams:
        
        for d in t.draftees:
            print("%s - NFL Team: %s Position: %s Cost: $%d Drafted by: %s" % (d.player_name, d.team, d.position, d.cost, d.drafted_team))