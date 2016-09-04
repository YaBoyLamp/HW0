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
        return self.queue == other.queue
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return 'Front ' + str(self.queue)

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
        return self.stack == other.stack
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return 'Top ' + str([e for e in reversed(self.stack)])

## Problem 4

def add_position_iter(lst, number_from=0):
    l = lst[:]
    for i in range(0, len(lst)):
        l[i] += i + number_from
    return l

def add_position_recur(lst, number_from=0):
    if lst == []:
        return []
    l = [lst[0] + number_from]
    return l + add_position_recur(lst[1:], number_from=number_from + 1)


def add_position_map(lst, number_from=0):
    return map(lambda x: x[0] + x[1] + number_from, enumerate(lst))

## Problem 5

def remove_course(roster, student, course):
    return roster[student].discard(course)

## Problem 6

def copy_remove_course(roster, student, course):
    new_roster = dict()
    for e in roster.items():
        new_roster[e[0]] = e[1].copy()
    remove_course(new_roster, student, course)
    return new_roster

