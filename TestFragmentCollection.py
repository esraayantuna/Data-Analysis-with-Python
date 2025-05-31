from FragmentCollection import FragmentCollection

fc = FragmentCollection()
fc.add("AC")
fc.add("TACG")
fc.add("TCGAA")
fc.add("CGA")
fc.add("AGCT")
fc.add("TCGG")
fc.add("TCGG") #added twice , will be counted twice

print("Fragment collection: " + str(fc))
fragment = ""
count = fc.prefixCount (fragment) #returns 7 ( number of adds )
print(fragment + " count is " + str(count))

fragment = "T"
count = fc.prefixCount (fragment) #returns 4 (TACG , TCGAA , TCGG , TCGG )
print(fragment + " count is " + str(count))

fragment = "TC"
count = fc.prefixCount (fragment) #returns 3 (TCGAA , TCGG , TCGG )
print(fragment + " count is " + str(count))

fragment = "G"
count = fc.prefixCount (fragment) #returns 0
print(fragment + " count is " + str(count))