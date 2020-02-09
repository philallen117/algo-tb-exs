# Uses python3
import sys
from collections import namedtuple

class Ix(namedtuple('Ix', ['ix', 'p'])):
    def __eq__(self, other): self.p == other.p

class IxLeft(Ix):
    def __lt__(self, other): return self.p < other.p
    def __le__(self, other): return self.p <= other.p

class IxRight(Ix):
    def __lt__(self, other): return self.p > other.p
    def __le__(self, other): return self.p >= other.p

def bounded(p, a):
    # a assumed sort; return subset (i.e. prefix) of a less than or equal p
    n = len(a)
    left, right = 0, n
    while True:
        if left == right:
            if left < n and a[left] <= p: left = left + 1
            break
        else: # length at least 2
            mid = (left + right) // 2
            amid = a[mid]
            if amid <= p:
                left = mid + 1
                continue
            else: # p < amid
                right = mid
                continue
    return a[:left]

def segs(ls_ordered, rs_ordered, p):
    # Returns indexes in original list
    left_segs = bounded(IxLeft(0, p), ls_ordered)
    left_segs = map(lambda p: p.ix, left_segs)
    right_segs = bounded(IxRight(0, p), rs_ordered)
    right_segs = map(lambda p: p.ix, right_segs)
    return set(left_segs) & set(right_segs)

def fast_count_segments(ls, rs, points):
    n = len(ls)
    ixs = range(0, n)
    ls_ordered = list(map(lambda ix, p: IxLeft(ix, p), ixs, ls))
    ls_ordered.sort()
    rs_ordered = list(map(lambda ix, p: IxRight(ix, p), ixs, rs))
    rs_ordered.sort()
    cnts = []
    for p in points:
        cnts.append(len(segs(ls_ordered, rs_ordered, p)))
    return cnts

def naive_count_segments(ls, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(ls)):
            if ls[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    ls = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(ls, ends, points)
    for x in cnt:
        print(x, end=' ')
