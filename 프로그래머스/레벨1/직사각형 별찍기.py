a, b = map(int, input().strip().split(' '))
string = ""
for x in range(b):
    for y in range(a):
        print("*", end = "")
    print("")