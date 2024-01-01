def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    total = num_one + num_two
    if total < 50:
        return total
    else:
        return None


if __name__ == "__main__":
    print(sum_if_less_than_fifty(20, 25))
