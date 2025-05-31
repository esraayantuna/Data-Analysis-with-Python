class FragmentCollection:

    def __init__(self):
        self.__fragments = list()

    def add(self, fragment):
        self.__fragments.append(fragment)

    def prefixCount(self, p):
        count = 0
        for fragment in self.__fragments:
            if fragment.startswith(p):
                count += 1
        return count

    def __str__(self):
        return str(self.__fragments)
