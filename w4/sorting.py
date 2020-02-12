# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


# single pass attempt ... maybe later
def partition3a(a, l, r):
    x = a[l]
    j, w = l, 0
    for i in range(l+1, r+1):
        if a[i] == x:
            w += 1
            a[j+w], a[i] = a[i], a[j+w]
        elif a[i] < x:
            j += 1
            a[j], a[j+w], a[i] = a[i], a[j], a[j+w]
    return j, j+w


# say x = a[l] initially
# permutes a in place and returns s, e where l <= s <= e <= r
# a[l] .. a[s-1] < x and a[s] .. a[e] == x and a[e+1] .. a[r] > x
def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    # a[j] == x and a[l] .. a[j-1] <= x
    k = j
    # a[k] .. a[j] = x
    for i in range(j - 1, l - 1, -1):
        if a[i] == x:
            k -= 1
            if i != k:
                a[i], a[k] = a[k], a[i]
            # invariant a[k] .. a[j] = x and a[i] .. a[k-1] < x
    # a[k] .. a[j] = x and a[l] .. a[k-1] < x
    return k, j


# l, r are inclusive and 0-based
def randomized_quick_sort(a, l, r):
    if l >= r:  # noqa: E741
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    s, e = partition3(a, l, r)
    randomized_quick_sort(a, l, s - 1)
    randomized_quick_sort(a, e + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
