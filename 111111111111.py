class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def days(self):
        return self.__days

    @property
    def season(self):
        return self.__season


    def set_days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception('Неверное кол-во дней в году')

    def set_season(self, season):
        self.__season = season


year = Year(25, 'winter')


# year.set_days(366)
# year.set_season('summer')

#print(year.days)
#print(year.season)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def fullname(self):
        del self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def fullname(self):
        del self.age


person = Person('Ваня', -7)
del person.name
del person.age
print(person.name)
print(person.age)
