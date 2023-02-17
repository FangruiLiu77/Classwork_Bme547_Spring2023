def para_entry():
    print("Enter two tuples, (x1, y1), (x2, y2)")

    first = input("Enter the first tuple (split in ','): ")
    second = input("Enter the second tuple (split in ','):")

    print("Enter the point that you want to check if it's in this line.")
    third = input("Enter the third tuple (split in ','): ")

    first = tuple(float(x) for x in first.split(","))
    second = tuple(float(x) for x in second.split(","))
    third = tuple(float(x) for x in third.split(","))

    add_inputs = [first, second, third]
    result = y_checker(add_inputs)

    if result is True:
        print(
            "The third point is on the line defined by the first two points."
            )
    else:
        print(
            "The third point is NOT on the line defined \
            by the first two points"
            )


def y_checker(inputs):
    first = inputs[0]
    second = inputs[1]
    third = inputs[2]

    a = (first[1] - second[1]) / (first[0] - second[0])
    b = first[1] - a*first[0]

    y = a*third[0] + b

    if third[1] == y:
        return True
    else:
        return False


if __name__ == "__main__":
    para_entry()
