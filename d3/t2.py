import re


def main() -> int:
    with open("t1.txt", "r") as f:
        file = f.read().strip()
    res = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", file)
    flag = True
    total = 0
    for val in res:
        if "don" in val:
            flag = False
            continue
        if "do" in val:
            flag = True
            continue
        if flag and "mul" in val:
            values = re.search(r"mul\((\d+),(\d+)\)", val)
            total += int(values.group(1)) * int(values.group(2))
    return total


if __name__ == "__main__":
    print(main())
