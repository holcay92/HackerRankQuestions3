if __name__ == '__main__':
    N = int(input())
    result = [4, 5]
    for _ in range(N):
        operation = input().split()
        if operation[0] == "print": print(result)
        if operation[0] == "append": result.append(int(operation[1]))
        if operation[0] == "insert": result.insert(int(operation[1]), int(operation[2]))
        if operation[0] == "remove": result.remove(int(operation[1]))
        if operation[0] == "pop": result.pop()
        if operation[0] == "sort": result.sort()
        if operation[0] == "reverse": result.reverse()



