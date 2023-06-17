def proverka(word):
    check = False
    if word == word[::-1]:
        check = True
    print(check)
proverka('лепсспел')