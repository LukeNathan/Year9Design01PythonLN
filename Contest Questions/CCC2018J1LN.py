l1 = str(input(""))
l2 = str(input(""))
l3 = str(input(""))
l4 = str(input(""))

if l1 == 8 or l1 == 9:
    print("ignore")
    if l2 == l3:
        print("ignore")
        if l4 == 8 or l4 == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
