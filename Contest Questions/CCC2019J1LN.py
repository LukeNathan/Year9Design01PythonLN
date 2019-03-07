apple3 = input()
apple2 = input()
apple1 = input()
banana3 = input()
banana2 = input()
banana1 = input()

app3 = int(apple3)
app2 = int(apple2)
app1 = int(apple1)
ban3 = int(banana3)
ban2 = int(banana2)
ban1 = int(banana1)

if 3 * app3 + 2 * app2 + app1 > 3 * ban3 + 2 * ban2 + ban1:
    print("A")
elif 3 * ban3 + 2 * ban2 + ban1 > 3 * app3 + 2 * app2 + app1:
    print("B")
elif 3 * app3 + 2 * app2 + app1 == 3 * ban3 + 2 * ban2 + ban1:
    print("T")
