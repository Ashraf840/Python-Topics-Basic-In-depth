# the barebone process of using enumerate function in a for loop.

list_var = [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), ]


for index, letter in list_var:
    print(index, '-'*10, letter)


"""
Output
0 ---------- A
1 ---------- B
2 ---------- C
3 ---------- D
"""
