def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    filtered_list = []
    for string in input_strs:
        # if find returns 0 or higher, than an 'a' was found
        if string.find("a") >= 0:
            filtered_list.append(string)
    return filtered_list


if __name__ == '__main__':
    print(filter_strings_containing_a(["apple", "banana", "cherry", "data"]))
