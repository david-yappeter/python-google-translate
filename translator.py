import requests
from lang.languageList import *

def Translate(fromLan, toLan, word):
    URL = "http://localhost:3000/translate"
    params = {"before": fromLan, "after": toLan, "word": word}

    r = requests.get(url = URL, params = params)

    return r.json()["translated"]

print("Python x Nodejs Translator API")
print("------------------------------")
print("Code   |  Language")
print("==================")

for key, val in ListLanguage.items():
    print("%-7s| %s\n" %(key, val), end="", sep="")

while(1):
    beforeLan = input("Before code : ").strip().lower()
    if beforeLan in ListLanguage.keys():
        break
    print("Not Valid Country Code")
    
while(1):
    afterLan = input("After code : ").strip().lower()
    if afterLan in ListLanguage.keys():
        break
    print("Not Valid Country Code")
    
word = input("Word : ")

print("Translate Result :", Translate(beforeLan, afterLan, word))

