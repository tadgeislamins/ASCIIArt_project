from char_tensors import char_t


def shade(tensor):
    return float(tensor.mean())


chlist = range(33, 127)
chars_list = [char_t(ch) for ch in chlist]
chars_t = torch.stack(chars_list)

def normalization(chars_t):
    mean, std = chars_t.mean([2, 3]), chars_t.std([2, 3])
    normalize = transforms.Compose([T.Normalize(mean, std)])
    chars_normalized = normalize(chars_t)
    return chars_normalized

normalization(chars_t)

# shadelist = sorted(
#     [(chr(ch), shade(char_t(ch))) for ch in chlist],
#     key=lambda tup: tup[1])
# for i in shadelist:
#     print(i)
