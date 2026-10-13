#Пермское время
def print_perm_time_call(msc_time):
    msc_time=msc_time.split(':')
    msc_time[0]=str(int(msc_time[0])+2)
    perm_time=':'.join(msc_time)

    print(f'Созвон будет в {perm_time}')
msc_time=input()
print_perm_time_call(msc_time)