"""
Heaps are concrete data structures, whereas priority queues are abstract data structures.
"""
import heapq

"""
Create heap using heapq package
"""
a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)
print(a)
# Output:- [1, 2, 3, 5, 6, 8, 7]

"""
Push element
"""
heapq.heappush(a, 10)
print(a)
# Output:- [1, 2, 3, 5, 6, 8, 7, 10]

"""
Pop element
"""
heapq.heappop(a)
print(a)
# Output:- [2, 5, 3, 10, 6, 8, 7]
