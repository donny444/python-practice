alphabet = input("Enter alphabet for an example word(upper-case): ")

match alphabet:
    case "A":
        print("Ant")
    case "B":
        print("Bat")
    case "C":
        print("Cat")
    case "D":
        print("Donny")
    case "E":
        print("Eat")
    case "F":
        print("Fish")
    case "G":
        print("Galaxy")
    case _:
        print("Unidentified")
