from logger import Logger


class Repeat:
    @staticmethod
    def run_command(command):
        return command.execute()


class Command(Logger):
    def run_command(self, array_command):
        command = array_command.pop(0)
        response = command.execute()

        if isinstance(response, Exception):
            repeat_response = Repeat.run_command(command)

        if isinstance(repeat_response, Exception):
            self.log(response)


class Repeat2:
    @staticmethod
    def run_command(command):
        response = command.execute()

        if isinstance(response, Exception):
            repeat_response = command.execute()

        return repeat_response


class Command2(Logger):
    def run_command(self, array_command):
        command = array_command.pop(0)
        response = command.execute()

        if isinstance(response, Exception):
            repeat_response = Repeat2.run_command(command)

        if isinstance(repeat_response, Exception):
            self.log(response)
