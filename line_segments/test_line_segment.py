"""
Tests for line_segment.py.
"""

import line_segment
from nose.tools import assert_raises

def test_line_segs():
    assert line_segment.line_segs(0.2) == {'A'}
    assert line_segment.line_segs(0.9) == {'A', 'B'}
    assert line_segment.line_segs(1.5) == {'B'}
    assert line_segment.line_segs(1.7) == {'B', 'C'}
    assert line_segment.line_segs(1.8) == {'B', 'C'}
    assert line_segment.line_segs(1.6) == {'B', 'C'}
    assert line_segment.line_segs(2.8) == set()
    assert line_segment.line_segs(-1) == set()
    assert line_segment.line_segs(2) == {'C'}
    assert line_segment.line_segs(0) == {'A'}
    assert line_segment.line_segs(0.8) == {'A', 'B'}
    assert line_segment.line_segs(1) == {'A', 'B'}
    assert line_segment.line_segs(2.6) == {'C'}
    assert_raises(ValueError, line_segment.line_segs, 'dskfjs')
    assert line_segment.line_segs('1.0') == {'A', 'B'}

def test_in_line_seg():
    assert line_segment.in_line_seg(0.2, 'A') == True
    assert line_segment.in_line_seg(1.9, 'B') == False

def test_not_line_segs():
    assert line_segment.not_line_segs(0.2) == {'B', 'C'}
    assert line_segment.not_line_segs(-1) == {'A', 'B', 'C'}
