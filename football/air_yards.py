'''import urllib.request
import urllib.parse
'''
import requests
from bs4 import BeautifulSoup

'''url = 'https://fantasy.espn.com/football/league/draftrecap?seasonId=2019&leagueId=113756'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))

page = requests.get('https://fantasy.espn.com/football/league/draftrecap?seasonId=2019&leagueId=113756')
soup = BeautifulSoup(page.text, 'html.parser')

draft_recap_tables = soup.find(class_='draftRecapTable')

print(page.text)
'''
