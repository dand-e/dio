# Decisions

def intro:
	'''Usage of decision loops'''

>>> print(shopping)
['apple', 'banana', 'carrot', 'dragonfruit', 'eggplant']

# Using len() to count array lenght
>>> print (len(shopping))
5

# It is possible to assign len() value to a variable
>>> shopping.append("ficus")
>>> number_of_itens = len(shopping)
>>> print (number_of_itens)
6

# While usage
>>> print (shopping)
['apple', 'banana', 'carrot', 'dragonfruit', 'eggplant', 'ficus']
>>> number_of_itens = len(shopping)
>>> print (number_of_itens)
6
>>> while number_of_itens >= 6:
...     print ("We need groceries!")
...     number_of_itens -= 1
...
We need groceries!


# While usage 2
>>> print (shopping)
['apple', 'banana', 'carrot', 'dragonfruit', 'eggplant']
>>> while number_of_itens >= 5:
...     print ("We need groceries!")
...     number_of_itens = 3
...     if number_of_itens < 5:
...             print ("We can go to the market tomorrow!")
...             print (f"We have {number_of_itens} itens to eat today")
...
We need groceries!
We can go to the market tomorrow!
We have 3 itens to eat today

# For usage
>>> for i in range (4):
...	print ("***********---------")
>>> for i in range (4):
...     print ("--------------------")
...
***********---------
***********---------
***********---------
***********---------
--------------------
--------------------
--------------------
--------------------



# When len() is used with an empty array will return 0
>>> farmers_market = []
>>> print (len(farmers_market))
0

# It is also possible to use them as a condition parameter
>>> if len(farmers_market) == 0:
...     print("Go to neighbourhood Market")
...
Go to neighbourhood Market


