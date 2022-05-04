places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

no_empties = list(filter(lambda t: t != '', places))

print(no_empties)
