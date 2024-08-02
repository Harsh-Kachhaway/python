with open ("sample.txt", 'r') as f:
    content = True
    i = 0
    while content:
        line = f.readline().lower()
        i += 1
        if 'python' in line:
            print(str(i) + ' line')
            break
