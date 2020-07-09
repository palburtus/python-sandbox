import nflgame

games = nflgame.games(2013, week=1)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(5):
    print( '%s' % p.rushing_att + ' carries for %s yards and' % p.rushing_yds + ' and TDs: %s' % p.rushing_tds)