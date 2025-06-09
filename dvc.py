def identifiers():
    f = open('identifiers.csv', 'x')
    with open('identifiers.csv', 'w') as f:
        for i in range(1, 11):
            print(i)
        f.close()

identifiers()