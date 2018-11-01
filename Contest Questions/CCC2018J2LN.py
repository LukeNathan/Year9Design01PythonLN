num = int(input(""))
y = input("")
t = input("")

count = 0

for i in range(0, num):
    if(y[i] == 'C' and t[i] == 'C'):
        count += 1

print(count)
