class FragmentCollection:

    def __init__(self ,a=[], n=0):
        self.__list = a
        self.__number = n

    def add(self, fragment):
        totalfragments = FragmentCollection()
        self.__list.append(fragment)
        self.__number += 1
        totalfragments.__list = self.__list
        totalfragments.__number = self.__number
        print(totalfragments.__list)                                 # I added print command to see the total list after each addition.
        return totalfragments.__list



    def prefixCount(self,p):
        count=0
        if p == '':
            count= self.__number
        else:
            for i in range(self.__number):
                    if list(self.__list)[i][0: len(p)] == p:
                        count +=1
        print(count)



