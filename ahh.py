numDay = input("number of days:" )
dayStart = input ("not confusing at all:")

print(" Su Mo Tu We Th Fr Sat\n")

secondlist = [1,2,3,4,5,6,7]


count = 0
print (secondlist)
while count < int(numDay):
    count = count + 7
    secondlist = [element + 7 for element in secondlist]
    print(secondlist)