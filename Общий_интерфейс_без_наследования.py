# 5. Общий интерфейс без наследования 🔔
class EmailNotifier:
    def send(self,message):
        return f'Email: {message}'
class SmsNotifier:
    def send(self,message):
        return f'SMS: {message}'
def notify_all(notifiers, message):
    notify=[]
    for i in notifiers:
        notify.append(f'{i.send(message)}')
    return f'{notify}'
notifiers = [EmailNotifier(), SmsNotifier()]

print(notify_all(notifiers, 'Заказ готов'))
class ConsoleNotifier:
    def send(self, message):
        return f'Console: {message}'


print(notify_all([ConsoleNotifier()], 'Проверка'))
print(notify_all([], 'Проверка'))