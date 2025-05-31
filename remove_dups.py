# Removes dups and returns the new list
def remove_dups(l):
    distinctList = []
    for i in range(len(l)):
        # add element l[i] to the distinct list if already not there
        found = False
        for j in range(len(distinctList)):
            if l[i] == distinctList[j]:
                found = True
                break
        if not found:
            distinctList.append(l[i])

    return distinctList

a = [10, 8, 6, 6, 4, 4, 0, -2, -2, 1, 1, 3, 5, 7, 15, 15]
print(a)
a = remove_dups(a)
print(a)