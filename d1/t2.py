from collections import defaultdict


def main() -> None:
    l1 = defaultdict(int)
    l2 = defaultdict(int)
    with open("t1_tsk.txt", "r") as f:
        for line in f:
            v1, v2 = [int(v) for v in line.strip().split("  ")]
            l1[v1] += 1
            l2[v2] += 1
    print(t2(l1, l2))
    return


def t2(l1: dict[int, int], l2: dict[int, int]) -> int:
    res = 0
    for key, val in l1.items():
        res += key * l2[key]
    return res


if __name__ == "__main__":
    main()
