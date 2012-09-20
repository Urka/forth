# -*- coding: utf-8 -*-

from __future__ import print_function

import math
import sys
import unittest
import re

COMMANDS = {}

def register_command(func):
    if func.__name__ not in ['wrraper']:
        COMMANDS[func.__name__] = func
    def wrraper(self, *args, **kwargs):
        return func(self, *args, **kwargs)
    return wrraper

class Stack(object):

    _s = []

    @register_command
    def push(self, number):
        self._s.append(number)

    @register_command    
    def pop(self):
        return self._s.pop()

    
    @register_command
    def dup(self):
        self._s.append(self._s[-1])

    
    @register_command
    def mul(self):
        self._s.append(self._s[-1]*self._s[-2])

    
    @register_command
    def swap(self):
        self._s[-2], self._s[-1] = self._s[-1], self._s[-2]

    
    @register_command
    def over(self):
        self._s.append(self._s[-2])


    
    @register_command
    def sin(self):
        self._s[-1] = math.sin(self._s[-1])


    
    @register_command
    def cos(self):
        self._s[-1] = math.cos(self._s[-1])

    
    @register_command
    def add(self):
        self._s.append(self._s[-1]+self._s[-2])

    @register_command
    def print(self):
        print(self._s)


def stack_runner():
    # number = int(raw_input("Imput number: "))
    # if not number: return

    s = Stack()
    # s.push(number)
    
    
    inpt = raw_input("Imput command or command with arguments: [{0}]".format(", ".join(COMMANDS.keys()))) 
    arg = re.compile('\d+')
    commands = 	re.compile('[a-z]+')
	
    while inpt:
        if commands.findall(inpt) and arg.findall(inpt):
            try:
                COMMANDS[commands.findall(inpt)[0].lower()](s, int(arg.findall(inpt)[0]))
            except:
                print ("Wrong comand or argument. Try again later")
        elif commands.findall(inpt):
            try:
                COMMANDS[commands.findall(inpt)[0].lower()](s)
            except:
                print ("Wrong comand or argument. Try again later")    
        else: break
        inpt = raw_input("Imput command or command with arguments: [{0}]".format(", ".join(COMMANDS.keys())))

    print(s.print())

	

class TestStack(unittest.TestCase):

    def test_stack(self):
        n = 5
        r0 = math.sin(n) + math.cos(n)

        s = Stack()
        s.push(n)
        s.dup()
        s.sin()
        s.swap()
        s.cos()
        s.add()

        r1 = s.pop()

        self.assertEqual(r0, r1)


if __name__ == '__main__':
    # unittest.main()
    stack_runner()