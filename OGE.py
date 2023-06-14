class Myfile:

    def __init__(self, name, type_of_reading, kodirovka):
        self.name = name
        self.type_of_reading = type_of_reading
        self.kodirovka = "utf-8"

    def myfile(self, name, type_of_reading, kodirovka):
        with open(f'./{name}', type_of_reading, encoding=kodirovka) as f:
            print(f.read())


file = Myfile('txtx', 'r', "utf-8")
print(file)