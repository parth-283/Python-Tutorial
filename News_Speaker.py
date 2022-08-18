import requests
import json

# Exxercise9
API_KEY = '4665a53e142c4022abe41ddf551ba156'
# URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=4665a53e142c4022abe41ddf551ba156 '
URL = 'https://newsapi.org/v2/top-headlines?Sources=the-times-of-india&apiKey=4665a53e142c4022abe41ddf551ba156'


def speak(Str):
    from win32com.client import Dispatch
    Speak = Dispatch("SAPI.SpVoice")
    Speak.Speak(Str)


if __name__ == '__main__':

    r = requests.get(URL)
    jsComp = json.loads(r.text)

    for articles in jsComp['articles']:
        for key, value in articles.items():
            print(key, " => ", value, "\n\n")
            if key == 'url':
                pass
            elif key == 'urlToImage':
                pass
            else:
                speak(key)
                speak(value)
