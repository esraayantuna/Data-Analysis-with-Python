from hw.MyLinkedList import LinkedList

def printList(s, l):
    print("\n" + s)
    for v in l:
        print(str(v) + " ", end="")

# Union of two sorted lists */
def union(list1, list2):
    current1 = list1.getHeadNode()  # Current index in list1
    current1NodeCount = 0

    current2 = list2.getHeadNode()  # Current index in list2
    current2NodeCount = 0

    current3 = LinkedList()

    while current1NodeCount < list1.getSize() and current2NodeCount < list2.getSize():
        if current1.element <= current2.element:
            current3.add(current1.element)
            current1NodeCount += 1
            if current1.element == current2.element:
                current2NodeCount += 1
                current2 = current2.next
            current1 = current1.next
        else:
            current3.add(current2.element)
            current2NodeCount += 1
            current2 = current2.next


    while current1NodeCount < list1.getSize():
        current3.add(current1.element)
        current1NodeCount += 1
        current1 = current1.next

    while current2NodeCount < list2.getSize():
        current3.add(current2.element)
        current2NodeCount += 1
        current2 = current2.next

    return current3

# Union of two sorted lists */
def intersection(list1, list2):
    current1 = list1.getHeadNode()  # Current index in list1
    current1NodeCount = 0

    current2 = list2.getHeadNode()  # Current index in list2
    current2NodeCount = 0

    current3 = LinkedList()

    while current1NodeCount < list1.getSize() and current2NodeCount < list2.getSize():
        if current1.element == current2.element:
            current3.add(current1.element)
            current1NodeCount += 1
            current2NodeCount += 1
            current1 = current1.next
            current2 = current2.next
        elif current1.element < current2.element:
            current1NodeCount += 1
            current1 = current1.next
        else:
            current2NodeCount += 1
            current2 = current2.next

    return current3

def main():
    l1 = [2, 4, 8, 12, 20, 46]
    l1list = LinkedList()
    for e in l1:
        l1list.addLast(e)

    l2 = [1, 4, 12, 35, 72]
    l2list = LinkedList()
    for e in l2:
        l2list.addLast(e)

    unionList = union(l1list, l2list)
    print("\nl1:", l1list)
    print("\nl2:", l2list)
    print("Union:", unionList)

    intersectionList = intersection(l1list, l2list)
    print("Intersection:", intersectionList)

main()
 
