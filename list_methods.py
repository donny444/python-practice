#More on Lists

a=["Apple","Ant","Arm",]
a.append("Abbrevation")
#Add an item to the end of the list. Equivalent to a[len(a):] = [x].

b=["Boss","Bee","Brother"]
b.insert(1,"Bat")
#Insert an item at a given position. The first argument is the index of the element before which to insert, so 
#a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).