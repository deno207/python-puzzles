def sum_even(input_nums: list[int]) -> int:
    total = 0
    for number in input_nums:
        # check if number is divisible by 2, and therefor even
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
