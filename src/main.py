import Animal as a


def main():

    obj2 = a.Dog("Dog")
    obj3 = a.Horse("Horse")

    print("================")
    obj2.speak()
    obj3.speak()

    obj3.dies()

main()
