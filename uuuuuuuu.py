spells_1 = input().split(', ')
spells_2 = input().split(', ')
spisok = []
for elem in spells_1:
    if elem in spells_2:
        spisok.append(elem)
spisok.sort()
print(" ".join(spisok))