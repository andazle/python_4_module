import random
print('напиши л или д')
p = ['i', 'o']
a = input()
def i():
    global tu, ut
    print('напиши актера')
    if input() == "хз":
        tu = "хз"
        print('напишите жанр')
        if input() == "зх":
            ut = 'зх'
tu = ''
ut = ''
if a == 'л':
    i()
if tu == "хз" and ut == 'зх':
    print(random.choice(p))