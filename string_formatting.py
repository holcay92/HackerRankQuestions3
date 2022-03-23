def print_formatted(number):
    # your code goes here
    if not 1 <= number <= 99: exit("constrain")
    result = list()
    for i in range(number):
        result.append(i+1)
    hexa_format(number)
    print(result)

def binary_format(number):
    str = ""
    while number != 0:
        if number % 2 == 1:
            str += "1"
        else: str += "0"
        number = int(number / 2)
        print(number)
    str = str[::-1]
    return print(str)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
