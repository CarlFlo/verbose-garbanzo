from os import system
import requests
import datetime

min = 0
max = 500
cc = {}


def farm():

    timeLeft = 0.0

    for i in range(min, max):
        startTime = datetime.datetime.now()

        percentage = (i/max)*100

        pro = str.format("{0:.2f} {1} done {2:.1f} seconds left",
                         percentage, '%', (timeLeft*(max-i)))

        system("title " + pro)

        reqURL = str.format(
            "http://kulturarvsdata.se/shm/object/jsonld/{}", str(i))

        r = requests.get(reqURL)

        if (r.status_code != 200):
            addToMap("error")
            continue

        data = r.json()

        line = ""

        for j in range(0, 30):
            try:
                line = data["@graph"][j]["itemLicense"]
            except:
                pass

        if(len(line) == 0):
            addToMap("no data")
            continue

        line = line.split("#")[1]

        addToMap(line)
        endTime = datetime.datetime.now()
        timeLeft = (endTime-startTime).total_seconds()


def addToMap(_key):
    try:
        cc[_key] += 1
    except:
        cc[_key] = 1


def showResult():
    for key in cc:
        print(key, ":", cc[key])


system("cls")
farm()
showResult()
