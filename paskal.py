# -*- coding: utf-8 -*- 

"""
This module contains my realization of pascal triangle.
But on this site http://rosettacode.org/wiki/Pascal's_triangle#Python 
I was found the most beautifull realization of this problem on python.

def pascal(n):
   '''Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success.'''
   row = [1]
   k = [0]
   for x in range(max(n,0)):
      print row
      row=[l+r for l,r in zip(row+k,k+row)]
   return n>=1
On this vode we just shake the previuos row.
Very elegant.

"""
from numpy import *

def pascal(row_n):
    pascal_delta = [[]]*row_n
    pascal_delta[0]=[1]
    pascal_delta[1]=[1,1]
    print (' ' * row_n +  ' '.join(map(str,pascal_delta[0])))
    print (' ' * (row_n-1) +  ' '.join(map(str,pascal_delta[1])))
    i=2
    j=1
    while i<row_n:
        pascal_delta[i]=[1]*(i+1)
        while j<i: 
            pascal_delta[i][j]=pascal_delta[i-1][j-1]+pascal_delta[i-1][j] 
            j+=1
        cur_row = ' '* (row_n-i) + ' '.join(map(str,pascal_delta[i]))
        i+=1
        j=1
        print (cur_row)
    
    

if __name__ == '__main__':
    print pascal(10)
    
    
    
    
    
    
    
    
    
    
    
    
    