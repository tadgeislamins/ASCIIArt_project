from char_tensors import totensor

for t in totensor(range(33, 127)):
    print(t[0][0:60][0:30])
