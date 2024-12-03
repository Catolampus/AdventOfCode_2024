import re


def main() -> int:
    with open("t1.txt", "r") as f:
        file = f.read().strip()
    res = re.findall(r"mul\((\d+),(\d+)\)", file)
    return sum([int(i[0]) * int(i[1]) for i in res])


if __name__ == "__main__":
    print(main())
