spaces = int(input())
yes = input()
tod = input()

count = 0
for i in range(0, spaces):
    if(yes[i] == 'C' and tod[i] == 'C'):
        count += 1

print(count)
