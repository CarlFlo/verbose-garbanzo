from os import system
import requests

min = 1
max = 100
cc = {}

def farm():
    for i in range(min,max):

        pro = str.format("{0:.2f} precent of porn found", (i/max)*100)

        system("title " + pro)

        reqURL = str.format("http://kulturarvsdata.se/shm/object/jsonld/{}", str(i))

        r = requests.get(reqURL)

        if (r.status_code != 200):
            addToMap("Error")
            continue

        data = r.json()

        line = ""

        for j in range(0,30):
            try:
                line = data["@graph"][j]["itemLicense"]
            except:
                pass

        if(len(line) == 0):
            addToMap("No length")
            continue

        line = line.split("#")[1]

        addToMap(line)


def addToMap(_key):
    try:
        cc[_key] = cc[_key]+1
    except:
        cc[_key] = 1

def showResult():
    for key in cc:
        print(key,":", cc[key])


system("cls")
farm()
showResult()
