import json, requests

apiKey = "x-api=test"


def requestData():

    # Make a get request with the parameters.
    r = requests.get("https://www.google.se")

    if (r.status_code != 200):
        return
    
    print(r.content)

    #r=requests.options("https://www.google.se")

requestData()





