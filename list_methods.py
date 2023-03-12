#More on Lists

def printCity():
    print(City)

City=["กรุงเทพ","สมุทรปราการ","นนทบุรี",]
City.append("นครปฐม")
#Add an item to the end of the list. Equivalent to a[len(a):] = [x].

City.insert(3,"ปทุมธานี")
#Insert an item at a given position. The first argument is the index of the element before which to insert,
#so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

printCity()

City.remove("กรุงเทพ")
#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

City.pop(0)
#Remove the item at the given position in the list, and return it.
#If no index is specified, a.pop() removes and returns the last item in the list.

City.reverse()
#Reverse the elements of the list in place.

printCity()

City.clear()
#Remove all items from the list. Equivalent to del a[:].

printCity()