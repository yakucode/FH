class Queue:
    def __init__(self):
        self.__liste = []

    def arrive(self, name):
        self.__liste.append(name)
        print(f"{name} has joined the queue")

    def output(self):
        print(self.__liste)

    def exit(self):
        print(f"{self.__liste[0]} has left the queue")
        self.__liste.pop(0)


q = Queue()
q.output()
q.arrive("Schahed")
q.arrive("Assgoblin")
q.arrive("TESTERMESTER")
q.output()
q.exit()
q.exit()
q.output()
q.exit()
