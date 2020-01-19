#! /usr/bin/python3

###! Python Iterators // Thats hard

##      * An iterator is an object that contains a countable number of values.
##      * Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()



##? Iterator vs Iterable
#       * Lists, tuples, dictionaries, and sets are all iterable objects.
#       * they have a iter() method which is used to get an iterator
myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))


#       * strings are also iterable objects
myStr = "banana"
myIt = iter(myStr)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))



##? Looping through an Iterator
#       * the 'for' loop automatically creates the iterator and executes the next() method

myTuple = ("apple", "banana", "cherry")

for x in myTuple:
    print(x)

myStr = "banana"

for x in myStr:
    print(x)



##? Create an Iterator
#       * to create object/class as an iterator you have to implement '__iter__()' and '__next__()' methods
#       * '__iter__()' method acts similar to '__init__()', you can do operations (initializing etc.), but must always return the iterator object itself
#       * '__next__()' method allows you to do operations, and must return the next item in the sequence

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))



##? StopIteration
#       * The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
#       * To prevent the iteration to go on forever, we can use the StopIteration statement.

class MyNewNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # raising the 'StopIteration' error when the condition is no longer true

myNewClass = MyNewNumbers()
myNewIter = iter(myNewClass)

for x in myNewIter:
    print(x)
