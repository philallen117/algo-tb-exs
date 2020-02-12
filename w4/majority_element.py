# Uses python3
import sys


class Counter(dict):
    def __missing__(self, key):
        return 0


def get_majority_element(votes, left=0, right=0):
    target = len(votes) // 2 + 1
    count = Counter()
    for vote in votes:
        count[vote] += 1
    for vote, val in count.items():
        if val >= target:
            return vote
    return -1


def get_majority_element1(a, left, right):
    if left == right:
        return -1
    if right == left + 1:
        return a[left]
    # right >= left + 2
    mid = (left + right) // 2
    lme = get_majority_element(a, left, mid)
    rme = get_majority_element(a, mid, right)
    if lme == -1:
        if rme == -1:
            return -1
        else:
            return rme
    else:
        if rme == -1:
            return lme
        else:
            if lme == rme:
                return lme
            else:
                return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
