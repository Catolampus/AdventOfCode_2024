def main() -> int:
    save = 0
    with open("t1_tsk.txt") as f:
        for line in f:
            is_save = True
            row = [int(i) for i in line.split(" ")]
            pairs = [[ch, row[idx + 1]] for idx, ch in enumerate(row[:-1])]
            if pairs[0][0] - pairs[0][1] < 0:
                is_positive_sign = False
            elif pairs[0][0] - pairs[0][1] > 0:
                is_positive_sign = True
            else:
                continue
            for pair in pairs:
                diff = pair[0] - pair[1]
                if diff > 0:
                    diff_sign_positive = True
                else:
                    diff_sign_positive = False
                if abs(diff) > 3 or abs(diff) == 0:
                    is_save = False
                    break
                if is_positive_sign != diff_sign_positive:
                    is_save = False
                    break
            save += is_save
    return save


if __name__ == "__main__":
    print(main())
