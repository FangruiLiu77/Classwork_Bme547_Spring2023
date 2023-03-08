def add_two_numbers(a, b):
    answer = a + b

    if type(a) != int or type(b) != int:
        raise TypeError("Cannot send a string.")
    if a < 0 or b < 0:
        raise ValueError("You cannot send a negative"
                         "number to this function.")

    return answer


def main():
    print(add_two_numbers(4, 5))


if __name__ == "__main__":
    main()
