import random
a = 0
for i in range(1,8000000):
    ran = random.randint(0,1)
    f = open("another.txt", 'a')
    if a == 7:
        f.write(str(" "))
        a = 0
    else:
        f.write(str(ran))
        a+= 1
f.close()
print("over")