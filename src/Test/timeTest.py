import datetime, time

def Test():
    while True:
        startTime = datetime.datetime.now()
        time.sleep(.1)
        endTime = datetime.datetime.now()

        print((endTime-startTime).total_seconds())

print("Hej")
Test()