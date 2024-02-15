try:
    positive = int(input("Enter only positive integer!: "))
    if(positive < 0):
        raise ValueError("Not negative integer")
    if(positive == 0):
        raise ValueError("Not Zero")
except ValueError as e:
    print(e)
except ValueError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("Goodbyes")

print("No error detected")