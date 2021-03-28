Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=4
>>> b=10
>>> a
4
>>> b
10
>>> a+b
14
>>> a-b
-6
>>> a*b
40
>>> a/b
0.4
>>> b**a
10000
>>> b%a
2
>>> a+=1
>>> a
5
>>> a+=b
>>> a
15
>>> if a>15:
	print('a is greater than 15')
elif a==15
SyntaxError: invalid syntax
>>> if a>15:
	print('a is greater than 15')
elif a==15:
	print('a is equal to 15')
else:
	print('a is less than 15')

	
a is equal to 15
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> while b<a:
	print(b)
	b+=1

	
10
11
12
13
14
>>> def compare_with_15(a):
	if a>15:
		print('a is greater than 15')
	elif a==15:
		print('a is equal to 15')
	else:
		print('a is less than 15')

		
>>> compare_with_15(7)
a is less than 15
>>> compare_with_15(15)
a is equal to 15
>>> a=[1,2,3,4,5]
>>> a={'Name':['Shubham','Sunit','Shreyas'],'Marks':[50,60,70]}
>>> a
{'Name': ['Shubham', 'Sunit', 'Shreyas'], 'Marks': [50, 60, 70]}
>>> print(a)
{'Name': ['Shubham', 'Sunit', 'Shreyas'], 'Marks': [50, 60, 70]}
>>> 