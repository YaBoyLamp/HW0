##### Filename: util.py
##### Author: {your name}
##### Date: {current date}
##### Email: {your email}

import copy
from collections import deque

## Problem 1

def matrix_multiply(x, y):
    mm = []
    for i in range(0,len(x)):
        row = []
        for j in range(0,len(y)):
            sum = 0
            for k in range(0,len(x[i])):
                sum += x[i][k] * y[k][j]
            row.append(sum)
        mm.append(row)
    return mm



## Problem 2, 3

class MyQueue:
    def __init__(self):
        self.queue = []
    def push(self, val):
        self.queue.append(val)
    def pop(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            self.queue = self.queue[1:]
            return val
        return None
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __str__(self):
        pass

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if len(self.stack) > 0:
            val = self.stack[len(self.stack) - 1]
            self.stack = self.stack[:len(self.stack) - 1]
            return val
        return None
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __str__(self):
        pass

## Problem 4

def add_position_iter(lst, number_from=0):
    pass

def add_position_recur(lst, number_from=0):
    pass

def add_position_map(lst, number_from=0):
    pass

## Problem 5

def remove_course(roster, student, course):
    pass

## Problem 6

def copy_remove_course(roster, student, course):
    pass

