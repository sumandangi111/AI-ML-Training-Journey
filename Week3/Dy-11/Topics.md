## Lists , Tuples , Sets , Dictionaries , String methods 

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

#  -------------------------------------------------------------------
## List
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor- used to create list
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# 1. Access Items
List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# 2. Change Item Value
To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# 3. Add List Items
# Append Items .append()
To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items .insert()
The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List .extend()
To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# 4. Remove List Items
# Remove List Items .remove()
The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index  .pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del keyword
The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
 #this will cause an error because you have succsesfully deleted "thislist".

# Clear the List
The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

## Loop Lists
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# ----------------------------------------------------------
## List Methods

# 1.To add elements:-
1. append() - add element at the end of the list / also add any another list at the end
2. insert() - add element at particular index
3. extend() - The extend() method adds the specified list elements (or any iterable) to the end of the current list.

# 2. Remove elements:-
1. remove() - Removes the item at the specified value
2. pop() - removes the element at the specified postion(index number) / if index number is not mentioned than last element will be removed
3. del keyword - remove element at specific index / if index not mentioned than the whole list will be deleted
4. clear() - empties the list

# 3. copy() - Return a copy of the list

# 4. count() - Return the number of elements with the specified value

# 5. index() - return the index of first element with specific value

# 6.reverse() - reverse the list

# 7. sort() - sort the list by default ascending / .sort(reverse=True)

# -----------------------------------------------------------------

## Tuple

# 1. count() - Returns the number of times a specified value occurs in a tuple
# 2. index()	Searches the tuple for a specified value and returns the position of where it was found

# --------------------------------------------------------------------

