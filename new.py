from pprint import pprint

goods = [
 {
    'name': 'Iphone 14',
    'brand': 'Apple',
    'price': 1200
},
{
    'name': 'Samsung Galaxy A53',
    'brand': 'Samsung',
    'price': 600
},
{
    'name': 'Xiaomi Mi 10T',
    'brand': 'Xiaomi',
    'price': 400
}
    ]

# def item_price(item):
# return item['price']

pprint(sorted(goods, key=lambda item: item['price']))

# все товары бренда Apple
apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
print(apple_list)

# функцию map
numbers = ['1', '2', '3', '4', '5']
numbers = list(map(int, numbers))
print(numbers)

names = ['Данил', 'Никита', 'Настя']
surnames = ['Петров', 'Иванов', 'Смирнова']

full_names = list(map(lambda name, surname: f'{name} {surname}', names, surnames))
print(full_names)

# функция enumerate
indexed_goods = []
for index, item in enumerate(goods):
    indexed_goods.append({index: item})
    pprint(indexed_goods)

# функция zip
patronymics = ['Михайлович', 'Витальевич', 'Ивановна']
for name, surname, patronymic in zip(names, surnames, patronymics):
    print(surname, name, patronymic)

print(__name__)