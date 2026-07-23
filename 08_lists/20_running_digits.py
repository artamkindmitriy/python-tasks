import math

def cyclic_shift(lst, k):
    n = len(lst)
    if n == 0:
        return lst

    k = k % n
    if k == 0:
        return lst

    num_cycles = math.gcd(n, k)

    for start in range(num_cycles):
        temp = lst[start]
        current = start

        while True:
            next_idx = (current + k) % n
            if next_idx == start:
                lst[current] = temp
                break
            lst[current] = lst[next_idx]
            current = next_idx

    return lst

print(cyclic_shift([1, 2, 3, 4, 5], 1))
print(cyclic_shift([1, 4, -3, 0, 10], 3))