x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if key!='a'}

print(x)