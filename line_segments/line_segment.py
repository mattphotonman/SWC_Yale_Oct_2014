"""
Determines which line segment(s) a point
belongs to.
"""

def line_segs(point):
    """
    Function to determine which line
    segment(s) a point belong to.
    """
    point = float(point)
    
    result = set()

    # If the point is in [0,1]
    # then it is in segment 'A'
    if point >= 0 and point <= 1:
        result.add('A')
    
    # If the point is in [0.8, 1.8]
    # the it is in segment 'B'
    if point >= 0.8 and point <= 1.8:
        result.add('B')

    # If the point is in [1.6, 2.6]
    # the it is in segment 'C'
    if point >= 1.6 and point <= 2.6:
        result.add('C')
    
    return result

def in_line_seg(point, seg):
    """
    Returns True if the point is in the
    line segment, otherwise returns
    False.
    """
    return seg in line_segs(point)


# Make a function that returns
# the line segments that a point
# does NOT belong to.
# 
# Hint:  Write some tests first.
#
# Hint 2: Use some of the functions
# we already wrote.


print line_segs(0.1)
print line_segs(0.8)
print line_segs(-1)
