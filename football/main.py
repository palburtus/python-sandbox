import re 
from team_draft import TeamDraft
from player import Player
import json
from utils import normalize_name
from auto_completer import AutoCompleter
from pyreadline import Readline
readline = Readline()

notes = dict()

def run():
    
    team_abbreviation = ['Dal', 'Was', 'NYG', 'Phi', 'NE', 'NYJ', 'Mia', 'Buf', 'TB', 'Atl', 'NO', 'Car', 'Ind', 'Hou', 'Jac', "Ten", 'GB', 'Det', 'Min', 'Chi', 'Cin', 'Pit', 'Bal', 'Cle', 'LAR', 'Ari', 'Sea','SF', 'LAC', 'Den', 'Oak', 'KC']

    draftedTeams = list()
    draftedPlayers = list()
    allPlayers = dict()
    playerNames = list()

    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\rotoworld_2021_rankings.csv") as f:
        lines = f.readlines()
        for l in lines:
            if("Player" not in l):
                csvs = l.split(',')
                rank_number = csvs[0].replace('"', '')
                rank_player_name = csvs[1].replace('"', '')
                rank_postion = csvs[2].replace('"', '')
                rank_nfl_team = csvs[3].replace('"', '')

                rank_player_name = normalize_name(rank_player_name)     

                playerNames.append(rank_player_name)

                rankedPlayer = Player(rank_player_name, rank_postion, rank_nfl_team)
                allPlayers[rank_player_name] = rankedPlayer


    teamNameSpillter = ",,"
    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\2020-Draft.csv") as f:
        lines = f.readlines()
        team_name = ''
        for l in lines:
            
            if(teamNameSpillter in l):
                team_name = re.sub(teamNameSpillter, '', l)
                team_name = team_name.replace('\n', '')
                team_name = team_name.replace(',N', '')
                team_name = team_name.replace('ï»¿', '')
                team_name = team_name.strip()
            else:
                if("BID AMOUNT" not in l):
                    csvs = l.split(',')
                    if len(csvs) > 3:
                        name = csvs[1].replace('"', '')
                        if any(name[-3] in t for t in team_abbreviation):
                            team = name[-4:]
                        if any(name[-2] in t for t in team_abbreviation):
                            team = name[-3:]
                        team = team.replace(' ', '')
                        name = name.replace(team, '')
                        name = name.replace('Â', '')
                        name = name.strip()
                        

                        position = csvs[2].replace('"', '')
                        position = position.replace(' ', '')
                        cost = csvs[3].replace('$', '')
                        cost = cost.replace('\n', '')
                        is_keeper_symbol = csvs[4].replace('"', '')
                        is_keeper = False
                        if("K" in is_keeper_symbol):
                            is_keeper = True
                
                        position = position.replace('"', '')

                        name = normalize_name(name)

                        p = allPlayers.get(name)

                        if p is not None:
                            draftee = allPlayers[name]
                            draftee.set_2019_draft(int(cost), team_name, is_keeper)                       
                            draftedPlayers.append(draftee)
                        
                        

            team = TeamDraft(team_name, draftedPlayers)
            draftedTeams.append(team)
            draftedPlayers = list()

    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\airyards_2020.csv") as f:
        lines = f.readlines()
        team_name = ''
        for l in lines:
            if("full_name" not in l):
                csvs = l.split(',')
                player_name = csvs[1].replace('"', '').replace('*+', '').replace('*', '')
                player_position = csvs[2].replace('"', '')
                player_team = csvs[3].replace('"', '')
                player_air_yards = csvs[7].replace('"', '')
                player_tds = csvs[9].replace('"', '')
                player_name = normalize_name(player_name)
                p = allPlayers.get(player_name)
                if p is not None:
                    airYards_player = allPlayers[player_name]
                    airYards_player.set_ay(float(player_air_yards), 0)
                    airYards_player.set_tds(int(player_tds))
                    allPlayers[player_name] = airYards_player            


    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\runningback_workload.csv") as f:
        lines = f.readlines()
        for l in lines:
            if("Name" not in l):
                l = re.sub(r'(?!(([^"]*"){2})*[^"]*$),', "", l)
                csvs = l.split(',')
                player_name = csvs[0].replace('"', '').replace('*+', '').replace('*', '')
                player_team = csvs[1].replace('"', '')    
                player_position = csvs[2].replace('"', '')
                player_rush_attemps = csvs[4].replace('"', '')
                player_ypa = csvs[5].replace('"', '')
                player_td = csvs[6].replace('"', '')
                player_name = normalize_name(player_name)
                p = allPlayers.get(player_name)
                if p is not None:
                    rush_player = allPlayers[player_name]
                    rush_player.set_rush_yards(float(player_rush_attemps), float(player_ypa))
                    rush_player.add_tds(int(player_td))
                    allPlayers[player_name] = rush_player            

    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\2021_keepers.csv") as f:
        lines = f.readlines()
        for l in lines:
            csvs = l.split(",")
            keeper_name = csvs[1].replace('"', '')
            keeper_name = normalize_name(keeper_name)

            p = allPlayers.get(keeper_name)
            if p is not None:
                keeper_player = allPlayers[keeper_name]
                keeper_player.set_2020_is_keeper(True)
                allPlayers[keeper_name] = keeper_player

    #with open(r"C:\Users\patri\Google Drive\Fantasy Football\2020\2020_adp.csv") as f:
    #    lines = f.readlines()
    #    for l in lines:
    #        csvs = l.split(",")
    #        adp_name = csvs[0].replace('"', '')
    #        adp = csvs[13].replace('"', '')
    #        p = allPlayers.get(adp_name)
    #        if p is not None:
    #            adp_player = allPlayers[adp_name]
    #            adp_player.set_adp(adp)
    #            allPlayers[adp_name] = adp_player

    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2021\notes.csv") as f:
        lines = f.readlines()
        for l in lines:
            csvs = l.split(",")
            note_player_name = csvs[0]
            note_player_note = csvs[1].replace('\n', '')
            note_player = allPlayers[note_player_name]
            note_player.set_note(note_player_note)            
            notes[note_player_name] = note_player_note
        
    for k,v in allPlayers.items():
        note = notes.get(k)
        if note is not None:
            note_player = allPlayers[k]
            note_player.set_note(note)            
    
    with open(r"C:\Users\patri\Google Drive\Fantasy Football\2020\notes.csv", 'w') as f:
        for key in notes:
            f.writelines('%s,%s\n' % (key, notes[key]))
        
    
    json_string = "["

    for k,v in allPlayers.items():
        p = allPlayers[k]
        #json_string += '{"player_name" : "%s" , "nfl_team" : "%s" , "position" : "%s" , "adp" : %s , "cost" : %d , "drafted_by" : "%s" , "is_2019_keeper" : "%s", "is_2020_keeper" : "%s", "air_yards" : "%s" , "yards_per_carry" : "%s" , "rush_attempts" : "%s" , "TDs" : %s, "note": "%s"  , "is_available" : true},' % (p.player_name.replace('\n', ''), p.team, p.position, p.adp, p.cost, p.drafted_team.replace(' ', '').replace('\n', ''), p.is_2019_keeper, p.is_2020_keeper, p.ay, p.ypa_rush, p.rush_attempts, p.tds, p.note)
        json_string += '{"player_name" : "%s" , "nfl_team" : "%s" , "position" : "%s" , "adp" : %s , "cost" : %d , "drafted_by" : "%s", "is_2020_keeper" : "%s" , "air_yards" : "%s" , "rush_attempts" : "%s", "yards_per_carry" : "%s", "TDs" : %s, "note": "%s"  , "is_available" : true },' % (p.player_name.replace('\n', ''), p.team, p.position, p.adp, p.cost, p.drafted_team.replace(' ', '').replace('\n', ''),  p.is_2020_keeper, p.ay, p.rush_attempts, p.ypa_rush, p.tds, p.note)

    json_string = json_string[:-1]
    json_string += "]"

    with open(r"C:\Users\patri\Documents\Sources\fantasy-football-client\client\src\data_2021.json", 'w', encoding='utf-8') as f:
        json.dump(json_string, f, ensure_ascii=False, indent=4)
    print(json_string)
    create_note()


def create_note():
    print("Add Note - {Player Name}, {note}")
    player_name_note = input("Player Name:")
    print("Player: " + player_name_note)
    player_note = input("Enter Note: ")
    print("Note Saved: " + player_name_note + " - " + player_note)
    notes[player_name_note] = player_note
    run()
    

run()


