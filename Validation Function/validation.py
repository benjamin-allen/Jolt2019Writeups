val1s = [False, True, False, True, True, True, False, False]
val2s = [351, 227, 325, 436, 220, 645, 517, 349]

f = open("dict.txt")
dict_str = f.read()
dict = dict_str.split("\n")

def val1(a):
    return (len(a) % 2) == 0

def val2(a):
    total = 0
    for c in a:
        total += ord(c)
    return total
"""
print(len(dict))

word_count = 0
current_word = 0
while(word_count < 8):
    test = dict[current_word]
    if val1(test) == val1s[word_count] and val2(test) == val2s[word_count]:
        print(test)
        word_count += 1
        current_word = 0
    else:
        current_word += 1
"""

counter = 0
candidates = []
for v2 in val2s:
    out = []
    for word in dict:
        if(val2(word) == v2 and val1(word) == val1s[counter]):
            out.append(word)
    candidates.append(out)
    counter += 1

for candidate in candidates:
    print(candidate)

"try to let ... you"
