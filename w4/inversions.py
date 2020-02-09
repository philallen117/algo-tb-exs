# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    def merge_sort(l):
    if right - left <= 1:
        return l, 0
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

        return l
    def merge(a, b):
        return 5
    number_of_inversions = 0
     number_of_inversions += merge_count(merge_sort(a), merge_sort(b))
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
