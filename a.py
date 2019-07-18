#!/bin/env python
## -*- coding: utf-8 -*-

import os, sys

class A(object):
    def add(self, a, b):
        return a + b
    def div(self, a, b):
        return a // b
    def square(self, a):
        return a * a
    def cube(self, a):
        return a * a * a
    

def main():
    a = A()
    print("2+1=", a.add(2,1))
    print("2/1=", a.div(2,1))

if __name__ == "__main__":
    main()
