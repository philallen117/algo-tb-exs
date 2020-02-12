# Uses python3
import sys
from collections import namedtuple


Event = namedtuple('Event', ['x', 'type', 'index'])


def fast_count_segments(starts, ends, points):
    count = [None] * len(points)
    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range(len(points)):
        events.append(Event(points[i], 'p', i))
    events.sorted()
    number_of_segments = 0
    for e in events:
        if e.type == 'l':
            number_of_segments += 1
        elif e.type == 'r':
            number_of_segments -= 1
        elif e.type == 'p':
            count[e.index] = number_of_segments
    return count


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
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
