# python3
import sys


def compute_min_refills(distance, tank, stops):
    assert stops[-1] < distance, "Distance before last fill stop"
    fills = []
    last_fill = 0 # distance, start with full tank
    last_s_tried = 0 # distance, not position
    stops.append(distance) # add distance as a stop
    for s in stops:
        # travelled < distance
        # travelled < (len(fills) + 1) * tank
        # used <= tank
        # last_fill + used = s_before
        if s - last_fill <= tank:
            last_s_tried = s
            # don't add fill yet ... might be able to get further
            continue
        else: 
            # cannot get here on current tank
            if last_s_tried > last_fill:
                # add a fill at last_s_tried and check again
                fills.append(last_s_tried)
                last_fill = last_s_tried
                if s - last_fill <= tank:
                    # can get to s from additional fill ... but don't fill yet
                    last_s_tried = s
                else:
                    # screwed ... cannot get to s
                    return -1
            else:
                # no reachable stops since last fill, including s
                return -1
    # got here means reached distance (last stop)
    return len(fills)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
