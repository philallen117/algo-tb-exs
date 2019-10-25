# python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points1(segments):
    assert len(segments) > 0, "Segments was empty"
    def intersect(seg1, seg2):
        lb = max(seg1.start, seg2.start)
        ub = min(seg1.end, seg2.end)
        if lb <= ub:
            return Segment(lb, ub)
        else:
            return None
    points = []
    current = segments[0]
    for s in segments[1:]:
        inter = intersect(current, s)
        if inter == None:
            points.append(current.start)
            current = s
        else:
            current = inter
    points.append(current.start)
    return points

def optimal_points(segments):
    return []

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
