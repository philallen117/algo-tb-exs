import pytest
from points_and_segments import *
from segments_utils import *

@pytest.fixture
def data():
    segs =[(1, 4), (4, 4), (5, 8), (7, 10)]
    return Data(segs)

def test_ordering(data):
    ixs = range(0, data.n)
    ls_ordered = list(map(lambda ix, p: IxLeft(ix, p), ixs, data.ls))
    ls_ordered.sort()
    rs_ordered = list(map(lambda ix, p: IxRight(ix, p), ixs, data.rs))
    rs_ordered.sort()
    assert len(ls_ordered) == data.n
