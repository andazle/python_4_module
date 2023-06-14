def kinopoisk():
    first_message = input(
        'Привет! Совсем недавно оформил подписку на Netflix и не знаешь что посмотреть? Наша программа '
        'поможет тебе в этом! Благодаря нашей программе ты сможешь подобрать подходящий под твои '
        'предпочтения фильм или сериал с твоим любимым актером и любимым жанром.Для начала напиши, '
        'что ты хочешь найти: фильм или сериал ').lower()

    spisokserial1 = ['Аббатство Даунтон', 'Бесстыжие', 'Чернобыль', 'Анатомия страсти', 'Молодой папа']
    spisokserial2 = ['Офис', 'Друзья', 'Клиника', 'Теория большого взрыва', 'Тед Лассо']
    spisokserial3 = ['Мост', 'Настоящий детектив', 'Большая маленькая ложь', 'Ганнибал', 'Шерлок']
    spisokserial4 = ['Игра престолов', 'Сверхъестественное', 'Древние', 'Гримм', 'Дом дракона']
    spisokserial5 = ['Вечность', 'Засланец из космоса', 'Мир Дикого Запада', 'Рассказ служанки', 'Флэш']
    spisokserial6 = ['Во все тяжкие', 'Нарко', 'Настоящий детектив', 'Мейр из Исттауна', 'Сопрано']

    spisok1 = ['Отпетые мошенницы']
    spisok2 = ['8 Подруг Оушена']
    spisok3 = ['Один день']
    spisok4 = ['Темный рыцарь: Возрождение легенды']
    spisok5 = ['Море соблазна']
    spisok6 = ['Убийство на яхте']
    spisok7 = ['Укради мою жену']
    spisok8 = ['Притворись моей женой']
    spisok9 = ['Охотник за головами']
    spisok10 = ['Пышка']
    spisok11 = ['Ключ от всех дверей']
    spisok12 = ['Достать ножи: Стеклянная луковица']
    spisok13 = ['Жених напрокат']
    spisok14 = ['Четыре пера']
    spisok15 = ['Война невест']
    spisok16 = ['Страна грез']
    spisok17 = ['Девушка, подающая надежды']
    spisok18 = ['Волк с Уолл - стрит']
    spisok19 = ['Отряд самоубийц']
    spisok20 = ['Фокус']
    spisok21 = ['Темное наследие']
    spisok22 = ['Красивый, плохой, злой']
    spisok23 = ['С любовью, Рози']
    spisok24 = ['Орудия смерти: Город костей']
    spisok25 = ['Белоснежка: месть гномов']
    spisok26 = ['Бойцовский клуб']
    spisok27 = ['Одиннадцать друзей Оушена']
    spisok28 = ['Вавилон']
    spisok29 = ['Мистер и миссис Смит']
    spisok30 = ['Затерянный город']
    spisok31 = ['Роковое искушение']
    spisok32 = ['Джентльмены']
    spisok33 = ['Банши Инишерина']
    spisok34 = ['Агент Ева']
    spisok35 = ['Залечь на дно в Брюгге']
    spisok36 = ['Под покровом ночи']
    spisok37 = ['Братья Систерс']
    spisok38 = ['Любовь и другие лекарства']
    spisok39 = ['Скорая']
    spisok40 = ['Разрушение']
    spisok41 = ['Побочный эффект']
    spisok42 = ['Омерзительная восьмерка']
    spisok43 = ['Клятва']
    spisok44 = ['Штурм Белого дома']
    spisok45 = ['Мачо и ботан 2']
    spisok46 = ['Исчезнувшая']
    spisok47 = ['Va-банк']
    spisok48 = ['К чуду']
    spisok49 = ['Закон ночи']
    spisok50 = ['Блеск славы']

    slovar = {
        'Отпетые мошенницы': 'https://www.kinopoisk.ru/film/428711/',
        '8 Подруг Оушена': 'https://www.kinopoisk.ru/film/983177/',
        'Один день': 'https://www.kinopoisk.ru/film/495518/',
        'Темный рыцарь: Возрождение легенды': 'https://www.kinopoisk.ru/film/437410/',
        'Море соблазна': 'https://www.kinopoisk.ru/film/1045061/',
        'Убийство на яхте': 'https://www.kinopoisk.ru/film/505995/',
        'Укради мою жену': 'https://www.kinopoisk.ru/film/523029/',
        'Притворись моей женой': 'https://www.kinopoisk.ru/film/490323/',
        'Охотник за головами': 'https://www.kinopoisk.ru/film/462662/',
        'Пышка': 'https://www.kinopoisk.ru/film/1048333/',
        'Ключ от всех дверей': 'https://www.kinopoisk.ru/film/77673/',
        'Достать ножи: Стеклянная луковица': 'https://www.kinopoisk.ru/film/1343908/',
        'Жених напрокат': 'https://www.kinopoisk.ru/film/463149/',
        'Четыре пера': 'https://www.kinopoisk.ru/film/673/',
        'Война невест': 'https://www.kinopoisk.ru/film/272225/',
        'Страна грез': 'https://www.kinopoisk.ru/film/1076555/',
        'Девушка, подающая надежды': 'https://www.kinopoisk.ru/film/1236567/',
        'Волк с Уолл - стрит': 'https://www.kinopoisk.ru/film/462682/',
        'Отряд самоубийц': 'https://www.kinopoisk.ru/film/468522/',
        'Темное наследие': 'https://www.kinopoisk.ru/film/1208499/',
        'С любовью, Рози': 'https://www.kinopoisk.ru/film/512784/',
        'Орудия смерти: Город костей': 'https://www.kinopoisk.ru/film/484391/',
        'Белоснежка: месть гномов': 'https://www.kinopoisk.ru/film/544226/',
        'Красивый, плохой, злой': 'https://www.kinopoisk.ru/film/512784/',
        'Аббатство Даунтон': 'https://www.kinopoisk.ru/series/518192/',
        'Бесстыжие': 'https://www.kinopoisk.ru/series/571335/',
        'Чернобыль': 'https://www.kinopoisk.ru/series/1227803/',
        'Анатомия страсти': 'https://www.kinopoisk.ru/series/277535/',
        'Молодой папа': 'https://www.kinopoisk.ru/series/893361/',
        'Мост': 'https://www.kinopoisk.ru/series/574497/',
        'Настоящий детектив': 'https://www.kinopoisk.ru/series/681831/',
        'Большая маленькая ложь': 'https://www.kinopoisk.ru/series/947758/',
        'Ганнибал': 'https://www.kinopoisk.ru/series/682468/',
        'Шерлок': 'https://www.kinopoisk.ru/series/502838/',
        'Вечность': 'https://www.kinopoisk.ru/series/823594/',
        'Засланец из космоса': 'https://www.kinopoisk.ru/series/1200189/',
        'Мир Дикого Запада': 'https://www.kinopoisk.ru/series/195523/',
        'Рассказ служанки': 'https://www.kinopoisk.ru/series/1007426/',
        'Флэш': 'https://www.kinopoisk.ru/series/817506/',
        'Затерянный город': 'https://www.kinopoisk.ru/film/4308624/',
        'Мистер и миссис Смит': 'https://www.kinopoisk.ru/film/12090/',
        'Вавилон': 'https://www.kinopoisk.ru/film/1283955/',
        'Одиннадцать друзей Оушена': 'https://www.kinopoisk.ru/film/770/',
        'Бойцовский клуб': 'https://www.kinopoisk.ru/film/361/',
        'Залечь на дно в Брюгге': 'https://www.kinopoisk.ru/film/276295/',
        'Агент Ева': 'https://www.kinopoisk.ru/film/1189368/',
        'Банши Инишерина': 'https://www.kinopoisk.ru/film/1354524/',
        'Джентльмены': 'https://www.kinopoisk.ru/film/1143242/',
        'Роковое искушение': 'https://www.kinopoisk.ru/film/970873/',
        'Разрушение': 'https://www.kinopoisk.ru/film/842493/',
        'Скорая': 'https://www.kinopoisk.ru/film/1207170/',
        'Любовь и другие лекарства': 'https://www.kinopoisk.ru/film/463695/',
        'Братья Систерс': 'https://www.kinopoisk.ru/film/968375/',
        'Под покровом ночи': 'https://www.kinopoisk.ru/film/909898/',
        'Мачо и ботан 2': 'https://www.kinopoisk.ru/film/672899/',
        'Штурм Белого дома': 'https://www.kinopoisk.ru/film/675649/',
        'Клятва': 'https://www.kinopoisk.ru/film/506296/’',
        'Омерзительная восьмерка': 'https://www.kinopoisk.ru/film/819101/',
        'Побочный эффект': 'https://www.kinopoisk.ru/film/623744/',
        'Блеск славы': 'https://www.kinopoisk.ru/film/5591/',
        'Закон ночи': 'https://www.kinopoisk.ru/film/677768/',
        'К чуду': 'https://www.kinopoisk.ru/film/496899/',
        'Va-банк': 'https://www.kinopoisk.ru/film/677880/',
        'Исчезнувшая': 'https://www.kinopoisk.ru/film/692861/',
        'Офис': 'https://www.kinopoisk.ru/series/253245/',
        'Друзья': 'https://www.kinopoisk.ru/series/77044/',
        'Клиника': 'https://www.kinopoisk.ru/series/251568/',
        'Теория большого взрыва': 'https://www.kinopoisk.ru/series/306084/',
        'Тед Лассо': 'https://www.kinopoisk.ru/series/1309707/',
        'Игра престолов': 'https://www.kinopoisk.ru/series/464963/',
        'Сверхъестественное': 'https://www.kinopoisk.ru/series/178707/',
        'Древние': 'https://www.kinopoisk.ru/series/762203/',
        'Гримм': 'https://www.kinopoisk.ru/series/582314/',
        'Дом Дракона': 'https://www.kinopoisk.ru/series/1316601/',
        'Во все тяжкие': 'https://www.kinopoisk.ru/series/404900/',
        'Нарко': 'https://www.kinopoisk.ru/series/821565/',
        'Настоящий детектив': 'https://www.kinopoisk.ru/series/681831/',
        'Мейр из Исттауна': 'https://www.kinopoisk.ru/series/1254133/',
        'Сопрано': 'https://www.kinopoisk.ru/series/79848/',
    }

    def storing_incoming_data_for_movie():
        choice = input('Отлично, подбираем для тебя фильм!С чего бы ты хотел начать: с выбора актера или жанра? Если '
                       'хочешь сначала выбрать актера, напиши «актёр», если жанр - «жанр» ').lower()
        if choice == 'актёр':
            actor = input(
                'Теперь выбери своего любимого актера из предложенных(Энн Хэтэуэй, Дженифер Энистон, Кейт Хадсон, '
                'Марго Робби, Лили Коллинз, Брэд Питт, Колин Фаррелл, Джейк Джилленхол, Ченнинг Татум, Бен Аффлек) и '
                'напиши его полное имя ').lower()
            genre = input(
                'Теперь выбери свой любимый жанр из предложенных(комедия, боевик, драма, криминал, триллер)'
                ' и напиши ').lower()
        if choice == 'жанр':
            genre = input(
                'Теперь выбери свой любимый жанр из предложенных(комедия, боевик, драма, криминал, триллер)'
                ' и напиши ').lower()
            actor = input(
                'Теперь выбери своего любимого актера из предложенных(Энн Хэтэуэй, Дженифер Энистон, Кейт Хадсон, '
                'Марго Робби, Лили Коллинз, Брэд Питт, Колин Фаррелл, Джейк Джилленхол, Ченнинг Татум, Бен Аффлек) и '
                'напиши его полное имя ').lower()

        if actor == 'энн хэтэуэй' and genre == 'триллер':
            for i in range(len(spisok5)):
                print(f'Ваш {i + 1} фильм это {spisok5[i]} и ссылка к нему {slovar[spisok5[i]]}')

        elif actor == 'энн хэтэуэй' and genre == 'криминал':
            for i in range(len(spisok4)):
                print(f'Ваш {i + 1} фильм это {spisok4[i]} и ссылка к нему {slovar[spisok4[i]]}')

        elif actor == 'энн хэтэуэй' and genre == 'драма':
            for i in range(len(spisok3)):
                print(f'Ваш {i + 1} фильм это {spisok3[i]} и ссылка к нему {slovar[spisok3[i]]}')

        elif actor == 'энн хэтэуэй' and genre == 'боевик':
            for i in range(len(spisok2)):
                print(f'Ваш {i + 1} фильм это {spisok2[i]} и ссылка к нему {slovar[spisok2[i]]}')

        elif actor == 'энн хэтэуэй' and genre == 'комедия':
            for i in range(len(spisok1)):
                print(f'Ваш {i + 1} фильм это {spisok1[i]} и ссылка к нему {slovar[spisok1[i]]}')

        elif actor == 'дженифер энистон' and genre == 'комедия':
            for i in range(len(spisok10)):
                print(f'Ваш {i + 1} фильм это {spisok10[i]} и ссылка к нему {slovar[spisok10[i]]}')

        elif actor == 'дженифер энистон' and genre == 'боевик':
            for i in range(len(spisok9)):
                print(f'Ваш {i + 1} фильм это {spisok9[i]} и ссылка к нему {slovar[spisok9[i]]}')

        elif actor == 'дженифер энистон' and genre == 'драма':
            for i in range(len(spisok8)):
                print(f'Ваш {i + 1} фильм это {spisok8[i]} и ссылка к нему {slovar[spisok8[i]]}')

        elif actor == 'дженифер энистон' and genre == 'криминал':
            for i in range(len(spisok7)):
                print(f'Ваш {i + 1} фильм это {spisok7[i]} и ссылка к нему {slovar[spisok7[i]]}')

        elif actor == 'дженифер энистон' and genre == 'триллер':
            for i in range(len(spisok6)):
                print(f'Ваш {i + 1} фильм это {spisok6[i]} и ссылка к нему {slovar[spisok6[i]]}')

        elif actor == 'кейт хадсон' and genre == 'триллер':
            for i in range(len(spisok11)):
                print(f'Ваш {i + 1} фильм это {spisok11[i]} и ссылка к нему {slovar[spisok11[i]]}')

        elif actor == 'кейт хадсон' and genre == 'криминал':
            for i in range(len(spisok12)):
                print(f'Ваш {i + 1} фильм это {spisok12[i]} и ссылка к нему {slovar[spisok12[i]]}')

        elif actor == 'кейт хадсон' and genre == 'драма':
            for i in range(len(spisok13)):
                print(f'Ваш {i + 1} фильм это {spisok13[i]} и ссылка к нему {slovar[spisok13[i]]}')

        elif actor == 'кейт хадсон' and genre == 'боевик':
            for i in range(len(spisok14)):
                print(f'Ваш {i + 1} фильм это {spisok14[i]} и ссылка к нему {slovar[spisok14[i]]}')

        elif actor == 'кейт хадсон' and genre == 'комедия':
            for i in range(len(spisok15)):
                print(f'Ваш {i + 1} фильм это {spisok15[i]} и ссылка к нему {slovar[spisok15[i]]}')

        elif actor == 'марго робби' and genre == 'триллер':
            for i in range(len(spisok16)):
                print(f'Ваш {i + 1} фильм это {spisok16[i]} и ссылка к нему {slovar[spisok16[i]]}')

        elif actor == 'марго робби' and genre == 'криминал':
            for i in range(len(spisok17)):
                print(f'Ваш {i + 1} фильм это {spisok17[i]} и ссылка к нему {slovar[spisok17[i]]}')

        elif actor == 'марго робби' and genre == 'драма':
            for i in range(len(spisok18)):
                print(f'Ваш {i + 1} фильм это {spisok18[i]} и ссылка к нему {slovar[spisok18[i]]}')

        elif actor == 'марго робби' and genre == 'боевик':
            for i in range(len(spisok19)):
                print(f'Ваш {i + 1} фильм это {spisok19[i]} и ссылка к нему {slovar[spisok19[i]]}')

        elif actor == 'марго робби' and genre == 'комедия':
            for i in range(len(spisok20)):
                print(f'Ваш {i + 1} фильм это {spisok20[i]} и ссылка к нему {slovar[spisok20[i]]}')

        elif actor == 'лили коллинз' and genre == 'триллер':
            for i in range(len(spisok21)):
                print(f'Ваш {i + 1} фильм это {spisok21[i]} и ссылка к нему {slovar[spisok21[i]]}')

        elif actor == 'лили коллинз' and genre == 'криминал':
            for i in range(len(spisok22)):
                print(f'Ваш {i + 1} фильм это {spisok22[i]} и ссылка к нему {slovar[spisok22[i]]}')

        elif actor == 'лили коллинз' and genre == 'драма':
            for i in range(len(spisok23)):
                print(f'Ваш {i + 1} фильм это {spisok23[i]} и ссылка к нему {slovar[spisok23[i]]}')

        elif actor == 'лили коллинз' and genre == 'боевик':
            for i in range(len(spisok24)):
                print(f'Ваш {i + 1} фильм это {spisok24[i]} и ссылка к нему {slovar[spisok24[i]]}')

        elif actor == 'лили коллинз' and genre == 'комедия':
            for i in range(len(spisok25)):
                print(f'Ваш {i + 1} фильм это {spisok25[i]} и ссылка к нему {slovar[spisok25[i]]}')

        elif actor == 'брэд питт' and genre == 'триллер':
            for i in range(len(spisok26)):
                print(f'Ваш {i + 1} фильм это {spisok26[i]} и ссылка к нему {slovar[spisok26[i]]}')

        elif actor == 'брэд питт' and genre == 'криминал':
            for i in range(len(spisok27)):
                print(f'Ваш {i + 1} фильм это {spisok27[i]} и ссылка к нему {slovar[spisok27[i]]}')

        elif actor == 'брэд питт' and genre == 'драма':
            for i in range(len(spisok28)):
                print(f'Ваш {i + 1} фильм это {spisok28[i]} и ссылка к нему {slovar[spisok28[i]]}')

        elif actor == 'брэд питт' and genre == 'боевик':
            for i in range(len(spisok29)):
                print(f'Ваш {i + 1} фильм это {spisok29[i]} и ссылка к нему {slovar[spisok29[i]]}')

        elif actor == 'брэд питт' and genre == 'комедия':
            for i in range(len(spisok30)):
                print(f'Ваш {i + 1} фильм это {spisok30[i]} и ссылка к нему {slovar[spisok30[i]]}')

        elif actor == 'колин фаррелл' and genre == 'триллер':
            for i in range(len(spisok31)):
                print(f'Ваш {i + 1} фильм это {spisok31[i]} и ссылка к нему {slovar[spisok31[i]]}')

        elif actor == 'колин фаррелл' and genre == 'криминал':
            for i in range(len(spisok32)):
                print(f'Ваш {i + 1} фильм это {spisok32[i]} и ссылка к нему {slovar[spisok32[i]]}')

        elif actor == 'колин фаррелл' and genre == 'драма':
            for i in range(len(spisok33)):
                print(f'Ваш {i + 1} фильм это {spisok33[i]} и ссылка к нему {slovar[spisok33[i]]}')

        elif actor == 'колин фаррелл' and genre == 'боевик':
            for i in range(len(spisok34)):
                print(f'Ваш {i + 1} фильм это {spisok34[i]} и ссылка к нему {slovar[spisok34[i]]}')

        elif actor == 'колин фаррелл' and genre == 'комедия':
            for i in range(len(spisok35)):
                print(f'Ваш {i + 1} фильм это {spisok35[i]} и ссылка к нему {slovar[spisok35[i]]}')

        elif actor == 'джейк джилленхол' and genre == 'триллер':
            for i in range(len(spisok36)):
                print(f'Ваш {i + 1} фильм это {spisok36[i]} и ссылка к нему {slovar[spisok36[i]]}')

        elif actor == 'джейк джилленхол' and genre == 'криминал':
            for i in range(len(spisok37)):
                print(f'Ваш {i + 1} фильм это {spisok37[i]} и ссылка к нему {slovar[spisok37[i]]}')

        elif actor == 'джейк джилленхол' and genre == 'драма':
            for i in range(len(spisok38)):
                print(f'Ваш {i + 1} фильм это {spisok38[i]} и ссылка к нему {slovar[spisok38[i]]}')

        elif actor == 'джейк джилленхол' and genre == 'боевик':
            for i in range(len(spisok39)):
                print(f'Ваш {i + 1} фильм это {spisok39[i]} и ссылка к нему {slovar[spisok39[i]]}')

        elif actor == 'джейк джилленхол' and genre == 'комедия':
            for i in range(len(spisok40)):
                print(f'Ваш {i + 1} фильм это {spisok40[i]} и ссылка к нему {slovar[spisok40[i]]}')

        elif actor == 'ченнинг татум' and genre == 'триллер':
            for i in range(len(spisok41)):
                print(f'Ваш {i + 1} фильм это {spisok41[i]} и ссылка к нему {slovar[spisok41[i]]}')

        elif actor == 'ченнинг татум' and genre == 'криминал':
            for i in range(len(spisok42)):
                print(f'Ваш {i + 1} фильм это {spisok42[i]} и ссылка к нему {slovar[spisok42[i]]}')

        elif actor == 'ченнинг татум' and genre == 'драма':
            for i in range(len(spisok43)):
                print(f'Ваш {i + 1} фильм это {spisok43[i]} и ссылка к нему {slovar[spisok43[i]]}')

        elif actor == 'ченнинг татум' and genre == 'боевик':
            for i in range(len(spisok44)):
                print(f'Ваш {i + 1} фильм это {spisok44[i]} и ссылка к нему {slovar[spisok44[i]]}')

        elif actor == 'ченнинг татум' and genre == 'комедия':
            for i in range(len(spisok45)):
                print(f'Ваш {i + 1} фильм это {spisok45[i]} и ссылка к нему {slovar[spisok45[i]]}')

        elif actor == 'бен аффлек' and genre == 'триллер':
            for i in range(len(spisok46)):
                print(f'Ваш {i + 1} фильм это {spisok46[i]} и ссылка к нему {slovar[spisok46[i]]}')

        elif actor == 'бен аффлек' and genre == 'криминал':
            for i in range(len(spisok47)):
                print(f'Ваш {i + 1} фильм это {spisok47[i]} и ссылка к нему {slovar[spisok47[i]]}')

        elif actor == 'бен аффлек' and genre == 'драма':
            for i in range(len(spisok48)):
                print(f'Ваш {i + 1} фильм это {spisok48[i]} и ссылка к нему {slovar[spisok48[i]]}')

        elif actor == 'бен аффлек' and genre == 'боевик':
            for i in range(len(spisok49)):
                print(f'Ваш {i + 1} фильм это {spisok49[i]} и ссылка к нему {slovar[spisok49[i]]}')

        elif actor == 'бен аффлек' and genre == 'комедия':
            for i in range(len(spisok50)):
                print(f'Ваш {i + 1} фильм это {spisok50[i]} и ссылка к нему {slovar[spisok50[i]]}')

        else:
            print('Я не нашел то, про что вы писали')

    def storing_incoming_data_for_serial():
        choice_serial = input(
            'Выберите жанр для вашего сериала из списка(драма, комедия, фэнтези, фантастика, криминал, детектив) и '
            'напишите его ').lower()
        if choice_serial == 'драма': 
            for i in range(len(spisokserial1)):
                print(f'Ваш {i + 1} фильм это {spisokserial1[i]} и ссылка к нему {slovar[spisokserial1[i]]}')

        elif choice_serial == 'комедия':
            for i in range(len(spisokserial2)):
                print(f'Ваш {i + 1} фильм это {spisokserial2[i]} и ссылка к нему {slovar[spisokserial2[i]]}')

        elif choice_serial == 'детектив':
            for i in range(len(spisokserial3)):
                print(f'Ваш {i + 1} фильм это {spisokserial3[i]} и ссылка к нему {slovar[spisokserial3[i]]}')

        elif choice_serial == 'фэнтези':
            for i in range(len(spisokserial4)):
                print(f'Ваш {i + 1} фильм это {spisokserial4[i]} и ссылка к нему {slovar[spisokserial4[i]]}')

        elif choice_serial == 'фантастика':
            for i in range(len(spisokserial5)):
                print(f'Ваш {i + 1} фильм это {spisokserial5[i]} и ссылка к нему {slovar[spisokserial5[i]]}')

        elif choice_serial == 'криминал':
            for i in range(len(spisokserial6)):
                print(f'Ваш {i + 1} фильм это {spisokserial6[i]} и ссылка к нему {slovar[spisokserial6[i]]}')

        else:
            print("я не понял, что вы написали")

    if first_message == 'фильм':
        storing_incoming_data_for_movie()
    if first_message == 'сериал':
        storing_incoming_data_for_serial()

    message = input('можете попробовать еще раз напишите продолжить или завершить чтобы завершить ')
    if message == 'продолжить':
        kinopoisk()
    if message == 'завершить':
        print('Спасибо что воспользовались нашим помощником. До свидания')


kinopoisk()
