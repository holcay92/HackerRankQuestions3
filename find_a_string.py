def count_substring(string, sub_string):
    str_length = len(string)
    sub_str_length = len(sub_string)
    count: int = 0
    for i in range(0, str_length - sub_str_length + 1):
        if string[i:i+sub_str_length] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)