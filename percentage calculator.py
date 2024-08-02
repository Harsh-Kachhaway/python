a = []

i = 0
while i < 1:
    inp = int(input("enter markes:"))
    if inp == 0 :
        print('over')
        break
    else:
        a.append(inp)

print(a)
percent = (sum(a)/(100*len(a)))*100
print("your percent is " + str(percent) + "%")