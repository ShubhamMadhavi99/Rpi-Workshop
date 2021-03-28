Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> a=numpy.array([1,2,3,4])
>>> import numpy as np
>>> b=numpy.array([4,3,2,1])
>>> c=[1,2,3,4]
>>> d=[4,3,2,1]
>>> a
array([1, 2, 3, 4])
>>> print(a)
[1 2 3 4]
>>> print(c)
[1, 2, 3, 4]
>>> c+d
[1, 2, 3, 4, 4, 3, 2, 1]
>>> a+b
array([5, 5, 5, 5])
>>> c=np.array([1.1, np.e, np.pi])
>>> c
array([1.1       , 2.71828183, 3.14159265])
>>> d=np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> e=np.arange(0,21)
>>> e
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20])
>>> e=np.arange(0,2,0.1)
>>> e
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
>>> z=np.zeros(10)
>>> z
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
>>> o=np.ones(5)
>>> o
array([1., 1., 1., 1., 1.])
>>> z+1
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> fill=np.zeros(10)
>>> fill+12
array([12., 12., 12., 12., 12., 12., 12., 12., 12., 12.])
>>> fill=np.full(10,99)
>>> fill
array([99, 99, 99, 99, 99, 99, 99, 99, 99, 99])
>>> fill=np.full((3,3),99)
>>> fill
array([[99, 99, 99],
       [99, 99, 99],
       [99, 99, 99]])
>>> a
array([1, 2, 3, 4])
>>> a[0]
1
>>> a[2]
3
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> d[1,0]
4
>>> b
array([4, 3, 2, 1])
>>> b[0:3]
array([4, 3, 2])
>>> b[1:3]
array([3, 2])
>>> a
array([1, 2, 3, 4])
>>> a[3]
4
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a[4]
IndexError: index 4 is out of bounds for axis 0 with size 4
>>> a[0]
1
>>> a[-1]
4
>>> a[-3]
2
>>> a[-4]
1
>>> a[-5]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a[-5]
IndexError: index -5 is out of bounds for axis 0 with size 4
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> d[0:2,1:3]
array([[2, 3],
       [5, 6]])
>>> d[0,:]
array([1, 2, 3])
>>> d[:,1]
array([2, 5, 8])
>>> a
array([1, 2, 3, 4])
>>> a[1:4]
array([2, 3, 4])
>>> a[1:]
array([2, 3, 4])
>>> a+b
array([5, 5, 5, 5])
>>> c
array([1.1       , 2.71828183, 3.14159265])
>>> f=np.array([])
>>> f
array([], dtype=float64)
>>> a^b
array([5, 1, 1, 5], dtype=int32)
>>> c+d
array([[ 2.1       ,  4.71828183,  6.14159265],
       [ 5.1       ,  7.71828183,  9.14159265],
       [ 8.1       , 10.71828183, 12.14159265]])
>>> a+c
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a+c
ValueError: operands could not be broadcast together with shapes (4,) (3,) 
>>> a
array([1, 2, 3, 4])
>>> c
array([1.1       , 2.71828183, 3.14159265])
>>> a.shape
(4,)
>>> a.ndim
1
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> d.ndim
2
>>> e
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
>>> f
array([], dtype=float64)
>>> f.ndim
1
>>> a.shape
(4,)
>>> d.shape
(3, 3)
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> b.shape[0]
4
>>> a.size
4
>>> d.size
9
>>> e.size
20
>>> a.itemsize
4
>>> a.dtype
dtype('int32')
>>> c
array([1.1       , 2.71828183, 3.14159265])
>>> c.dtype
dtype('float64')
>>> c.itemsize
8
>>> f
array([], dtype=float64)
>>> f.itemsize
8
>>> f.size
0
>>> c=np.array([1.1,np.e,np.pi],dtype='int16')
>>> c
array([1, 2, 3], dtype=int16)
>>> e=np.array([0,1,2],dtype='int8')
>>> e
array([0, 1, 2], dtype=int8)
>>> e+255
array([255, 256, 257], dtype=int16)
>>> e==np.array([255,256,0],dtype='int8')
array([False, False, False])
>>> e=np.array([255,128,0],dtype='int8')
>>> e
array([  -1, -128,    0], dtype=int8)
>>> a.nbytes
16
>>> a
array([1, 2, 3, 4])
>>> a.itemsize
4
>>> c=np.array([1.1,np.e,np.pi])
>>> c
array([1.1       , 2.71828183, 3.14159265])
>>> c.nbytes
24
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> c=np.array([[1],[1],[1]])
>>> c
array([[1],
       [1],
       [1]])
>>> np.matmul(d,c)
array([[ 6],
       [15],
       [24]])
>>> I=np.identity(3)
>>> I
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> I=np.identity(3,dtype='int32')
>>> I
array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]])
>>> np.matmul(d,I)
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np.linalg.det(d)
0.0
>>> np.linalg.det(I)
1.0
>>> a
array([1, 2, 3, 4])
>>> d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> d.min()
1
>>> d.max()
9
>>> d.mean()
5.0
>>> 