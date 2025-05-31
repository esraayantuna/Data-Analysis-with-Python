from LinkedList import LinkedList

L1= LinkedList()
L1.add(2)
L1.add(4)
L1.add(8)
L1.add(12)
L1.add(20)
L1.add(46)

L2=LinkedList()
L2.add(1)
L2.add(4)
L2.add(12)
L2.add(35)
L2.add(72)

intersectionlist=LinkedList()

for i in range(L1.getSize()):
    currentelement = L1.removeFirst()
    if L2.contains(currentelement):
        intersectionlist.add(currentelement)

print(str(intersectionlist))









