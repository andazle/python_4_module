pictures = {
    "gfh": 'я',
    "gfhp": 'я',
    "gfhi": 'y',
    "gfhu": 'я',
    "gfhy": 'o',
    "gfht": '[',
}
artist_to_search = input()
for i in pictures.values():
    if i == artist_to_search:
        print(pictures[i])

