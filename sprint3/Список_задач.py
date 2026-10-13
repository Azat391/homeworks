# Список задач
class TodoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self, text):
        self.tasks.append(text)
    def remove_task(self,text):
        if text in self.tasks:
            self.tasks.remove(text)
            return True
        else:
            return False
    def get_tasks(self):
        return self.tasks.copy()
todo = TodoList()
todo.add_task('Прочитать урок')

tasks = todo.get_tasks()
tasks.append('Посторонняя задача')

print(todo.get_tasks())