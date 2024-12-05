import numpy as np
import pandas as pd

data_test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("input.txt", "r") as fh:
    data_real = fh.read()

data = data_real

data = [d.split(" ") for d in data.split("\n")]


arr = pd.DataFrame(data).values.astype(float)


def replace_second_false_if_adjacent(arr):
    """
    Replaces the second False with True if there are exactly two adjacent False values.
    """
    false_indices = np.where(arr == False)[0]
    if len(false_indices) == 2 and false_indices[1] - false_indices[0] == 1:
        arr[false_indices[1]] = True
    return arr


def replace_first_false_if_adjacent(arr):
    """
    Replaces the first False with True if there are exactly two adjacent False values.
    """
    false_indices = np.where(arr == False)[0]
    if len(false_indices) == 2 and false_indices[1] - false_indices[0] == 1:
        arr[false_indices[0]] = True
    return arr


def check_is_safe(arrr):
    arrr = arrr[~np.isnan(arrr)]
    diff = arrr[1:] - arrr[:-1]

    if np.nan in arrr:
        breakpoint()

    if sum(diff > 0) == len(diff):
        return diff.max() <= 3
    elif sum(diff < 0) == len(diff):
        return diff.min() >= -3
    else:
        return False


def check_is_safe_tolerance(arrr):
    arrr = arrr[~np.isnan(arrr)]
    diff = arrr[1:] - arrr[:-1]

    if np.nan in arrr:
        breakpoint()

    if sum(diff > 0) == len(diff):
        return diff.max() <= 3
    elif sum(diff > 0) >= len(diff) - 2:
        # return sum(diff <= 3) >= len(diff) - 1
        mask = (diff <= 3) & (diff > 0)
        mask_arrr = np.concatenate(([True], mask))
        if len(arrr[mask_arrr]) >= len(arrr) - 2:
            return (
                check_is_safe(
                    arrr[
                        np.concatenate(([True], replace_first_false_if_adjacent(mask)))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate((replace_first_false_if_adjacent(mask), [True]))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate(([True], replace_second_false_if_adjacent(mask)))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate((replace_second_false_if_adjacent(mask), [True]))
                    ]
                )
            )
        else:
            return False

    elif sum(diff < 0) == len(diff):
        return diff.min() >= -3
    elif sum(diff < 0) >= len(diff) - 2:
        mask = (diff >= -3) & (diff < 0)
        mask_arrr = np.concatenate(([True], mask))
        if len(arrr[mask_arrr]) >= len(arrr) - 2:
            return (
                check_is_safe(
                    arrr[
                        np.concatenate(([True], replace_first_false_if_adjacent(mask)))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate((replace_first_false_if_adjacent(mask), [True]))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate(([True], replace_second_false_if_adjacent(mask)))
                    ]
                )
                or check_is_safe(
                    arrr[
                        np.concatenate((replace_second_false_if_adjacent(mask), [True]))
                    ]
                )
            )
        else:
            return False
    else:
        return False


# arr = np.array(data_test).astype(int)

check_is_safe_tolerance(np.array([1000, 5, 7, 8, 9, 10]))

# assert False
results = []
for i in range(len(arr)):
    r = check_is_safe_tolerance(arr[i])
    if r and False:
        print(
            f"{i} - sum diff < 0 {sum((arr[i][1:] - arr[i][:-1]) < 0)} > 0 {sum((arr[i][1:] - arr[i][:-1]) > 0)}"
        )
    results.append(r)
print(sum(np.array(results)))
breakpoint()

results = []
for i in range(len(arr)):
    success_iter = check_is_safe(arr[i])
    for j in range(len(arr[i])):
        result = check_is_safe(np.delete(arr[i], j))
        if result:
            success_iter = True
    results.append(success_iter)

print(sum(np.array(results)))
