from char_tensors import totensor


def shade(tensor):
    return float(tensor.mean())


chlist = range(33, 127)
shadelist = sorted(
    [(chr(ch), shade(totensor(ch))) for ch in chlist],
    key=lambda tup: tup[1])
for i in shadelist:
    print(i)
