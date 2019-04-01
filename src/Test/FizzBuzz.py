data = {3: "Fizz", 5: "Buzz"}


def FizzBuzz(values):
    for i in range(1, 101):
        didFizzBuzz = False
        for elem in values:
            if i % elem == 0:
                print(data[elem], end='')
                didFizzBuzz = True

        if not didFizzBuzz:
            print(i, end='')

        print()


FizzBuzz(data)
