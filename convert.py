import json
import requests

apiKey = 'YOUR API KEY'

def getSynonym(word):
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': apiKey})
    if response.status_code == requests.codes.ok:
        resp = json.loads(response.text)
        return resp['synonyms']
    else:
        print("Error:", response.status_code, response.text)

def getSentimentScore(text):
    api_url = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)
    response = requests.get(api_url, headers={'X-Api-Key': apiKey})
    if response.status_code == requests.codes.ok:
        resp = json.loads(response.text)
        return resp['score']
    else:
        print("Error:", response.status_code, response.text)

def replaceWord(word):
    synonyms = getSynonym(word)
    word = word
    score = getSentimentScore(word)
    for synonym in synonyms:
        synonymScore = getSentimentScore(synonym)
        if synonymScore > score:
            word = synonym
            score = synonymScore
    return word

def printTranslation(text, newText):
    print('Original Text: ' + text)
    print('New Text: ' + newText)

def convertText(text):
    wordSplice = text.split()
    textList = []
    for word in wordSplice:
        score = getSentimentScore(word)
        if score < 0.0:
            newWord = replaceWord(word)
            textList.append(newWord)
        else:
            textList.append(word)
    newText = ' '.join(textList)
    printTranslation(text, newText)

# change exmapleText to try different sentences
exampleText = 'this house is disgusting'
convertText(exampleText)
