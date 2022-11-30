class StepCounter:
    def __init__(self, date):
        self.__date = date
        self.__steps = 0

    def incrementSteps(self):
        self.__steps += 1

    def getSteps(self):
        return self.__steps


sc = StepCounter("11.11.2022")

for i in range(0, 1111):
    sc.incrementSteps()

print(sc.getSteps())
