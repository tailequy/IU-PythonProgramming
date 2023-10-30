'''
Iterators are implemented as classes using the iterator protocol definition. An iterator protocol
is a specific class that implements the methods __iter__() and __next__().
• __iter__ returns the iterator object itself.
• __next__ returns the next iteration value.
'''
class SequenceNumber():
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.low < self.high:
            self.low += 1
            return self.low - 1
        else:
            raise StopIteration