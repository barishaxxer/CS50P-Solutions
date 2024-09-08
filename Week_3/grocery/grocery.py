glist = []
try:
    while True:
        item = input("").upper()
        glist.append(item)
except (EOFError,TypeError):
    uniq = list(set(glist))
    uniq.sort()
    for i in uniq:
        print(glist.count(i),i)

