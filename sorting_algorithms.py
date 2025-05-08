from ds import LinkedList

def bubble_sort(theSeq):
    if isinstance(theSeq, list):
        n = len(theSeq)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if theSeq[j] > theSeq[j + 1]:
                    theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
        return theSeq

    elif isinstance(theSeq, LinkedList):
        for i in range(theSeq.num_items - 1):
            current = theSeq.head
            for j in range(theSeq.num_items - 1 - i):
                if current.data > current.next.data:
                    # verileri swap ediyoruz, node'ları değil
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
        return theSeq

    else:
        raise TypeError("bubble_sort only supports list or LinkedList")



