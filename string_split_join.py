#haldun halil olcay
def split_and_join(str):
    # write your code here
    str = "-".join(str.split(" "))
    return str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)