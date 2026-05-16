import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    myHeap = []

    # Reverse sorted order 
    for num in nums:
        pair = (-num, num)
        heapq.heappush(myHeap, pair)
    
    myList = []
    while myHeap:
        pair = heapq.heappop(myHeap)
        myList.append(pair[1])
    
    return myList


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
