class Logger:
    def __init__(self, log_file='log.txt'):
        self.file = log_file

    def log(self, error):
        with open(self.file, "a") as file:
            file.write(f'Ошибка - {error.__str__()}\n')
