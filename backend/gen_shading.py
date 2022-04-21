from char_tensors import totensor

symbols = ['a', 'b', 99, 100, 101]

for i in totensor(symbols).values():
    print(i[0][0:30][0:60])
