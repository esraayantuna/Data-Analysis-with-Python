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

unionlist=L1

for i in range(L2.getSize()):
    currentelement = L2.removeFirst()
    if L1.contains(currentelement) != True:
        unionlist.add(currentelement)

print(str(unionlist))