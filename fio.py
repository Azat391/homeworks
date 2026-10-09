#Практика 2

#ФИО
def print_fio(name, surname, patronymic):
    
    print(f'{name.title()}'+' '+f'{surname.title()}'+' '+f'{patronymic.title()}')
name, surname, patronymic= input().split()
print_fio(name, surname, patronymic)