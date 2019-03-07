c = int(input(""))
if "" in c[1]:
    c1 = c[0]
elif "" in c[2]:
    c1 = c[0:1]

if "" in c[3]:
    c1 = c[2]
elif "" in c[4]:
    c1 = c[0:1]

if "" in c[1]:
    c1 = c[0]
elif "" in c[2]:
    c1 = c[0:1]

if "" in c[1]:
    c1 = c[0]
elif "" in c[2]:
    c1 = c[0:1]


print("0", c1, c1 + c2, c1 + c2 + c3, c1 + c2 + c3 + c4)
print(c1, "0", c2, c2 + c3, c2 + c3 + c4)
print(c1, c1 + c2, "0", c3, c3 + c4)
print(c1, c1 + c2, c1 + c2 + c3, "0", c4)
print(c1, c1 + c2, c1 + c2 + c3, c1 + c2 + c3 + c4, "0")
