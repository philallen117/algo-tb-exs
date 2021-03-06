# Uses python3
import sys

def binary_search_r(a, x):
    def aux(a, left, right):
        if left == right:
            return -1
        else:
            mid = (left + right) // 2
            amid = a[mid]
            if amid == x:
                return mid
            elif x > amid:
                return aux(a, mid + 1, right)
            else:
                return aux(a, left, mid)
    return aux(a, 0, len(a))
        
def binary_search(a, x):
    left, right = 0, len(a)
    while True:
        if left == right:
            return -1
        else:
            mid = (left + right) // 2
            amid = a[mid]
            if amid == x:
                return mid 
            elif x > amid:
                left = mid + 1
                continue
            else:
                right = mid
                continue

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
