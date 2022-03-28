# Altering arrays

def intro():
	'''We will see usage of .insert(), .append(), .pop() when changing arrays'''

>>> shopping = ["kiwis", "peas"]
>>> print(shopping)
['kiwis', 'peas']

# inserting string to index 0
>>> shopping.insert(0, "lemon")
>>> print(shopping)
['lemon', 'kiwis', 'peas']

# inserting string to last position
>>> shopping.append("banana")
>>> print(shopping)
['lemon', 'kiwis', 'peas', 'banana']

# removing last item
>>> shopping.pop()
'banana'
>>> shopping.pop()
'peas'
>>> print(shopping)
['lemon', 'kiwis']

>>> shopping.append("banana")
>>> shopping.append("pinapple")
>>> print(shopping)
['lemon', 'kiwis', 'banana', 'pinapple']

# removing a specific item within array
>>> shopping.pop(2)
'banana'
>>> print(shopping)
['lemon', 'kiwis', 'pinapple']

# printing a item removed with pop
>>> print(shopping)
['lemon', 'kiwis', 'pinapple']
>>> removed = shopping.pop(1)
>>> print(removed)
kiwis
>>> print(shopping)
['lemon', 'pinapple']
