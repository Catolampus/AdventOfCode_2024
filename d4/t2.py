import numpy as np


def rolling_window(matrix, window):
    matrix_x, matrix_y = matrix.shape
    strides = (
        matrix.strides[0],  # bytes between rows
        matrix.strides[1],  # bytes between cols
        matrix.strides[0],
        matrix.strides[1],
    )
    windows = np.lib.stride_tricks.as_strided(
        matrix,
        shape=(
            matrix_x - window[0] + 1,
            matrix_y - window[1] + 1,
            window[0],
            window[1],
        ),
        strides=strides,
    )
    return windows


def main() -> int:
    with open("t.txt", "r") as f:
        file = [list(i) for i in f.read().split("\n")[:-1]]
    x = np.array(file)
    res = 0
    window = (3, 3)
    word = np.array(object=["M", "A", "S"])
    sub_matrices = rolling_window(x, window).reshape(-1, 3, 3)
    for win in sub_matrices:
        diags = np.array(
            [
                np.diag(win),
                np.diag(win)[::-1],
                np.diag(np.fliplr(win)),
                np.diag(np.fliplr(win))[::-1],
            ]
        )
        if sum(np.all(diags == word, axis=1)) == 2:
            res += 1
    return res


if __name__ == "__main__":
    print(main())
