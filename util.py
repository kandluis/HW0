##### Filename: util.py
##### Author: Luis Perez
##### Date: September 10, 2015
##### Email: luisperez@college.harvar.edu

# Note: Modifications and tests for the functions are found in util.py.

import copy
from collections import deque

## Problem 1

def dot(x, y, i, j):
    '''
    Calculates the dot product of the i-th row and the j-th column of
    x and y, respectively. Assumes matrices.
    '''
    return sum([x[i][k] * y[k][j] for k in xrange(len(x[0]))])

def matrix_multiply(x, y):
    '''
    Assumes X,Y are matrices represented as a list of rows,
    where each row is a list of elements. Asserts inputs are
    properly formatted matrices. An empty matrix is not acceptable input.
    Returns the matrix X x Y.
    Asserts error if dimensions do not match.
    '''
    assert len(x) > 0 and len(y) > 0
    xrow, xcol = len(x), len(x[0])
    yrow, ycol = len(y), len(y[0])
    assert xcol == yrow
    return [[dot(x, y, i, j) for j in xrange(ycol)] for i in xrange(xrow)]

## Problem 2, 3

class MyQueue:
    def __init__(self):
        self.q = deque()
    def push(self, val):
        self.q.append(val)
    def pop(self):
        try:
            return self.q.popleft()
        except IndexError:
            return None
    def __eq__(self, other):
        return isinstance(other, MyQueue) and self.q == other.q
    def __ne__(self, other):
        return not isinstance(other, MyQueue) or self.q != other.q
    def __str__(self):
        return "MyQueue (head -> tail):\n %s" % str(self.q)

class MyStack:
    def __init__(self):
        self.s = deque()
    def push(self, val):
        self.s.append(val)
    def pop(self):
        try:
            return self.s.pop()
        except IndexError:
            return None
    def __eq__(self, other):
        return isinstance(other, MyStack) and self.s == other.s
    def __ne__(self, other):
        return not isinstance(other, MyStack) or self.s != other.s
    def __str__(self):
        return "MyStack (bottom -> top):\n %s" % str(self.s)

## Problem 4

def add_position_iter(lst, number_from=0):
    '''
    Essentially iteration, but much leaner than explicit for loops
    '''
    return [val + i + number_from for i,val in enumerate(lst)]

def add_position_recur(lst, number_from=0):
    if (len(lst) == 0):
        return lst
    else:
        return [lst[0] + number_from] + add_position_recur(lst[1:], number_from + 1)

def add_position_map(lst, number_from=0):
    return map(lambda (i, val) : val + i + number_from, enumerate(lst))

## Problem 5

def remove_course(roster, student, course):
    '''
    Raises KeyError if student is not present in roster.
    Only removes coures present in student schedule, otherwise does nothing.
    Mutates roster.
    '''
    roster[student].discard(course)


## Problem 6

def copy_remove_course(roster, student, course):
    new_roster = copy.deepcopy(roster)
    remove_course(new_roster, student, course)
    return new_roster

