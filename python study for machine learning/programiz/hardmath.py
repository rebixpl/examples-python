class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


a = iter(InfIter())
biglist = []

while True:
    x = next(a)
    print(x)
    biglist.append(x)
    print(biglist)