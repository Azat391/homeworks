# Голоса животных 🐈🐕
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return 'Неизвестный звук'
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return 'Гав'
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return 'Мяу'
def collect_voices(animals):
    collect=[]
    if len(animals)==0:
        return f'{collect}'
    for i in animals:
        collect.append(f'{i.name}: {i.speak()}')
    return f'{collect}'
# animals = [
#     Cat('Мурка'),
#     Dog('Шарик'),
#     Animal('Неизвестный')
# ]
# print(collect_voices(animals))
print(collect_voices([]))