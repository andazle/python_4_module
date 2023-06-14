def football():
    check = True
    win = 0
    lose = 0
    draw = 0
    spisok_match = input().replace("['", '', ).replace("']", '').split("', '")
    for match in spisok_match:
        if match == 'победа':
            win += 1
        if match == 'поражение':
            lose += 1
        if match == 'ничья':
            draw += 1
    if (win >= 3) or (win >= 2 and draw >= 2):
        check = True
    else:
        check = False
    if check:
        print(True)
    else:
        print(False)


# football()

def film_in_lib(film, director, l):
    check = 0
    for films in l[director]:
        if films == film:
            check += 1
    if check == 1:
        print('Фильм есть в коллекции')
    else:
        print('Увы!')


l = {'Д.Кемерон': ['Чужие', 'Титаник'],
     'С.Спилбег': ['Список Шиндлера', 'Война миров', 'Парк Юрского периода']}
movie = input()
director = input()

print(film_in_lib(movie, director, l))
