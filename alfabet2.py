print("Alfabet")
x = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera + " => " + litera.lower()
    if i > 65 and x % 10 == 0:
            x = 0
            tmp += "\n"
    print(tmp,end=" ")
