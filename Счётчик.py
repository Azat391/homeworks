# Счётчик 🔢
class Counter:
    def __init__(self,value=None):
        self.value=value
        if self.value is None:
            self.value=0
    def increment(self):
        self.value+=1
    def reset(self):
        self.value=0
    def get_value(self):
        return self.value
counter = Counter(2)

counter.increment()
counter.increment()
print(counter.get_value())

counter.reset()
print(counter.get_value())