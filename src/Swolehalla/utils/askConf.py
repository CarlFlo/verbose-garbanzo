def askConf(msg):

    print(msg)

    ans = input()
    if ans in ["y", "Y", "yes", "Yes"]:
        return True
    else:
        return False

