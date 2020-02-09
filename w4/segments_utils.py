from points_and_segments import Ix, IxLeft, IxRight

class Data:
    def __init__(self, segs):
        xsegs = list(zip(*segs))
        self.ls = xsegs[0]
        self.rs = xsegs[1]
        self.n = len(self.ls)
        ixs = range(0, self.n)
        self.ls_ordered = list(map(lambda ix, p: IxLeft(ix, p), ixs, self.ls))
        self.ls_ordered.sort()
        self.rs_ordered = list(map(lambda ix, p: IxRight(ix, p), ixs, self.rs))
        self.rs_ordered.sort()
