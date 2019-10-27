# python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def intersect(seg1, seg2):
    lb = max(seg1.start, seg2.start)
    ub = min(seg1.end, seg2.end)
    if lb <= ub:
        return Segment(lb, ub)
    else:
        return None

def optimal_points(segments):
    assert len(segments) > 0, "Segments was empty"
    zones = []
    zones.append(segments[0])
    def update_zones(seg):
        found = False
        for z in zones:
            cand = intersect(z, seg)
            if cand != None:
                found = True
                zones.remove(z)
                zones.append(cand)
        if not found:
            zones.append(z)
    for seg in segments[1:]:
        update_zones(seg)
    points = [z.start for z in zones]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
