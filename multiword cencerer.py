words = ["moti" , 'kadu', 'donkey']

with open('sample.txt' , 'r+') as f:
    contant = f.read()

for word in words:
    contant = contant.replace(word,"#$%^&")
    print(contant)
    with open('sample.txt' , 'w') as f:
        f.write(contant)
        print("done")
