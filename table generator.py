for i in range(2,21):
    with open(f"table/table_of { i }.txt ",'a') as f:
        for j in range(1,11):

            f.write( str(i) + '*' + str(j) + '=' + str(i*j) +'\n')
            print(f"done{i}")
print('over')