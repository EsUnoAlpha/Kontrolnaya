class Worker:
    def __init__(self, name, job, expirience):
        self.name = name
        self.job = job
        self.expirience = expirience

    def print_info(self):
        return ('Имя: ' + self.name + ' Должность: ' + self.job + ' Стаж: ' + self.expirience)


    @staticmethod
    def staticmethod(expirience):
        if expirience % 10 == 2 or expirience == 3 or expirience == 4:
            return 'года'
        else:
            return 'лет'





man = Worker('Василий', 'Системный администратор', '21')
print(man.print_info(), man.staticmethod(21))
