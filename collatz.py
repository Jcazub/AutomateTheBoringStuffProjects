def getUserInput():
    while True:
        try:
            return int(input())
        except ValueError:
            print('Please input a number')


def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2;
    else:
        print(str((3 * number) + 1))
        return (3 * number) + 1


number = getUserInput()
count = 0;
while number != 1:
    count += 1
    number = collatz(number)