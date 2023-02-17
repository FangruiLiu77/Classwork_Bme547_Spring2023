def para_entry():
    print("Enter two tuples, (x1, y1), (x2, y2)")

    first = input("Enter the first tuple (split in ','): ")
    second = input("Enter the second tuple (split in ','):")
    x = input("Enter the x: ")
    first = tuple(float(x) for x in first.split(","))
    second = tuple(float(x) for x in second.split(","))
    x = float(x)

    inputs = [first, second, x]
    y = y_finder(inputs)


def y_finder(inputs):
    first = inputs[0]
    second = inputs[1]
    x = inputs[2]

    a = (first[1] - second[1]) / (first[0] - second[0])
    b = first[1] - a*first[0]

    y = a*x + b
    return y


if __name__ == "__main__":
    para_entry()
