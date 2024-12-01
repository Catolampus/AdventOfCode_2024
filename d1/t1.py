def main() -> None:
    l1 = []
    l2 = []
    with open("t1_tsk.txt", "r") as f:
        for line in f:
            v1, v2 = [int(v) for v in line.strip().split("  ")]
            l1.append(v1)
            l2.append(v2)
    print(t1(l1, l2))
    return


def t1(l1: list[int], l2: list[int]) -> int:
    l1.sort()
    l2.sort()
    res = 0
    for v1, v2 in zip(l1, l2):
        res += abs(v1 - v2)
    return res


if __name__ == "__main__":
    main()
