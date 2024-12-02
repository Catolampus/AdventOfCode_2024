def _get_pairs(row) -> list[list[int]]:
    return [[ch, row[idx + 1]] for idx, ch in enumerate(row[:-1])]


def _get_trend(pairs) -> bool | None:
    if pairs[0][0] - pairs[0][1] < 0:
        return False
    elif pairs[0][0] - pairs[0][1] > 0:
        return True
    else:
        return


def checkup(pairs, is_positive_sign) -> tuple[int, bool]:
    is_save = True
    for idx, pair in enumerate(pairs):
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
    return idx, is_save


def brutforce_checkup(base_row) -> bool:
    for idx in range(len(base_row)):
        row = base_row[:]
        row.pop(idx)
        pairs = _get_pairs(row)
        is_positive_sign = _get_trend(pairs)
        idx, is_save = checkup(pairs, is_positive_sign)
        if is_save:
            return True
    return False


def main() -> int:
    save = 0
    with open("t1_tsk.txt") as f:
        for line in f:
            row = [int(i) for i in line.split(" ")]
            _base_row = row[:]
            pairs = _get_pairs(row)
            is_positive_sign = _get_trend(pairs)
            idx, is_save = checkup(pairs, is_positive_sign)
            if is_save:
                save += 1
                continue
            is_new_save = brutforce_checkup(_base_row)
            if is_new_save:
                save += 1
    return save


if __name__ == "__main__":
    print(main())
