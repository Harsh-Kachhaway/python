def game(s):
    return s

with open ('sample.txt' , "r") as f:
    a = f.read()

score = game(input("score"))
print(score)

if a < score:
    with open ('sample.txt','w') as f:
        f.write(score)