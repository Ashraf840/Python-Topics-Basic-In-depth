var_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}


# Access the key & value of a dict (Faster Execution Time)
# for i in var_dict:
#     print('Key:', i, '-----', 'Value:', var_dict[i])


# Access the key & value of a dict (Slower Execution Time)
for i,j in enumerate(var_dict):
    print('Key:', i, '-----', 'Value:', j)


