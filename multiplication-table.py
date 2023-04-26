for i in range(1, 10):
    for j in range(1, 10):
        out = "\u2502{:^4d}".format(i*j)
        print(out, end='')
    print("\u2502\n", "\u253c\u2500\u2500\u2500\u2500"*9, '\u253c', sep='')
