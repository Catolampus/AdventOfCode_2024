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
    word = np.array(object=["X", "M", "A", "S"])
    # x-wise
    window = (x.shape[0], 4)
    sub_matrices = rolling_window(x, window).reshape(-1, x.shape[0], 4)
    for win in sub_matrices:
        mxs = [
            win,
            np.fliplr(win),
        ]
        total = np.vstack(mxs)
        r = sum(np.all(total == word, axis=1))
        res += r
    # y-wise
    window = (4, x.shape[1])
    sub_matrices = rolling_window(x, window).reshape(-1, 4, x.shape[1])
    for win in sub_matrices:
        mxs = [
            win.T,
            np.fliplr(win.T),
        ]
        total = np.vstack(mxs)
        r = sum(np.all(total == word, axis=1))
        res += r
    # diag
    window = (4, 4)
    sub_matrices = rolling_window(x, window).reshape(-1, 4, 4)
    for win in sub_matrices:
        diags = np.array(
            [
                np.diag(win),
                np.diag(win)[::-1],
                np.diag(np.fliplr(win)),
                np.diag(np.fliplr(win))[::-1],
            ]
        )
        r = sum(np.all(diags == word, axis=1))
        res += r
    return res


if __name__ == "__main__":
    print(main())
