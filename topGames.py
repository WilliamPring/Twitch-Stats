import httplib2
from datetime import datetime


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
    """stores original binary data received from http call
    returns name of the file that is stored"""
    savedTime = getTopGameFileName()
    with open(todayFolder + savedTime, mode='wb') as newFile:
        newFile.write(content)
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