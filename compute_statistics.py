def compute_mean(array: list) -> float:
    return sum(array) / len(array)

def compute_median(array: list) -> float:
    array = sorted(array)
    if len(array) % 2 == 0:
        return (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
    else:
        return array[len(array) // 2]