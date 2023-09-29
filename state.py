class State(object):
    def __init__(self, semaforo):
        self.semaforo = semaforo

    def read_green(self):
        pass

    def read_yellow(self):
        pass

    def read_red(self):
        pass


class Red(State):
    def read_green(self):
        print("Verde")
        self.semaforo.current_state = self.semaforo.green

    def read_yellow(self):
        print("Amarelo")
        self.semaforo.current_state = self.semaforo.yellow


class Yellow(State):
    def read_red(self):
        print("Vermelhor")
        self.semaforo.current_state = self.semaforo.red

    def read_green(self):
        print("Verde")
        self.semaforo.current_state = self.semaforo.green


class Green(State):
    def read_yellow(self):
        print("Amarelo")
        self.semaforo.current_state = self.semaforo.yellow

    def read_red(self):
        print("Algo de errado n esta certo")


class Semaforo:
    def __init__(self):
        self.red = Red(self)
        self.yellow = Yellow(self)
        self.green = Green(self)
        self.current_state = self.green


semaforo = Semaforo()
semaforo.current_state.read_yellow()
semaforo.current_state.read_red()
semaforo.current_state.read_green()
