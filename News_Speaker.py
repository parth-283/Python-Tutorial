import requests
import json

# Exxercise9
API_KEY = '4665a53e142c4022abe41ddf551ba156'
URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=4665a53e142c4022abe41ddf551ba156 '


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':

    r = requests.get(URL)
    jscomp = json.loads(r.text)

    for articles in jscomp['articles']:
        for key, value in articles.items():
            print(key," => ",value,"\n\n")
            if key == 'url':
                pass
            elif key == 'urlToImage':
                pass
            else:
                speak(key)
                speak(value)
