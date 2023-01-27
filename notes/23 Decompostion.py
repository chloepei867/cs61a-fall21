# Set Intersection
 # Linear-Time Intersection of Sorted Lists

def fast_overlap(s, t):
    """
    Given two sorted lists with no repeats, 
    return the number of elements that appear in both.
    >>> fast_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8]) 
    2
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count+1, i+1, j+1
        elif s[i] > t[j]:
            j += 1
        else:
            i += 1
    return count

# Modular Design
 # Example: Similar Restaurants
"""Implement similar, a Restaurant method that takes a positive integer k and a function
similarity that takes two restaurants as arguments and returns a number. Higher similarity
values indicate more similar restaurants. The similar method returns a list containing the
k most similar restaurants according to the similarity function, but not containing self.
"""
def similar(self, k, similarity):
    others = list(Restaurant.all)
    others.remove(self)
    return sorted(others, key=lambda r: -similarity(self, r))[:k]    #key point!! 用slice获得前n个元素

#知识点：sorted()
"""
sorted(iterable, /, *, key=None, reverse=False)
 Return a new list containing all items from the iterable in ascending order.
 A custom key function: can be supplied to customize the sort order, 
 the reverse flag: can be set to request the result in descending order.
"""