from heapq import heappush, heappop

def heapsort(iterable):
    heap = []

    ordered = []

    while heap:
        ordered.append(heappop(heap))