import httplib2
from datetime import datetime
import json as simplejson

todayFolder = 'today/'


def getClientId():
    with open('clientId', encoding='utf-8', mode='r') as fileClient:
        clientId = fileClient.read()
    return clientId


def getTopGameFileName():
    """returns string that is topGames[] with current time in it"""
    return 'topGames[{}]'.format(getCurrentTime())+'.json'


def getCurrentTime():
    """returns current time in format %Y%m%d%H%M%S"""
    return datetime.now().strftime('%Y%m%d%H%M%S')


def storeOriginalTopGames(content):
    """store data received from http call
    returns name of the file that is stored 
    also make the python data pretty"""
    savedTime = getTopGameFileName()
    with open(todayFolder + savedTime, mode='w', encoding="utf8") as newFile:
        'To sort it alphabetically put sort_keys=True'
        newFile.write(simplejson.dumps(simplejson.loads(content), indent=4))

    return savedTime



if __name__ == '__main__':
    # preparing variables
    urlGamesTop = 'https://api.twitch.tv/kraken/games/top?limit=100'
    httpHeaderClientId = {'Client-ID': getClientId()}
    httpObj = httplib2.Http()
    # getting content for top games
    response, content = httpObj.request(urlGamesTop, headers=httpHeaderClientId)
    # storing top games and getting name of the file with timestamp for it
    storeOriginalTopGames(content)