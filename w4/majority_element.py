# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right + 1) // 2
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

def get_majority_element1(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
