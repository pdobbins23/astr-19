import math


def main():
    points = []
    x = 0

    # compute values
    while x < (2 * math.pi):
        points.append((x, math.sin(x)))
        x += (2 * math.pi) / 1000

    print(f"Computed {len(points)} entries:")
    print("x   |   sin(x)")
    print("--------------")

    # print out all values
    for point in points:
        print(f"{point[0]}   |   {math.sin(point[1])}")


if __name__ == "__main__":
    main()
